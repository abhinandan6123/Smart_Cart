# 🛒 SmartCart – AI-Powered Shopping Assistant

Welcome to **SmartCart**, an AI-driven shopping assistant built using **Streamlit**. Designed to help customers navigate large retail stores like Walmart, it offers real-time product search, aisle mapping, and interactive FAQs — all in a beautifully designed UI.

---

## 🚀 Live Demo
🔗 Click here to try https://smart-cart-74fj.onrender.com

> 📌 *Replace the above URL with your actual Render live app link.*

---

## 📸 Project Preview

![SmartCart UI](https://cdn-icons-png.flaticon.com/512/2989/2989846.png)

---

## 🧠 Features

- 🔍 **Search Products** by name
- 📂 **Filter by Category** (e.g., Grocery, Fashion, Electronics)
- 🗺️ **Store Map** for aisle-based navigation
- 🎁 **Offers & Discounts** displayed for each product
- 🙋 **Interactive FAQ** section
- 🎨 **Professional UI** with custom CSS

---

## 🧰 Tech Stack

| Layer       | Tech Used             |
|-------------|------------------------|
| 🧠 Backend  | Python, Streamlit      |
| 🎨 Frontend | Streamlit UI, HTML/CSS |
| 🗃️ Assets   | Custom Map (JPG), Icons |
| 🌐 Hosting  | Render                 |

---

## 📂 File Structure

Smart_Cart/
│
├── app.py # Main Streamlit app
├── map-address.jpg # Store layout image
├── requirements.txt # Dependencies
└── README.md # Project documentation




---

## ⚙️ Installation & Local Run

```bash
git clone https://github.com/abhinandan6123/Smart_Cart.git
cd Smart_Cart
pip install -r requirements.txt
streamlit run app.py




Deployment (on Render)
Push your code to GitHub

Create a new Web Service on Render

Select Python + Streamlit template

Set start command to:
streamlit run app.py --server.enableCORS false

Upload map-address.jpg and test the app live!

👤 Author
Team Sparsh Creators (Tejshwini & Abhi)

💡 Future Plans
Add chatbot for in-app support

Integrate live product APIs (e.g., Walmart, Amazon)

Replace static map with an interactive one

User login system for personalized shopping
