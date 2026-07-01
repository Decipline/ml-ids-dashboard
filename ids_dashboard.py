# File: ids_dashboard.py
import streamlit as st
import pandas as pd
import time

# --- CONFIG ---
CSV_PATH = "/home/kali/ML_IDS_Project/results.csv"

# --- DASHBOARD SETUP ---
st.set_page_config(page_title="ML-IDS Dashboard", layout="wide")
st.title("🚨 ML-IDS + IPS Real-Time Dashboard")

# Sidebar options
st.sidebar.header("Settings")
refresh_rate = st.sidebar.slider("Refresh Rate (seconds)", min_value=1, max_value=10, value=5)

# Placeholders for dynamic content
summary_placeholder = st.empty()
pie_placeholder = st.empty()
table_placeholder = st.empty()

# --- HELPER FUNCTIONS ---
def load_data():
    try:
        df = pd.read_csv(CSV_PATH)
        return df
    except:
        return pd.DataFrame()

def get_attack_summary(df):
    if df.empty:
        return {"Flows":0, "Attacks":0, "Blocked":0}
    attacks = df[df['Prediction']==1] if 'Prediction' in df.columns else df.iloc[:,1]>0
    blocked_ips = df['Src IP'].unique() if 'Src IP' in df.columns else []
    return {"Flows": len(df), "Attacks": len(attacks), "Blocked": len(blocked_ips), "Blocked_IPs": blocked_ips}

# --- MAIN LOOP ---
while True:
    df = load_data()
    summary = get_attack_summary(df)

    # Summary stats
    summary_placeholder.markdown(
        f"""
        **Total Flows Analyzed:** {summary['Flows']}  
        **Attacks Detected:** {summary['Attacks']}  
        **IPs Blocked:** {summary['Blocked']}  
        """
    )

    # Pie chart for attack types
    if 'Attack_Type' in df.columns:
        attack_counts = df['Attack_Type'].value_counts()
        pie_placeholder.bar_chart(attack_counts)
    else:
        pie_placeholder.markdown("**No Attack_Type column found in CSV**")

    # Blocked IP table
    if 'Blocked_IPs' in summary:
        blocked_df = pd.DataFrame(summary['Blocked_IPs'], columns=["Blocked IPs"])
        table_placeholder.table(blocked_df)
    else:
        table_placeholder.markdown("No blocked IPs found yet.")

    time.sleep(refresh_rate)
