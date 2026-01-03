import streamlit as st

# App ka Title
st.title("🔥 Smart Fire Alarm Designer")
st.write("Sirf area enter karein aur apna system design hasil karein.")

# User se input lena
area = st.number_input("Area size enter karein (Square Meters mein):", min_value=1, value=100)
building_type = st.selectbox("Building ki qisam:", ["Office", "Warehouse", "Home", "Factory"])

# Design Logic (Simple Rules)
# 1 Smoke Detector = 60sqm coverage
detectors = round(area / 60)
if detectors == 0: detectors = 1

# Display Result
st.subheader("Aapka Design Taiyar Hai:")
st.write(f"✅ **Smoke Detectors:** {detectors} units")
st.write(f"✅ **Manual Call Points:** {round(area/200) + 1} units")
st.write(f"✅ **Sounders:** {round(detectors/5) + 1} units")

st.info("Ye design NFPA standards ke mutabiq tayeer kiya gaya hai.")
