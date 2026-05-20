import streamlit as st
import random

st.set_page_config(page_title="Rock Paper Scissors", layout="centered")
st.title("🎮 Rock Paper Scissors Game")

# Initialize session state
if 'player_score' not in st.session_state:
    st.session_state.player_score = 0
    st.session_state.computer_score = 0
    st.session_state.ties = 0

col1, col2, col3 = st.columns(3)

with col1:
    if st.button("🪨 Rock", use_container_width=True):
        player_choice = "rock"
        computer_choice = random.choice(['rock', 'paper', 'scissors'])

        if player_choice == computer_choice:
            result = "🤝 TIE!"
            st.session_state.ties += 1
        elif (player_choice == 'rock' and computer_choice == 'scissors') or \
             (player_choice == 'paper' and computer_choice == 'rock') or \
             (player_choice == 'scissors' and computer_choice == 'paper'):
            result = "🎉 YOU WIN!"
            st.session_state.player_score += 1
        else:
            result = "🤖 COMPUTER WINS!"
            st.session_state.computer_score += 1

        st.success(
            f"You: {player_choice.upper()} | Computer: {computer_choice.upper()}\n{result}")

with col2:
    if st.button("📄 Paper", use_container_width=True):
        player_choice = "paper"
        computer_choice = random.choice(['rock', 'paper', 'scissors'])

        if player_choice == computer_choice:
            result = "🤝 TIE!"
            st.session_state.ties += 1
        elif (player_choice == 'rock' and computer_choice == 'scissors') or \
             (player_choice == 'paper' and computer_choice == 'rock') or \
             (player_choice == 'scissors' and computer_choice == 'paper'):
            result = "🎉 YOU WIN!"
            st.session_state.player_score += 1
        else:
            result = "🤖 COMPUTER WINS!"
            st.session_state.computer_score += 1

        st.success(
            f"You: {player_choice.upper()} | Computer: {computer_choice.upper()}\n{result}")

with col3:
    if st.button("✂️ Scissors", use_container_width=True):
        player_choice = "scissors"
        computer_choice = random.choice(['rock', 'paper', 'scissors'])

        if player_choice == computer_choice:
            result = "🤝 TIE!"
            st.session_state.ties += 1
        elif (player_choice == 'rock' and computer_choice == 'scissors') or \
             (player_choice == 'paper' and computer_choice == 'rock') or \
             (player_choice == 'scissors' and computer_choice == 'paper'):
            result = "🎉 YOU WIN!"
            st.session_state.player_score += 1
        else:
            result = "🤖 COMPUTER WINS!"
            st.session_state.computer_score += 1

        st.success(
            f"You: {player_choice.upper()} | Computer: {computer_choice.upper()}\n{result}")

st.divider()
st.metric("Your Score", st.session_state.player_score)
st.metric("Computer Score", st.session_state.computer_score)
st.metric("Ties", st.session_state.ties)

if st.button("🔄 Reset Scores"):
    st.session_state.player_score = 0
    st.session_state.computer_score = 0
    st.session_state.ties = 0
    st.rerun()
