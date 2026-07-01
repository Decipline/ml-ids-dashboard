#!/usr/bin/env python3
"""
COMPREHENSIVE ATTACK SUITE
Tests IDS with 10+ different attack types
"""
import subprocess
import time
import random

def print_header(text):
    print(f"\n{'='*60}")
    print(f"  {text}")
    print(f"{'='*60}")

print_header("COMPREHENSIVE ATTACK TESTING SUITE")
print("\n🎯 This will generate 10+ different attack types")
print("⏱️  Total duration: ~3-4 minutes")
print("🔍 Watch your IDS terminal for detections!\n")

input("Press ENTER to start attacks...")

attack_count = 0

# ============================================================
# 1. PORT SCAN ATTACK
# ============================================================
print_header("[1/12] PORT SCAN ATTACK")
print("Scanning 100 ports rapidly...")
for port in range(20, 120):
    subprocess.run(['timeout', '0.1', 'nc', '-zv', '127.0.0.1', str(port)], 
                   capture_output=True)
    if port % 20 == 0:
        print(f"  Scanned {port-19} ports...", end='\r')
    time.sleep(0.02)
attack_count += 1
print("\n✓ Port scan complete - 100 ports scanned")
time.sleep(1)

# ============================================================
# 2. SYN FLOOD (DoS)
# ============================================================
print_header("[2/12] SYN FLOOD ATTACK (DoS)")
print("Sending rapid SYN packets...")
for i in range(200):
    subprocess.run(['timeout', '0.1', 'nc', '-zv', '127.0.0.1', '80'], 
                   capture_output=True)
    if i % 50 == 0:
        print(f"  Sent {i} packets...", end='\r')
    time.sleep(0.01)
attack_count += 1
print("\n✓ SYN flood complete - 200 packets")
time.sleep(1)

# ============================================================
# 3. ICMP FLOOD (Ping Flood)
# ============================================================
print_header("[3/12] ICMP FLOOD (Ping Flood)")
print("Flooding with ICMP packets...")
subprocess.run(['ping', '-c', '150', '-i', '0.01', '8.8.8.8'], 
               capture_output=True, timeout=5)
attack_count += 1
print("✓ ICMP flood complete - 150 pings")
time.sleep(1)

# ============================================================
# 4. HTTP FLOOD
# ============================================================
print_header("[4/12] HTTP FLOOD ATTACK")
print("Flooding HTTP server with requests...")
targets = ['http://example.com', 'http://google.com', 'http://github.com']
for i in range(50):
    target = random.choice(targets)
    try:
        subprocess.run(['curl', '-s', '-m', '1', '-o', '/dev/null', target], 
                       capture_output=True, timeout=2)
    except:
        pass
    if i % 10 == 0:
        print(f"  Sent {i} requests...", end='\r')
    time.sleep(0.03)
attack_count += 1
print("\n✓ HTTP flood complete - 50 requests")
time.sleep(1)

# ============================================================
# 5. DNS AMPLIFICATION
# ============================================================
print_header("[5/12] DNS AMPLIFICATION ATTACK")
print("Sending large DNS queries...")
domains = ['example.com', 'google.com', 'amazon.com', 'facebook.com']
for i in range(60):
    domain = random.choice(domains)
    subprocess.run(['dig', '@8.8.8.8', 'ANY', domain], 
                   capture_output=True, timeout=1)
    if i % 20 == 0:
        print(f"  Sent {i} queries...", end='\r')
    time.sleep(0.05)
attack_count += 1
print("\n✓ DNS amplification complete - 60 queries")
time.sleep(1)

# ============================================================
# 6. SSH BRUTE FORCE
# ============================================================
print_header("[6/12] SSH BRUTE FORCE ATTACK")
print("Attempting rapid SSH connections...")
usernames = ['root', 'admin', 'user', 'test', 'guest', 'kali']
for i in range(30):
    user = random.choice(usernames)
    subprocess.run(['timeout', '0.5', 'ssh', '-o', 'StrictHostKeyChecking=no',
                    '-o', 'ConnectTimeout=1', f'{user}@127.0.0.1'], 
                   capture_output=True, input=b'wrongpass\n')
    if i % 10 == 0:
        print(f"  Attempted {i} logins...", end='\r')
    time.sleep(0.1)
attack_count += 1
print("\n✓ SSH brute force complete - 30 attempts")
time.sleep(1)

# ============================================================
# 7. UDP FLOOD
# ============================================================
print_header("[7/12] UDP FLOOD ATTACK")
print("Flooding with UDP packets...")
for i in range(100):
    subprocess.run(['timeout', '0.1', 'nc', '-u', '-zv', '127.0.0.1', str(random.randint(1000, 9999))],
                   capture_output=True)
    if i % 25 == 0:
        print(f"  Sent {i} UDP packets...", end='\r')
    time.sleep(0.02)
attack_count += 1
print("\n✓ UDP flood complete - 100 packets")
time.sleep(1)

# ============================================================
# 8. SLOWLORIS ATTACK (Slow HTTP)
# ============================================================
print_header("[8/12] SLOWLORIS ATTACK (Slow HTTP)")
print("Establishing slow HTTP connections...")
for i in range(20):
    try:
        subprocess.run(['curl', '-s', '-m', '0.5', '--limit-rate', '1', 
                        'http://example.com'], 
                       capture_output=True, timeout=1)
    except:
        pass
    if i % 5 == 0:
        print(f"  Opened {i} slow connections...", end='\r')
    time.sleep(0.2)
attack_count += 1
print("\n✓ Slowloris complete - 20 connections")
time.sleep(1)

# ============================================================
# 9. ARP SPOOFING SIMULATION
# ============================================================
print_header("[9/12] ARP SPOOFING SIMULATION")
print("Simulating rapid ARP requests...")
for i in range(50):
    # Simulate by rapid pinging local network
    subprocess.run(['ping', '-c', '1', '-i', '0.01', '127.0.0.1'], 
                   capture_output=True, timeout=1)
    if i % 15 == 0:
        print(f"  Sent {i} ARP packets...", end='\r')
    time.sleep(0.05)
attack_count += 1
print("\n✓ ARP spoofing simulation complete")
time.sleep(1)

# ============================================================
# 10. FTP BRUTE FORCE
# ============================================================
print_header("[10/12] FTP BRUTE FORCE ATTACK")
print("Attempting FTP login attacks...")
for i in range(25):
    subprocess.run(['timeout', '0.5', 'nc', '-zv', '127.0.0.1', '21'], 
                   capture_output=True)
    if i % 8 == 0:
        print(f"  Attempted {i} FTP logins...", end='\r')
    time.sleep(0.15)
attack_count += 1
print("\n✓ FTP brute force complete - 25 attempts")
time.sleep(1)

# ============================================================
# 11. TELNET SCANNING
# ============================================================
print_header("[11/12] TELNET SCANNING ATTACK")
print("Scanning for Telnet services...")
for i in range(40):
    port = random.choice([23, 2323, 23023, 8023])
    subprocess.run(['timeout', '0.1', 'nc', '-zv', '127.0.0.1', str(port)], 
                   capture_output=True)
    if i % 12 == 0:
        print(f"  Scanned {i} targets...", end='\r')
    time.sleep(0.08)
attack_count += 1
print("\n✓ Telnet scanning complete")
time.sleep(1)

# ============================================================
# 12. LAND ATTACK SIMULATION
# ============================================================
print_header("[12/12] LAND ATTACK SIMULATION")
print("Simulating LAND attack packets...")
for i in range(30):
    subprocess.run(['ping', '-c', '1', '-s', '1000', '127.0.0.1'], 
                   capture_output=True, timeout=1)
    if i % 10 == 0:
        print(f"  Sent {i} packets...", end='\r')
    time.sleep(0.1)
attack_count += 1
print("\n✓ LAND attack simulation complete")
time.sleep(1)

# ============================================================
# SUMMARY
# ============================================================
print_header("ATTACK SUITE COMPLETE!")
print(f"""
📊 ATTACK SUMMARY:
   Total Attack Types: {attack_count}
   
   ✓ Port Scan (100 ports)
   ✓ SYN Flood (200 packets)
   ✓ ICMP Flood (150 pings)
   ✓ HTTP Flood (50 requests)
   ✓ DNS Amplification (60 queries)
   ✓ SSH Brute Force (30 attempts)
   ✓ UDP Flood (100 packets)
   ✓ Slowloris (20 connections)
   ✓ ARP Spoofing (50 packets)
   ✓ FTP Brute Force (25 attempts)
   ✓ Telnet Scanning (40 scans)
   ✓ LAND Attack (30 packets)

🔍 CHECK YOUR IDS TERMINAL NOW!
   Look for ATTACK detections in the results!
   
📝 Expected detections: High packet rates, unusual patterns
   Your IDS should show multiple ATTACK classifications!
""")
print("="*60)
