# 🎬 Movie Recommendation System

A **content-based Movie Recommendation System** built using **Python, Machine Learning, and Streamlit**.  
The application recommends movies similar to the one selected by the user by analyzing movie metadata and computing similarity using **cosine similarity**.

---

## 📖 Project Overview
Movie recommendation systems help users discover relevant content based on similarity. The system provides an interactive interface where users can select a movie and instantly receive similar movie suggestions along with posters.  
In this project, the **raw TMDB movie dataset was cleaned, processed, and transformed** before building the recommendation model.  
Important features such as genres, keywords, cast, and overview were extracted and combined to create meaningful movie representations.

---

## ✨ Features
- 🔍 Search and select a movie
- 🎥 Get top recommended movies based on similarity
- 🖼️ Fetches movie posters using TMDB API
- ⚡ Interactive and user-friendly Streamlit interface
- 🧠 Content-based recommendation using cosine similarity

---

## 🛠️ Tech Stack
- **Programming Language:** Python  
- **Framework:** Streamlit  
- **Libraries:** Pandas, NumPy, Scikit-learn  
- **ML Technique:** Content-Based Filtering  
- **API:** TMDB API  
- **Model Storage:** Pickle  

---
## 🧠 How It Works
1. Movie metadata is combined into a single feature set.
2. Text data is vectorized using **CountVectorizer**.
3. **Cosine similarity** is calculated to measure similarity between movies.
4. Based on the selected movie, the system recommends the most similar movies.

---
## 📂 Project Structure
Movie-Recommendation-System/
│
├── app.py
├── movies.pkl
├── similarity.pkl
├── requirements.txt
└── README.md
---

## ⚙️ Installation and Setup

```bash
git clone https://github.com/your-username/your-repository-name.git
cd your-repository-name
pip install -r requirements.txt
streamlit run app.py
```

---

## 🔑 Environment Variables

This project uses the TMDB API to fetch movie posters.

Create a `.env` file and add:
```env
TMDB_API_KEY=your_tmdb_api_key_here
```

---

## 👩‍💻 Author

Sharvari Chambhare  
Final Year Computer Engineering Student  
Interests: Data Science, Machine Learning, and Analytics

