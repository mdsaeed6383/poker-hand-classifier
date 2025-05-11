import streamlit as st
import pandas as pd
from pycaret.classification import load_model, predict_model

# Load your trained model
model = load_model('poker-hand-classifier')

st.title("🃏 Poker Hand Classifier")
st.markdown("Select **exactly 5 cards** from the grid below to predict the poker hand.")

# Suit mapping
suits = {1: "♥ Hearts", 2: "♠ Spades", 3: "♦ Diamonds", 4: "♣ Clubs"}
suit_emojis = {1: "♥", 2: "♠", 3: "♦", 4: "♣"}

# Track selected cards
selected_cards = []

# Show 4 rows (suits) × 13 columns (card values)
for suit_val in range(1, 5):  # 1 to 4
    st.markdown(f"### {suits[suit_val]}")
    cols = st.columns(13)
    for i in range(13):
        card_val = i + 1
        label = f"{card_val} {suit_emojis[suit_val]}"
        key = f"{suit_val}_{card_val}"
        if cols[i].checkbox(label, key=key):
            selected_cards.append((suit_val, card_val))

# Validate selection
if len(selected_cards) > 5:
    st.error("❌ Please select only 5 cards.")
elif len(selected_cards) < 5:
    st.info("🃏 Select 5 cards to get started.")
else:
    # Build input DataFrame for model
    input_data = {}
    for i, (suit, val) in enumerate(selected_cards):
        input_data[f"S{i+1}"] = suit
        input_data[f"C{i+1}"] = val
    input_df = pd.DataFrame([input_data])

    # Make prediction
    result = predict_model(model, data=input_df)
    class_id = int(result['prediction_label'][0])
    hand_types = [
        "Nothing in hand", "One pair", "Two pairs", "Three of a kind",
        "Straight", "Flush", "Full house", "Four of a kind", "Straight flush", "Royal flush"
    ]
    st.success(f"🧠 Predicted Hand: **{hand_types[class_id]}**")

