#!/usr/bin/env python3
"""Query Palantir Gotham objects via REST API.

Usage:
    python query_objects.py --type customer --query "healthcare" --limit 50
    python query_objects.py --type user --query "active" --output results.json

Requires env vars: GOTHAM_HOSTNAME, GOTHAM_CLIENT_ID, GOTHAM_CLIENT_SECRET
"""

import argparse
import json
import os
import sys
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


def search_objects(token, object_type, query, limit=100):
    """Search Gotham objects by type and query string."""
    hostname = os.environ["GOTHAM_HOSTNAME"]
    payload = json.dumps({
        "query": query,
        "objectTypes": [object_type] if object_type else [],
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


def main():
    parser = argparse.ArgumentParser(description="Query Gotham objects")
    parser.add_argument("--type", required=True, help="Object type to search")
    parser.add_argument("--query", default="*", help="Search query string")
    parser.add_argument("--limit", type=int, default=100, help="Max results")
    parser.add_argument("--output", help="Output file (JSON). Prints to stdout if omitted")
    args = parser.parse_args()

    for var in ("GOTHAM_HOSTNAME", "GOTHAM_CLIENT_ID", "GOTHAM_CLIENT_SECRET"):
        if var not in os.environ:
            print(f"Error: {var} environment variable not set", file=sys.stderr)
            sys.exit(1)

    token = get_token()
    results = search_objects(token, args.type, args.query, args.limit)

    output = json.dumps(results, indent=2, ensure_ascii=False)
    if args.output:
        with open(args.output, "w") as f:
            f.write(output)
        print(f"Results written to {args.output}")
    else:
        print(output)


if __name__ == "__main__":
    main()
