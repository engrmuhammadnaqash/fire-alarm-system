import streamlit as st
import pandas as pd

# App ka Title
st.set_page_config(page_title="Fire Alarm MTO Generator", layout="centered")
st.title("🔥 Fire Alarm System Designer & MTO")
st.write("Area input karein aur Material Take-Off (MTO) Excel mein download karein.")

# User Input
area = st.number_input("Area size (Square Meters):", min_value=1, value=100)
b_type = st.selectbox("Building Type:", ["Office", "Warehouse", "Residential", "Industrial"])

# Calculation Logic
detectors = max(1, round(area / 60))
mcps = max(1, round(area / 150))
sounders = max(1, round(detectors / 4))
panel = "1 Zone Panel" if detectors < 15 else "Addressable Panel (2 Loop)"

# Table (MTO) ka Data taiyar karna
mto_data = {
    "Sr. No": [1, 2, 3, 4, 5],
    "Item Description": [
        "Smoke/Heat Detectors", 
        "Manual Call Points (MCP)", 
        "Fire Alarm Sounders/Hooters", 
        "Fire Alarm Control Panel",
        "Fire Cable (Approx Meters)"
    ],
    "Quantity": [detectors, mcps, sounders, 1, area * 2.5],
    "Unit": ["Nos", "Nos", "Nos", "Set", "Meters"]
}

# DataFrame banana (Table ke liye)
df = pd.DataFrame(mto_data)

# Table Display karna
st.subheader(f"📊 Material Take-Off for {b_type} ({area} sqm)")
st.table(df)

# Excel/CSV Download function
@st.cache_data
def convert_df(df):
    return df.to_csv(index=False).encode('utf-8')

csv_file = convert_df(df)

# Download Button
st.download_button(
    label="📥 Download MTO as Excel (CSV)",
    data=csv_file,
    file_name=f'Fire_Alarm_MTO_{area}sqm.csv',
    mime='text/csv',
)

st.success("Aap niche diye gaye button se MTO download kar sakte hain.")
