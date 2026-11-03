import streamlit as st
from PIL import Image
import os

# Page Configuration
st.set_page_config(
    page_title="Mindanao Ave QC - Prime Commercial Lot", 
    page_icon="🏢", 
    layout="wide"
)

# Button to return to the catalog
st.page_link("home.py", label="⬅️ Back to All Listings", icon="🏠")

st.title("🏢 FOR SALE / FOR LEASE: Prime Commercial Lot in Mindanao Ave")
st.subheader("742 Mindanao Ave, Tandang Sora, Quezon City (Northbound)")

# Helper function to load images as Portrait orientation if needed
def load_as_portrait(image_path):
    img = Image.open(image_path)
    if img.width > img.height:
        img = img.rotate(270, expand=True)
    return img

# --- HERO BANNER / MAIN FACADE PHOTO ---
if os.path.exists("mindanao_facade.jpg"):
    st.image(load_as_portrait("mindanao_facade.jpg"), caption="Frontage View - Mindanao Ave, QC", use_container_width=True)
elif os.path.exists("mindanao1.jpg"):
    st.image(load_as_portrait("mindanao1.jpg"), caption="Frontage View - Mindanao Ave, QC", use_container_width=True)

st.markdown("---")

# --- MAIN CONTENT SECTION ---
col1, col2 = st.columns([1, 1])

with col1:
    st.header("📸 Photo Gallery & Site Photos")
    
    # AUTOMATIC PHOTO LOOPER: Scans for mindanao1.jpg, mindanao2.jpg, mindanao3.jpg...
    found_any_photo = False
    i = 1
    while True:
        photo_name = f"mindanao{i}.jpg"
        if os.path.exists(photo_name):
            portrait_img = load_as_portrait(photo_name)
            st.image(portrait_img, caption=f"Property Photo {i}", use_container_width=True)
            found_any_photo = True
            i += 1
        else:
            break
            
    if not found_any_photo:
        st.info("💡 Add photos named 'mindanao1.jpg', 'mindanao2.jpg', etc. in your root directory.")

with col2:
    st.header("✨ Property Highlights & Details")
    
    st.markdown("### 💰 **PRICING OPTIONS:**")
    st.markdown("* 🏷️ **For Sale:** **₱150,000 / sqm**")
    st.markdown("* 📝 **For Lease:** **₱400,000 / month** *(3 months advance + 6 months security deposit)*")
    
    st.markdown("---")
    st.markdown("### 📋 Property Specifications")
    st.markdown("""
    * ✅ **Lot Area:** 1,206 sqm
    * ✅ **Frontage:** 36 meters *(Wide, highly visible street presence)*
    * ✅ **Location Advantage:** Directly in front of the **upcoming Subway Tandang Sora Station** – prime positioning for high foot traffic and future growth.
    * 📍 **Nearby Landmarks:** Right beside Jollibee (right) & BJMP Office (left).
    """)

    st.markdown("### 💡 Ideal Development Uses")
    st.markdown("""
    * 🛒 **Retail & Commercial Centers**
    * 🍽️ **Dining & Drive-Thru Restaurants**
    * 🏢 **Office & Mixed-Use Developments**
    * 🚚 High-traffic corridor with excellent accessibility and unbeatable visibility.
    """)

st.markdown("---")

# --- INQUIRY FORM ---
st.header("📞 Inquire Now / Schedule a Site Visit")
st.write("For direct inquiries, proposals, or viewing, call or message: **09524656801**")

with st.form("inquiry_form_mindanao"):
    name = st.text_input("Full Name")
    phone = st.text_input("Phone Number / Email")
    inquiry_type = st.selectbox("Interested In:", ["For Sale", "For Lease", "General Inquiry"])
    message = st.text_area("Message or Preferred Inspection Date")
    submitted = st.form_submit_button("Submit Inquiry")
    
    if submitted:
        if name and phone:
            st.success(f"Thank you, {name}! We have received your inquiry regarding ({inquiry_type}) for the Mindanao Avenue Commercial Lot.")
        else:
            st.error("Please enter your full name and phone number.")
