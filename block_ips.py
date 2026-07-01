#!/usr/bin/env python3
import subprocess
from datetime import datetime

print("="*60)
print("ML-IDS IPS - IP Blocker")
print("="*60)

malicious_ips = ['192.168.1.100', '10.0.0.50', '172.16.0.88']

print(f"\n[*] Found {len(malicious_ips)} malicious IPs to block")

for ip in malicious_ips:
    print(f"\n[*] Blocking IP: {ip}")
    cmd = f"sudo iptables -A INPUT -s {ip} -j DROP"
    print(f"    Command: {cmd}")
    print("    (In production, this would block the IP)")
    
    # Save to log
    with open('logs/blocked_ips.txt', 'a') as f:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"{timestamp},{ip}\n")

print("\n" + "="*60)
print("IPS Summary")
print("="*60)
print(f"✓ {len(malicious_ips)} IPs logged for blocking")
print("✓ Log saved to: logs/blocked_ips.txt")

# Show log
print("\nBlocked IPs Log:")
with open('logs/blocked_ips.txt', 'r') as f:
    print(f.read())

print("="*60)
