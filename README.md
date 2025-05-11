# poker-hand-classifier
Multiclass classifier app for predicting poker hand using pycaret and streamlit

# 🃏 Poker Hand Classifier

A Streamlit web application that predicts the **type of poker hand** from a 5-card input using a **multiclass classification model** trained with PyCaret.

---

## 🚀 Live Demo

👉 [Click here to try the app](https://your-streamlit-app-url.streamlit.app)

---

## 🎯 Objective

This project demonstrates an end-to-end machine learning pipeline for **classifying poker hands** based on 5 playing cards. Users select cards using an interactive grid layout that mimics a real deck, and the app instantly predicts the hand type (e.g., Full House, Two Pairs, Royal Flush, etc.).

---

## 🧠 Model Details

- **Type**: Multiclass Classification
- **Target Variable**: `CLASS` (0 to 9 representing poker hands)
- **Algorithm**: Auto-selected by PyCaret's `compare_models()`
- **Accuracy**: ~68% on test data
- **Frameworks**: PyCaret 3.3.2, Streamlit

---

## 🗂️ App Features

✅ 4×13 card selection grid (real-deck-style UI)  
✅ Suit-aware and duplicate-aware card selection  
✅ Predicts hand type based on ML, not poker rules  
✅ Friendly UI with instant feedback  
✅ Deployed live on Streamlit Cloud

---

## 🃏 Poker Hand Labels

| Class | Hand Type         |
|-------|-------------------|
| 0     | Nothing in hand   |
| 1     | One pair          |
| 2     | Two pairs         |
| 3     | Three of a kind   |
| 4     | Straight          |
| 5     | Flush             |
| 6     | Full house        |
| 7     | Four of a kind    |
| 8     | Straight flush    |
| 9     | Royal flush       |

---

## 🧰 Installation

```bash
# Clone the repo
git clone https://github.com/your-username/poker-hand-classifier
cd poker-hand-classifier

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py
