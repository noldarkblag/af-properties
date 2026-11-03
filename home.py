import streamlit as st
import streamlit.components.v1 as components
from PIL import Image
import os

# Page Configuration
st.set_page_config(
    page_title="Properties For Sale", 
    page_icon="🏠", 
    layout="wide"
)

# Initialize navigation state
if 'current_page' not in st.session_state:
    st.session_state.current_page = 'home'

def go_to(page_name):
    st.session_state.current_page = page_name

# Helper function for image rotation
def load_as_portrait(image_path):
    img = Image.open(image_path)
    if img.width > img.height:
        img = img.rotate(270, expand=True)
    return img

# ==========================================
# 🏠 HOME PAGE / CATALOG
# ==========================================
if st.session_state.current_page == 'home':
    # --- HEADER WITH LOGO ---
    col_logo, col_title = st.columns([1, 4])
    with col_logo:
        if os.path.exists("logo.png"):
            st.image("logo.png", width=140)
    with col_title:
        st.title("Properties For Sale")
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
        st.button("👉 View Full Details & Photos", key="btn_bonifacio", on_click=go_to, args=('bonifacio',))

    st.markdown("---")

    # --- PROPERTY 2: MINDANAO AVENUE ---
    col3, col4 = st.columns([1, 2])
    with col3:
        if os.path.exists("mindanao1.jpg"):
            st.image(load_as_portrait("mindanao1.jpg"), use_container_width=True)
        elif os.path.exists("mindanao_facade.jpg"):
            st.image(load_as_portrait("mindanao_facade.jpg"), use_container_width=True)
    with col4:
        st.subheader("🏢 Prime Commercial Lot in Mindanao Ave, QC")
        st.write("💰 **For Sale:** ₱150,000 / sqm | **For Lease:** ₱400,000 / month")
        st.write("📍 **Location:** 742 Mindanao Ave, Tandang Sora, Quezon City (In front of Subway Station)")
        st.write("📐 **Lot Area:** 1,206 sqm | **Frontage:** 36 meters")
        st.button("👉 View Full Details & Photos", key="btn_mindanao", on_click=go_to, args=('mindanao',))

    st.markdown("---")

    # --- PROPERTY 3: ANTIPOLO PROPERTY ---
    col5, col6 = st.columns([1, 2])
    with col5:
        if os.path.exists("antipolo1.jpg"):
            st.image("antipolo1.jpg", use_container_width=True)
    with col6:
        st.subheader("🏡 Property for Sale in Antipolo")
        st.write("💰 **Price:** Inquire for Price")
        st.write("📍 **Location:** Antipolo, Rizal")
        st.write("🛏️ Bedrooms | 🛁 Bathrooms | 📐 LA: --- sqm | FA: --- sqm")
        st.button("👉 View Full Details & Photos", key="btn_antipolo", on_click=go_to, args=('antipolo',))


# ==========================================
# 📍 PROPERTY 1: BONIFACIO VILLAGE DETAILS
# ==========================================
elif st.session_state.current_page == 'bonifacio':
    st.button("⬅️ Back to All Listings", on_click=go_to, args=('home',))
    
    st.title("🏠 2-Storey Corner Lot Home for Sale")
    st.subheader("Bonifacio Village, Quezon City | High-Elevation & 100% Flood-Free")

    if os.path.exists("facade.jpg"):
        st.image("facade.jpg", caption="Facade & Frontage - Bonifacio Village, QC", use_container_width=True)

    st.markdown("---")
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
        * ✅ **Lot Area:** 126 sqm | **Floor Area:** 200 sqm
        * ✅ **Layout:** 2-Storey Corner Lot
        * ✅ **Bedrooms:** 4 Bedrooms | **Bathrooms:** 3 Full Baths + 1 Powder Room
        * ✅ **Parking:** 2-Car Garage inside + 3 cars parking space in front
        * ✅ **Highlights:** Solid Wood Flooring upstairs, Family Area w/ mini library, Balcony, & Dirty Kitchen.
        * ✅ **Security & Amenities:** 24/7 Gated Security, Clubhouse, Basketball Court, & Children's Playground.
        """)

        st.markdown("### 📍 Prime Location & Accessibility")
        st.markdown("""
        * 🎓 **Schools (10 mins):** UP Diliman, Ateneo de Manila, Miriam College
        * 🛍️ **Malls (15 mins):** SM North EDSA, TriNoma, Vertis North, Solaire North
        * 🏥 **Hospitals:** Philippine Heart Center & East Avenue Medical Center
        """)

    st.markdown("---")
    st.header("📞 Schedule a Viewing / Inquire Now")
    st.write("For direct inquiries, call or message: **09524656801**")

    form_bonifacio = """
    <form action="https://formsubmit.co/YOUR_EMAIL@gmail.com" method="POST" style="font-family: sans-serif;">
        <input type="hidden" name="_subject" value="New Inquiry: Bonifacio Village House">
        <input type="hidden" name="_captcha" value="false">
        <div style="margin-bottom: 12px;">
            <label style="font-weight: bold; display: block; margin-bottom: 5px;">Full Name</label>
            <input type="text" name="name" required style="width: 100%; padding: 8px; border: 1px solid #ccc; border-radius: 4px;">
        </div>
        <div style="margin-bottom: 12px;">
            <label style="font-weight: bold; display: block; margin-bottom: 5px;">Phone Number / Email</label>
            <input type="text" name="contact" required style="width: 100%; padding: 8px; border: 1px solid #ccc; border-radius: 4px;">
        </div>
        <div style="margin-bottom: 12px;">
            <label style="font-weight: bold; display: block; margin-bottom: 5px;">Message or Preferred Date of Viewing</label>
            <textarea name="message" rows="4" required style="width: 100%; padding: 8px; border: 1px solid #ccc; border-radius: 4px;"></textarea>
        </div>
        <button type="submit" style="background-color: #ff4b4b; color: white; border: none; padding: 10px 20px; border-radius: 4px; cursor: pointer; font-weight: bold;">Submit Inquiry</button>
    </form>
    """
    components.html(form_bonifacio, height=360)


# ==========================================
# 🏢 PROPERTY 2: MINDANAO AVENUE DETAILS
# ==========================================
elif st.session_state.current_page == 'mindanao':
    st.button("⬅️ Back to All Listings", on_click=go_to, args=('home',))
    
    st.title("🏢 FOR SALE / FOR LEASE: Prime Commercial Lot in Mindanao Ave")
    st.subheader("742 Mindanao Ave, Tandang Sora, Quezon City (Northbound)")

    if os.path.exists("mindanao1.jpg"):
        st.image(load_as_portrait("mindanao1.jpg"), caption="Frontage View - Mindanao Ave, QC", use_container_width=True)

    st.markdown("---")
    col1, col2 = st.columns([1, 1])

    with col1:
        st.header("📸 Photo Gallery & Site Photos")
        i = 1
        found_any = False
        while True:
            photo_name = f"mindanao{i}.jpg"
            if os.path.exists(photo_name):
                st.image(load_as_portrait(photo_name), caption=f"Property Photo {i}", use_container_width=True)
                found_any = True
                i += 1
            else:
                break
        if not found_any:
            st.info("💡 Add photos named 'mindanao1.jpg', 'mindanao2.jpg', etc. in GitHub.")

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
        * 🛒 Retail & Commercial Centers
        * 🍽️ Dining & Drive-Thru Restaurants
        * 🏢 Office & Mixed-Use Developments
        """)

    st.markdown("---")
    st.header("📞 Inquire Now / Schedule a Site Visit")
    st.write("For direct inquiries, proposals, or viewing, call or message: **09524656801**")

    form_mindanao = """
    <form action="https://formsubmit.co/YOUR_EMAIL@gmail.com" method="POST" style="font-family: sans-serif;">
        <input type="hidden" name="_subject" value="New Inquiry: Mindanao Ave Commercial Lot">
        <input type="hidden" name="_captcha" value="false">
        <div style="margin-bottom: 12px;">
            <label style="font-weight: bold; display: block; margin-bottom: 5px;">Full Name</label>
            <input type="text" name="name" required style="width: 100%; padding: 8px; border: 1px solid #ccc; border-radius: 4px;">
        </div>
        <div style="margin-bottom: 12px;">
            <label style="font-weight: bold; display: block; margin-bottom: 5px;">Phone Number / Email</label>
            <input type="text" name="contact" required style="width: 100%; padding: 8px; border: 1px solid #ccc; border-radius: 4px;">
        </div>
        <div style="margin-bottom: 12px;">
            <label style="font-weight: bold; display: block; margin-bottom: 5px;">Message or Preferred Inspection Date</label>
            <textarea name="message" rows="4" required style="width: 100%; padding: 8px; border: 1px solid #ccc; border-radius: 4px;"></textarea>
        </div>
        <button type="submit" style="background-color: #ff4b4b; color: white; border: none; padding: 10px 20px; border-radius: 4px; cursor: pointer; font-weight: bold;">Submit Inquiry</button>
    </form>
    """
    components.html(form_mindanao, height=360)


# ==========================================
# 🌄 PROPERTY 3: ANTIPOLO DETAILS
# ==========================================
elif st.session_state.current_page == 'antipolo':
    st.button("⬅️ Back to All Listings", on_click=go_to, args=('home',))
    
    st.title("🏡 Property for Sale in Antipolo")
    st.subheader("Antipolo, Rizal | Relaxing & Cool Environment")

    if os.path.exists("antipolo1.jpg"):
        st.image("antipolo1.jpg", caption="Frontage View - Antipolo", use_container_width=True)

    st.markdown("---")
    col1, col2 = st.columns([1, 1])

    with col1:
        st.header("📸 Photo Gallery")
        i = 1
        found_any = False
        while True:
            photo_name = f"antipolo{i}.jpg"
            if os.path.exists(photo_name):
                st.image(photo_name, caption=f"Property Photo {i}", use_container_width=True)
                found_any = True
                i += 1
            else:
                break
        if not found_any:
            st.info("💡 Maglagay ng mga larawan tulad ng 'antipolo1.jpg', 'antipolo2.jpg', atbp. sa GitHub.")

    with col2:
        st.header("✨ Property Highlights & Details")
        st.markdown("### 💰 **Asking Price:** *(Lagyan ng Presyo)*")
        st.markdown("📍 **Location:** Antipolo, Rizal")
        st.markdown("---")
        st.markdown("### 📋 Property Features")
        st.markdown("""
        * ✅ **Lot Area:** --- sqm
        * ✅ **Floor Area:** --- sqm
        * ✅ **Bedrooms:** ---
        * ✅ **Bathrooms:** ---
        * ✅ **Highlights:** Nice view, quiet neighborhood, accessible to main roads.
        """)

    st.markdown("---")
    st.header("📞 Schedule a Viewing / Inquire Now")
    st.write("For direct inquiries, call or message: **09524656801**")

    form_antipolo = """
    <form action="https://formsubmit.co/arnolh.fernandez00@gmail.com" method="POST" style="font-family: sans-serif;">
        <input type="hidden" name="_subject" value="New Inquiry: Antipolo Property">
        <input type="hidden" name="_captcha" value="false">
        <div style="margin-bottom: 12px;">
            <label style="font-weight: bold; display: block; margin-bottom: 5px;">Full Name</label>
            <input type="text" name="name" required style="width: 100%; padding: 8px; border: 1px solid #ccc; border-radius: 4px;">
        </div>
        <div style="margin-bottom: 12px;">
            <label style="font-weight: bold; display: block; margin-bottom: 5px;">Phone Number / Email</label>
            <input type="text" name="contact" required style="width: 100%; padding: 8px; border: 1px solid #ccc; border-radius: 4px;">
        </div>
        <div style="margin-bottom: 12px;">
            <label style="font-weight: bold; display: block; margin-bottom: 5px;">Message or Preferred Date of Viewing</label>
            <textarea name="message" rows="4" required style="width: 100%; padding: 8px; border: 1px solid #ccc; border-radius: 4px;"></textarea>
        </div>
        <button type="submit" style="background-color: #ff4b4b; color: white; border: none; padding: 10px 20px; border-radius: 4px; cursor: pointer; font-weight: bold;">Submit Inquiry</button>
    </form>
    """
    components.html(form_antipolo, height=360)
