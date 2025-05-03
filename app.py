import streamlit as st
import pickle
import faiss
import numpy as np

# Load vectorizer
with open("vectorizer.pkl", "rb") as f:
    vectorizer = pickle.load(f)

# Load FAISS index
index = faiss.read_index("faiss_index.idx")

# Load your original course corpus (must match index order)
# Ideally this is saved as a pickle or CSV when building the index
with open("course_corpus.pkl", "rb") as f:
    course_corpus = pickle.load(f)  # list of course titles/descriptions

st.set_page_config(page_title="Product Recommender", layout="centered")

st.title("🛒 Product Recommender")

search_input = st.text_input("🔍 Enter a user id to get product recommendations")

if search_input:
    try:
        # Vectorize and search
        query_vec = vectorizer.transform([search_input])
        query_vec_array = np.float32(query_vec.toarray())
        distances, indices = index.search(query_vec_array, 5)

        st.subheader("🎯 Top recommended products")
        for i, idx in enumerate(indices[0]):
            st.write(f"{i+1}. {course_corpus[idx]}")

    except Exception as e:
        st.error(f"An error occurred: {e}")
