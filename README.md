# 🤖 Data Retrieval Chatbot

A production-ready, Streamlit-powered conversational AI chatbot that enables fast, accurate data retrieval using NLP and machine learning techniques. Designed with scalability, testing rigor, and deployment readiness in mind.

**Accuracy:** 92% across 50+ natural language query variations  
**Response Time:** < 200ms  
**Status:** Deployed & production-tested

---

## 🌐 Live Demo
**Website:** (https://dataretriever.streamlit.app/)

---

## 🔍 Project Overview
This chatbot allows users to retrieve structured business data (sales, customers, inventory) using natural language queries. It leverages TF-IDF vectorization and intent matching to translate user input into accurate data responses.

The project emphasizes:
- Clean architecture and modular design  
- Strong test coverage  
- Real-world deployment via Streamlit Cloud  

---

## 🛠️ Tech Stack
**Frontend**
- Streamlit (interactive web UI)

**Backend / ML**
- Python 3.11+
- NLTK (tokenization, lemmatization)
- Scikit-learn (TF-IDF vectorization, similarity scoring)

**Tooling**
- Pytest (automated testing)
- Git & GitHub (version control)
- Streamlit Cloud (deployment)

---

## ⚙️ Installation & Local Setup
```bash
pip install -r requirements.txt
python -c "import nltk; nltk.download('punkt'); nltk.download('wordnet'); nltk.download('omw-1.4'); nltk.download('punkt_tab')"
```

Run locally:
```bash
streamlit run streamlit_app.py
```

Or via batch script:
```bash
.\RUN_CHATBOT.bat
```

---

## ✅ Testing & Quality Assurance
Run the full test suite:
```bash
pytest test_chatbot_advanced.py -v
```

**17 automated tests covering:**
- Accuracy validation across 50+ query variations
- Edge cases (empty input, unknown commands, special characters)
- Performance benchmarks (sub-200ms response time)
- Data integrity checks

✔️ 100% test pass rate

---

## 🚀 Deployment (Streamlit Cloud)
1. Push code to GitHub:
```bash
git add .
git commit -m "Deploy chatbot to Streamlit"
git push origin main
```

2. Visit https://share.streamlit.io  
   - Sign in with GitHub  
   - Click **Deploy an app**  
   - Select repository  
   - Main file: `streamlit_app.py`  

3. Click **Deploy**  
   - Live in ~2–3 minutes  
   - App URL auto-generated  

**Notes**
- Free tier sleeps after 7 days of inactivity  
- App automatically wakes on visit  
- Code is never deleted  

---

## 💡 Example Queries
- `show sales` → Revenue data  
- `customer count` → Customer analytics  
- `inventory` → Stock levels  
- `commands` → List of supported queries  

---

## 📌 Why This Project Matters
This project demonstrates:
- Applied NLP for real-world query understanding  
- Clean ML pipelines without overengineering  
- Production deployment experience  
- Testing discipline expected in industry environments  

---

## 📧 Contact
**Parth Patel**  
📩 parth.pat015@gmail.com  

---

**Built by Parth Patel**

