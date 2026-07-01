import sys
from scapy.all import rdpcap, wrpcap
from cicflowmeter.flow_session import FlowSession

# Paths
input_pcap = "dataset/live_traffic.pcap"
output_csv = "dataset/live_traffic_cic.csv"

print(f"📁 Reading PCAP: {input_pcap}")

# Create FlowSession
session = FlowSession()

# Read and process packets
packets = rdpcap(input_pcap)
print(f"📦 Processing {len(packets)} packets...")

for packet in packets:
    session.on_packet_received(packet)

# Write flows to CSV
session.write_flows(output_csv)
print(f"✅ Flows written to: {output_csv}")
