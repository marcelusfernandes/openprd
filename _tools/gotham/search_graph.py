#!/usr/bin/env python3
"""Explore entity relationships in Palantir Gotham graph.

Usage:
    python search_graph.py --rid ri.gotham.object.123 --depth 2
    python search_graph.py --rid ri.gotham.object.123 --link-types "WORKS_FOR,LOCATED_IN"

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


def get_object(token, rid):
    """Get a single Gotham object by RID."""
    hostname = os.environ["GOTHAM_HOSTNAME"]
    req = Request(
        f"{hostname}/gotham/api/graph/v1/objects/{rid}",
        headers={"Authorization": f"Bearer {token}"},
    )
    with urlopen(req) as resp:
        return json.loads(resp.read())


def get_links(token, rid, link_types=None):
    """Get relationships for a Gotham object."""
    hostname = os.environ["GOTHAM_HOSTNAME"]
    url = f"{hostname}/gotham/api/graph/v1/objects/{rid}/links"
    if link_types:
        url += f"?linkTypes={','.join(link_types)}"
    req = Request(url, headers={"Authorization": f"Bearer {token}"})
    with urlopen(req) as resp:
        return json.loads(resp.read())


def explore_graph(token, rid, depth=1, link_types=None, visited=None):
    """Recursively explore graph from a starting object."""
    if visited is None:
        visited = set()
    if rid in visited or depth < 0:
        return None
    visited.add(rid)

    obj = get_object(token, rid)
    links = get_links(token, rid, link_types)

    result = {
        "object": obj,
        "links": [],
    }

    if depth > 0 and "links" in links:
        for link in links["links"][:20]:  # Cap at 20 links per node
            target_rid = link.get("targetRid") or link.get("targetObjectRid")
            if target_rid and target_rid not in visited:
                child = explore_graph(token, target_rid, depth - 1, link_types, visited)
                result["links"].append({
                    "linkType": link.get("linkType", "unknown"),
                    "targetRid": target_rid,
                    "target": child,
                })

    return result


def main():
    parser = argparse.ArgumentParser(description="Explore Gotham graph")
    parser.add_argument("--rid", required=True, help="Starting object RID")
    parser.add_argument("--depth", type=int, default=1, help="Exploration depth (default: 1)")
    parser.add_argument("--link-types", help="Comma-separated link types to follow")
    parser.add_argument("--output", help="Output file (JSON)")
    args = parser.parse_args()

    for var in ("GOTHAM_HOSTNAME", "GOTHAM_CLIENT_ID", "GOTHAM_CLIENT_SECRET"):
        if var not in os.environ:
            print(f"Error: {var} environment variable not set", file=sys.stderr)
            sys.exit(1)

    token = get_token()
    link_types = args.link_types.split(",") if args.link_types else None
    graph = explore_graph(token, args.rid, args.depth, link_types)

    output = json.dumps(graph, indent=2, ensure_ascii=False)
    if args.output:
        with open(args.output, "w") as f:
            f.write(output)
        print(f"Graph written to {args.output}")
    else:
        print(output)


if __name__ == "__main__":
    main()
