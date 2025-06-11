%%writefile app.py
import streamlit as st
from PIL import Image

# Set up page config
st.set_page_config(
    page_title="SmartCart by SPARSH CREATOR",
    layout="centered",
    page_icon="🛒"
)

# Add custom CSS for styling
st.markdown("""
    <style>
        body {
            background-color: #f5f7fa;
        }
        .main {
            background: linear-gradient(120deg, #e0f7fa, #ffffff);
            border-radius: 10px;
            padding: 20px;
        }
        .stApp {
            background: linear-gradient(145deg, #f0f4ff, #fefefe);
        }
        h1, h4 {
            color: #2c3e50;
        }
        .faq-box {
            padding: 10px;
            background-color: #ecf0f1;
            border-radius: 8px;
            margin-bottom: 8px;
        }
    </style>
""", unsafe_allow_html=True)

# Header
st.markdown("""
<div class="main" style="text-align:center;">
    <h1>🛒 <b>SmartCart</b></h1>
    <p style="font-size:18px; color:#34495e;">Your AI-powered Shopping Assistant by <b>SPARSH CREATOR</b></p>
    <img src="https://cdn-icons-png.flaticon.com/512/2989/2989846.png" width="100">
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# Sample product data
products = [
    {"name": "Colgate Toothpaste", "aisle": "Health & Beauty", "price": "$2.99", "offer": "10% off"},
    {"name": "Dove Shampoo", "aisle": "Hair Care", "price": "$5.49", "offer": "Buy 1 Get 1 Free"},
    {"name": "Pepsodent Toothbrush", "aisle": "Health & Beauty", "price": "$1.99", "offer": "None"},
    {"name": "Clinic Plus Conditioner", "aisle": "Hair Care", "price": "$3.99", "offer": "5% off"},
    {"name": "Milk Packet", "aisle": "Grocery", "price": "$1.49", "offer": "5% off"},
    {"name": "T-Shirt", "aisle": "Fashion", "price": "$9.99", "offer": "20% off"},
    {"name": "Bread Loaf", "aisle": "Bakery/Deli", "price": "$2.00", "offer": "None"},
    {"name": "Mobile Charger", "aisle": "Electronics", "price": "$15.00", "offer": "Flat $2 off"},
]

# Categories
categories = sorted(set(p["aisle"] for p in products))
categories.insert(0, "All")

# Search and filter
st.markdown("### 🧭 Search & Filter Your Product")
col1, col2 = st.columns([2, 1])
with col1:
    query = st.text_input("🔍 Search by product name")
with col2:
    selected_category = st.selectbox("📂 Choose Category", categories)

# Filtering logic
filtered = products
if selected_category != "All":
    filtered = [p for p in filtered if p['aisle'] == selected_category]
if query:
    filtered = [p for p in filtered if query.lower() in p['name'].lower()]

# Display filtered results
if filtered:
    for p in filtered:
        st.markdown(f"""
        <div class="main" style="border: 1px solid #dcdcdc; margin-bottom:10px; padding:10px; border-radius:10px;">
            <h4>🛍️ {p['name']}</h4>
            <p><b>📌 Aisle:</b> {p['aisle']} &nbsp;&nbsp; <b>💰 Price:</b> {p['price']} &nbsp;&nbsp; <b>🎁 Offer:</b> {p['offer']}</p>
        </div>
        """, unsafe_allow_html=True)
else:
    st.warning("🚫 No matching products found.")

st.markdown("---")

# Store Map Section
st.markdown("### 🗺️ Store Map – Navigate the Aisles")
st.info("📍 Use the map below to locate Grocery, Fashion, Electronics, etc.")
image = Image.open("map-address.jpg")
st.image(image, caption="🧭 Store Layout – Map Address", use_column_width=True)

st.markdown("---")

# FAQ Section
st.markdown("## 🙋 Frequently Asked Questions (FAQs)")
with st.expander("❓ Tap to view FAQs"):
    faq = st.radio("📘 Select a question:", [
        "Where can I find today's offers?",
        "How do I search for a product?",
        "Where is the Bakery/Deli located on the map?",
        "Can I explore the full store layout?",
        "Do I need an account to use SmartCart?",
        "What to do if a product is not listed?"
    ])

    if faq == "Where can I find today's offers?":
        st.success("🎉 Check each product card – offers are mentioned below product name.")

    elif faq == "How do I search for a product?":
        st.info("🔍 Use the search bar and filter dropdown at the top of this page.")

    elif faq == "Where is the Bakery/Deli located on the map?":
        st.warning("📍 It’s located on the bottom-right (green zone).")
        st.image("map-address.jpg", caption="Bakery/Deli Zone", use_column_width=True)

    elif faq == "Can I explore the full store layout?":
        st.image("map-address.jpg", caption="Complete SmartCart Store Map", use_column_width=True)

    elif faq == "Do I need an account to use SmartCart?":
        st.success("🙌 No login required. Just start browsing!")

    elif faq == "What to do if a product is not listed?":
        st.warning("📩 In future updates, a contact form will be available to suggest new items.")

# Footer
st.markdown("---")
st.markdown("<div style='text-align:center; color: gray;'>Made with ❤️ by <b>SPARSH CREATOR</b> | Powered by Streamlit</div>", unsafe_allow_html=True)
