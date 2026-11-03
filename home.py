import streamlit as st
import os

# Page Configuration
st.set_page_config(
    page_title="Fernandez Properties For Sale", 
    page_icon="🏠", 
    layout="wide"
)

# --- HEADER SECTION WITH LOGO ---
col_logo, col_title = st.columns([1, 4])

with col_logo:
    if os.path.exists("logo.png"):
        st.image("logo.png", width=140)

with col_title:
    st.title("Fernandez Properties For Sale")
    st.subheader("Featured Properties & Real Estate Listings")

st.markdown("---")

st.write("Select a property below to view complete details, specifications, and photo galleries:")
st.write("")

# --- PROPERTY 1: BONIFACIO VILLAGE ---
col1, col2 = st.columns([1, 2])

with col1:
    if os.path.exists("facade.jpg"):
        st.image("facade.jpg", use_container_width=True)

with col2:
    st.subheader("🏠 2-Storey Home in Bonifacio Village, QC")
    st.write("💰 **Price:** ₱25,000,000")
    st.write("📍 **Location:** Bonifacio Village, Brgy. Pasong Tamo, Quezon City")
    st.write("🛏️ 4 Bedrooms | 🛁 3 Baths | 📐 LA: 126 sqm | FA: 200 sqm")
    
    # Safe Streamlit Page Navigation Link
    st.page_link("pages/1_Bonifacio_Village.py", label="👉 View Full Details & Photos", icon="🔍")

st.markdown("---")

# --- PROPERTY 2: MINDANAO AVENUE COMMERCIAL LOT ---
col3, col4 = st.columns([1, 2])

with col3:
    if os.path.exists("mindanao1.jpg"):
        st.image("mindanao1.jpg", use_container_width=True)
    elif os.path.exists("mindanao_facade.jpg"):
        st.image("mindanao_facade.jpg", use_container_width=True)

with col4:
    st.subheader("🏢 Prime Commercial Lot in Mindanao Ave, QC")
    st.write("💰 **For Sale:** ₱150,000 / sqm | **For Lease:** ₱400,000 / month")
    st.write("📍 **Location:** 742 Mindanao Ave, Tandang Sora, Quezon City (In front of Subway Station)")
    st.write("📐 **Lot Area:** 1,206 sqm | **Frontage:** 36 meters")
    
    # Safe Streamlit Page Navigation Link
    st.page_link("pages/2_Mindanao_Avenue.py", label="👉 View Full Details & Photos", icon="🔍")
