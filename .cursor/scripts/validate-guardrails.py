#!/usr/bin/env python3
"""
Deterministic guardrail validator for agent outputs.
Runs as a Cursor hook after file edits in 1-problem/, 2-solution/, 3-delivery/.
Exit code 2 = block (critical violation found).
Exit code 0 = pass (no violations or only warnings).
"""
import json
import re
import sys


def read_stdin_context():
    """Read the hook context from stdin (JSON with file path and content)."""
    try:
        data = json.load(sys.stdin)
        return data.get("file", ""), data.get("content", "")
    except (json.JSONDecodeError, EOFError):
        return "", ""


def check_untagged_dollars(content: str) -> list[str]:
    """Find dollar amounts not followed by an [AI estimation] or [Source:] tag."""
    violations = []
    for match in re.finditer(r'\$[\d,.]+[KkMmBb]?(?:\s*-\s*\$[\d,.]+[KkMmBb]?)?', content):
        context_after = content[match.end():match.end() + 200]
        if not re.search(r'\[(?:AI estimation|Source:|Assumption:)', context_after[:100]):
            violations.append(f"Untagged dollar amount: {match.group()}")
    return violations


def check_untagged_percentages(content: str) -> list[str]:
    """Find specific percentages not near a tag or source reference."""
    violations = []
    pattern = r'(\d+(?:\.\d+)?)\s*%'
    for match in re.finditer(pattern, content):
        start = max(0, match.start() - 100)
        end = min(len(content), match.end() + 100)
        surrounding = content[start:end]
        if not re.search(r'\[(?:AI estimation|Source:|Assumption:|Uncertain:)', surrounding):
            if not re.search(r'(?:WCAG|uptime|coverage|99\.\d|OCEAN)', surrounding):
                violations.append(f"Untagged percentage: {match.group()}")
    return violations


def check_untagged_roi(content: str) -> list[str]:
    """Find ROI claims without proper tagging."""
    violations = []
    roi_patterns = [
        r'ROI\s+(?:of\s+)?\d+',
        r'(?:saves?|worth|costs?)\s+\$[\d,.]+',
        r'guaranteed\s+(?:improvement|reduction|return)',
    ]
    for pat in roi_patterns:
        for match in re.finditer(pat, content, re.IGNORECASE):
            context = content[max(0, match.start() - 50):match.end() + 100]
            if not re.search(r'\[(?:AI estimation|Source:)', context):
                violations.append(f"Untagged ROI/guarantee claim: {match.group()}")
    return violations


def validate(file_path: str, content: str) -> tuple[list[str], list[str]]:
    """Return (critical_violations, warnings)."""
    criticals = []
    warnings = []

    criticals.extend(check_untagged_dollars(content))
    criticals.extend(check_untagged_roi(content))

    pct_issues = check_untagged_percentages(content)
    if file_path.startswith("1-problem/"):
        criticals.extend(pct_issues)
    else:
        warnings.extend(pct_issues)

    return criticals, warnings


def main():
    file_path, content = read_stdin_context()

    if not content:
        try:
            content = sys.stdin.read()
        except Exception:
            pass

    if not content:
        sys.exit(0)

    criticals, warnings = validate(file_path, content)

    if criticals:
        output = {
            "status": "blocked",
            "critical_violations": criticals[:10],
            "message": f"GUARDRAIL VIOLATION: {len(criticals)} critical issue(s) found. "
                       f"Add [AI estimation based on X] or [Source: file.md] tags."
        }
        json.dump(output, sys.stderr)
        sys.exit(2)

    if warnings:
        output = {
            "status": "warning",
            "warnings": warnings[:5],
            "message": f"Guardrail advisory: {len(warnings)} item(s) should be reviewed."
        }
        json.dump(output, sys.stderr)

    sys.exit(0)


if __name__ == "__main__":
    main()
