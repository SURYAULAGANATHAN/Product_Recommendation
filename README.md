## 📦 Product Recommender System

A simple and efficient product recommendation system using **FAISS** for similarity search and **Streamlit** for an interactive UI. The model recommends products based on the user's historical preferences or interactions.

---

## 🚀 Features

- 🔍 User ID-based Product Recommendations  
- ⚡ Fast vector search using FAISS  
- 🧠 TF-IDF vectorization on review and product metadata  
- 🌙 Dark theme UI built with Streamlit  
- 🎯 Top 5 product recommendations based on similarity  

---

## 🗂️ Project Structure

ecommerce-product-recommendation/
├── app.py
├── data_processing.py
├── recommendation_utils.py
├── requirements.txt
├── .env
└── README.md

---

## 💡 How It Works

1. Each user-product interaction is converted into a TF-IDF vector.  
2. These vectors are indexed using FAISS for fast nearest-neighbor search.  
3. When a user ID is entered, the app checks for a match and retrieves the top 5 similar product entries.

---

### 🧪 Installation and Running the App
To get started, install the required dependencies and launch the Streamlit app:
```bash
pip install streamlit faiss-cpu scikit-learn numpy
streamlit run app.py





 


