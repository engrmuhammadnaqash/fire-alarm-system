import streamlit as st
import pandas as pd

# App ka Title aur Description
st.set_page_config(page_title="Fire Alarm MTO Generator", layout="wide")
st.title("🔥 Professional Fire Alarm System Designer")
st.write("Area aur Building type select karein, system khud-ba-khud design ho kar table format mein aa jayega.")

# User Input Section
col1, col2 = st.columns(2)
with col1:
    area = st.number_input("Area size (Square Meters) enter karein:", min_value=1, value=100)
with col2:
    b_type = st.selectbox("Building Type select karein:", ["Office", "Warehouse", "Residential", "Industrial"])

# Calculation Logic (NFPA standards ke mutabiq)
qty_smoke = max(1, round(area / 60))
qty_mcp = max(1, round(area / 150))
qty_sounder = max(1, round(qty_smoke / 4))
qty_cable = area * 2.5 # Farzi calculation cable ke liye

# Data for the Table - Bilkul aapke headers ke mutabiq
mto_data = {
    "Sr #": [1, 2, 3, 4, 5],
    "Item description": [
        "Addressable Smoke Detector with Base", 
        "Addressable Manual Call Point (MCP)", 
        "Fire Alarm Sounder / Beacon", 
        "Addressable Fire Alarm Control Panel (LPCB Approved)",
        "2C x 1.5mm Fire Rated Shielded Cable"
    ],
    "UOM": ["Nos", "Nos", "Nos", "Set", "Meters"],
    "Qty": [qty_smoke, qty_mcp, qty_sounder, 1, qty_cable]
}

# DataFrame (Table) banana
df = pd.DataFrame(mto_data)

# Table ko screen par dikhana
st.subheader(f"📋 Material Take-Off (MTO) for {b_type} Area")
st.table(df) # Ye bilkul saaf table dikhayega

# Excel/CSV Download Logic
csv_file = df.to_csv(index=False).encode('utf-8')

st.download_button(
    label="📥 Download MTO as Excel (CSV)",
    data=csv_file,
    file_name=f'Fire_Alarm_MTO_{area}sqm.csv',
    mime='text/csv',
)

st.info("Note: Qty calculations are estimates based on standard coverage rules.")
