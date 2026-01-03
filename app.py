import streamlit as st
import pandas as pd

st.title("Fire Alarm Designer")

# Input
area = st.number_input("Area (sqm):", value=100)

# Calculations
detectors = max(1, round(area / 60))
mcp = max(1, round(area / 150))

# Table Data
data = {
    "Sr #": [1, 2],
    "Item description": ["Smoke Detector", "Manual Call Point"],
    "UOM": ["Nos", "Nos"],
    "Qty": [detectors, mcp]
}

# Display Table
df = pd.DataFrame(data)
st.subheader("Material Take-Off")
st.table(df) # Ye line table dikhayegi

# Excel Download
csv = df.to_csv(index=False).encode('utf-8')
st.download_button(
    label="Download Excel (CSV)",
    data=csv,
    file_name='mto.csv',
    mime='text/csv',
)
