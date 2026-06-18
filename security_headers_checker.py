#!/usr/bin/env python3

import requests
import sys

HEADERS = [
    "Content-Security-Policy",
    "Strict-Transport-Security",
    "X-Frame-Options",
    "X-Content-Type-Options",
    "Referrer-Policy",
    "Permissions-Policy"
]

print("""
=========================================================
 Security Headers Checker
 Developed by Mohamed Bou ("HermosZ888")
=========================================================
""")

if len(sys.argv) != 2:
    print(f"Usage: python3 {sys.argv[0]} https://example.com")
    sys.exit(1)

url = sys.argv[1]

try:
    response = requests.get(url, timeout=10)

    print(f"\nTarget: {url}")
    print(f"Status Code: {response.status_code}")
    print("-" * 50)

    score = 0

    for header in HEADERS:
        if header in response.headers:
            print(f"[+] {header}")
            score += 1
        else:
            print(f"[-] {header}")

    print("-" * 50)
    print(f"Security Score: {score}/{len(HEADERS)}")

except Exception as e:
    print(f"Error: {e}")