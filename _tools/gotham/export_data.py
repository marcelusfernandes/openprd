#!/usr/bin/env python3
"""Export Palantir Gotham data for discovery pipeline analysis.

Usage:
    python export_data.py --type customer --query "segment:enterprise" --format md
    python export_data.py --type interaction --query "date>2026-01-01" --format json --output data.json

Requires env vars: GOTHAM_HOSTNAME, GOTHAM_CLIENT_ID, GOTHAM_CLIENT_SECRET
"""

import argparse
import json
import os
import sys
from datetime import datetime
from urllib.request import Request, urlopen
from urllib.parse import urlencode


def get_token():
    """Get OAuth2 token via client credentials grant."""
    hostname = os.environ["GOTHAM_HOSTNAME"]
    data = urlencode({
        "grant_type": "client_credentials",
        "client_id": os.environ["GOTHAM_CLIENT_ID"],
        "client_secret": os.environ["GOTHAM_CLIENT_SECRET"],
    }).encode()
    req = Request(
        f"{hostname}/multipass/api/oauth2/token",
        data=data,
        headers={"Content-Type": "application/x-www-form-urlencoded"},
    )
    with urlopen(req) as resp:
        return json.loads(resp.read())["access_token"]


def search_objects(token, object_type, query, limit=500):
    """Search Gotham objects."""
    hostname = os.environ["GOTHAM_HOSTNAME"]
    payload = json.dumps({
        "query": query,
        "objectTypes": [object_type],
        "limit": limit,
    }).encode()
    req = Request(
        f"{hostname}/gotham/api/graph/v1/objects/search",
        data=payload,
        headers={
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
        },
    )
    with urlopen(req) as resp:
        return json.loads(resp.read())


def format_as_markdown(data, object_type, query):
    """Format Gotham data as discovery-compatible markdown."""
    objects = data.get("objects", [])
    today = datetime.now().strftime("%Y-%m-%d")

    lines = [
        f"# Gotham Data Export — {object_type}",
        f"**Query:** {query}",
        f"**Date:** {today}",
        f"**Objects:** {len(objects)}",
        "",
        f"[Source: Gotham, object_type={object_type}, query_date={today}]",
        f"[Gotham data: N={len(objects)}, types={object_type}]",
        "",
        "## Objects",
        "",
    ]

    for i, obj in enumerate(objects, 1):
        rid = obj.get("rid", "unknown")
        title = obj.get("title", obj.get("name", f"Object {i}"))
        obj_type = obj.get("objectType", object_type)
        lines.append(f"### {i}. {title}")
        lines.append(f"- **RID:** `{rid}`")
        lines.append(f"- **Type:** {obj_type}")

        properties = obj.get("properties", {})
        for key, value in properties.items():
            if value is not None:
                lines.append(f"- **{key}:** {value}")
        lines.append("")

    lines.extend([
        "## Summary",
        f"- Total objects: {len(objects)}",
        f"- Object type: {object_type}",
        f"- Query: {query}",
        "",
        "---",
        f"*Exported from Palantir Gotham on {today}*",
    ])

    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="Export Gotham data")
    parser.add_argument("--type", required=True, help="Object type to export")
    parser.add_argument("--query", default="*", help="Search query")
    parser.add_argument("--limit", type=int, default=500, help="Max objects")
    parser.add_argument("--format", choices=["json", "md"], default="md", help="Output format")
    parser.add_argument("--output", help="Output file path")
    args = parser.parse_args()

    for var in ("GOTHAM_HOSTNAME", "GOTHAM_CLIENT_ID", "GOTHAM_CLIENT_SECRET"):
        if var not in os.environ:
            print(f"Error: {var} environment variable not set", file=sys.stderr)
            sys.exit(1)

    token = get_token()
    data = search_objects(token, args.type, args.query, args.limit)

    if args.format == "md":
        output = format_as_markdown(data, args.type, args.query)
    else:
        output = json.dumps(data, indent=2, ensure_ascii=False)

    if args.output:
        with open(args.output, "w") as f:
            f.write(output)
        print(f"Exported to {args.output}")
    else:
        print(output)


if __name__ == "__main__":
    main()
