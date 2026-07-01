import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

print("🔍 Analyzing all prediction files...\n")

# Check both prediction files
files = ['predictions.csv', 'new_predictions.csv']

for file in files:
    if os.path.exists(file):
        print(f"\n{'='*50}")
        print(f"📁 File: {file}")
        print(f"{'='*50}")
        
        df = pd.read_csv(file)
        print(f"Total rows: {len(df):,}")
        print(f"File size: {os.path.getsize(file) / (1024*1024):.2f} MB")
        
        print("\n📊 Prediction Distribution:")
        counts = df['Predicted_Label'].value_counts()
        for label, count in counts.items():
            percentage = (count / len(df)) * 100
            print(f"  {label}: {count:,} ({percentage:.3f}%)")
        
        # Find attacks
        attacks = df[df['Predicted_Label'] != 'BENIGN']
        if len(attacks) > 0:
            print(f"\n⚠️  Found {len(attacks)} ATTACKS!")
            print("\nAttack Details:")
            print(attacks[['Destination Port', 'Flow Duration', 'Total Fwd Packets', 
                          'Total Backward Packets', 'Flow Bytes/s', 'Predicted_Label']].to_string())
        else:
            print("\n✅ No attacks detected in this file")

print("\n" + "="*50)
print("Analysis complete!")
