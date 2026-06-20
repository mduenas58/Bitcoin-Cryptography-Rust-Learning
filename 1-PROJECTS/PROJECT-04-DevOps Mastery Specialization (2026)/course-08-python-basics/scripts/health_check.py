#\!/usr/bin/env python3
"""
Health-check script: polls a list of URLs and reports status.
Usage: python health_check.py
"""
import requests
import json
from datetime import datetime

ENDPOINTS = [
    {"name": "Main App",    "url": "http://localhost:3000/health"},
    {"name": "API Gateway", "url": "http://localhost:8080/ping"},
]

TIMEOUT = 5  # seconds


def check(endpoint: dict) -> dict:
    try:
        resp = requests.get(endpoint["url"], timeout=TIMEOUT)
        return {
            "name":    endpoint["name"],
            "url":     endpoint["url"],
            "status":  resp.status_code,
            "ok":      resp.ok,
            "latency": f"{resp.elapsed.total_seconds() * 1000:.0f}ms",
        }
    except requests.RequestException as exc:
        return {
            "name":    endpoint["name"],
            "url":     endpoint["url"],
            "status":  None,
            "ok":      False,
            "latency": "N/A",
            "error":   str(exc),
        }


def main():
    print(f"\n🩺 Health Check — {datetime.utcnow().isoformat()}Z\n")
    results = [check(ep) for ep in ENDPOINTS]
    for r in results:
        icon = "✅" if r["ok"] else "❌"
        print(f"{icon}  {r['name']:20s} {str(r['status']):>4}  {r['latency']}")
        if "error" in r:
            print(f"     Error: {r['error']}")
    print()
    failed = [r for r in results if not r["ok"]]
    if failed:
        print(f"⚠️  {len(failed)} endpoint(s) unhealthy\!")
        raise SystemExit(1)


if __name__ == "__main__":
    main()
