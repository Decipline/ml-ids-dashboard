#!/usr/bin/env python3
import subprocess
import time

print("="*60)
print("     GENERATING ATTACK TRAFFIC FOR IDS TESTING")
print("="*60)

print("\n[1/4] Port Scan Attack...")
for port in range(20, 100, 5):
    subprocess.run(['timeout', '0.1', 'nc', '-zv', '127.0.0.1', str(port)], 
                   capture_output=True)
    time.sleep(0.05)
print("✓ Port scan complete\n")

print("[2/4] Ping Flood...")
subprocess.run(['ping', '-c', '100', '-i', '0.01', '8.8.8.8'], 
               capture_output=True, timeout=5)
print("✓ Ping flood complete\n")

print("[3/4] HTTP Flood...")
for i in range(30):
    try:
        subprocess.run(['curl', '-s', '-m', '2', '-o', '/dev/null', 'http://example.com'], 
                       capture_output=True, timeout=3)
    except:
        pass
    time.sleep(0.05)
print("✓ HTTP flood complete\n")

print("[4/4] DNS Flood...")
for i in range(50):
    subprocess.run(['dig', '@8.8.8.8', 'example.com'], 
                   capture_output=True, timeout=1)
    time.sleep(0.02)
print("✓ DNS flood complete\n")

print("="*60)
print("ALL ATTACKS COMPLETE!")
print("Check the IDS terminal for detections!")
print("="*60)
