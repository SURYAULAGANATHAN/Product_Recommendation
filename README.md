**📦 Product Recommender System**
A simple and efficient product recommendation system using FAISS for similarity search and Streamlit for an interactive UI. The model recommends products based on the user's historical preferences or interactions.

**🚀 Features**
🔍 User ID-based Product Recommendations
⚡ Fast vector search using FAISS
🧠 TF-IDF vectorization on review and product metadata
🌙 Dark theme UI built with Streamlit
🎯 Top 5 product recommendations based on similarity

**🗂️ Project Structure**
bash
Edit
├── vectorizer.pkl              # Saved TF-IDF vectorizer
├── faiss_index.idx             # FAISS index of product vectors
├── course_corpus.pkl           # Product data with user IDs
├── app.py                      # Streamlit app
├── README.md                   # This file

**💡 How It Works**
Each user-product interaction is converted into a TF-IDF vector.
These vectors are indexed using FAISS for fast nearest-neighbor search.
When a user ID is entered, the app checks for a match and retrieves the top 5 similar product entries.

**🧪 Prerequisites**
**Install the required Python packages:**
bash
pip install streamlit faiss-cpu scikit-learn numpy

**▶️ Running the App**
bash
streamlit run app.py
Open your browser and go to **http://localhost:8501** to view the app.
