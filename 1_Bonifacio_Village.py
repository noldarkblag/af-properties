import streamlit as st
import os

# Page Configuration
st.set_page_config(
    page_title="Bonifacio Village QC - House for Sale", 
    page_icon="🏠", 
    layout="wide"
)

# Button to return to the catalog
st.page_link("home.py", label="⬅️ Back to All Listings", icon="🏠")

st.title("🏠 2-Storey Corner Lot Home for Sale")
st.subheader("Bonifacio Village, Quezon City | High-Elevation & 100% Flood-Free")

# --- HERO BANNER / FACADE PHOTO ---
if os.path.exists("facade.jpg"):
    st.image("facade.jpg", caption="Facade & Frontage - Bonifacio Village, QC", use_container_width=True)

st.markdown("---")

# --- MAIN CONTENT SECTION ---
col1, col2 = st.columns([1, 1])

with col1:
    st.header("📸 Photo Gallery")
    
    if os.path.exists("living_room.jpg"):
        st.image("living_room.jpg", caption="Spacious Living Room", use_container_width=True)
        
    if os.path.exists("patio.jpg"):
        st.image("patio.jpg", caption="Relaxing Downstairs Patio", use_container_width=True)
        
    if os.path.exists("library.jpg"):
        st.image("library.jpg", caption="Family Area with Mini Library", use_container_width=True)

with col2:
    st.header("✨ Property Overview")
    st.markdown("### 💰 **Asking Price:** ₱25,000,000")
    st.markdown("📍 **Location:** Bonifacio Village, Brgy. Pasong Tamo, Quezon City *(Access Road via Mira Nila along Congressional)*")
    
    st.markdown("---")
    st.markdown("### 📋 Property Features")
    st.markdown("""
    * ✅ **Lot Area:** 126 sqm
    * ✅ **Floor Area:** 200 sqm
    * ✅ **Layout:** 2-Storey Corner Lot
    * ✅ **Bedrooms:** 4 Bedrooms
    * ✅ **Bathrooms:** 3 Full Bathrooms + 1 Downstairs Powder Room
    * ✅ **Parking:** 2-Car Garage inside + space for 3 cars in front
    * ✅ **Highlights:** Solid Wood Flooring upstairs, Family Area w/ mini library, Balcony, & Dirty Kitchen.
    * ✅ **Security & Amenities:** 24/7 Gated Security, Clubhouse, Basketball Court, & Children's Playground.
    """)

    st.markdown("### 📍 Prime Location & Accessibility")
    st.markdown("""
    * 🎓 **Schools (Around 10 mins):** UP Diliman, Ateneo de Manila University, Miriam College
    * 🛍️ **Malls (Around 15 mins):** SM North EDSA, TriNoma, Vertis North, Solaire North
    * 🏥 **Hospitals:** Philippine Heart Center & East Avenue Medical Center
    """)

st.markdown("---")

# --- INQUIRY FORM ---
st.header("📞 Schedule a Viewing / Inquire Now")
st.write("For direct inquiries, call or message: **09524656801**")
st.caption("📌 Serious buyers and real estate agents are welcome.")

with st.form("inquiry_form_bonifacio"):
    st.write("Or fill out the form below and we will get back to you:")
    name = st.text_input("Full Name")
    phone = st.text_input("Phone Number / Email")
    message = st.text_area("Message or Preferred Date of Viewing")
    submitted = st.form_submit_button("Submit Inquiry")
    
    if submitted:
        if name and phone:
            st.success(f"Thank you, {name}! We have received your inquiry. We will contact you at {phone} shortly.")
        else:
            st.error("Please enter your full name and phone number.")
