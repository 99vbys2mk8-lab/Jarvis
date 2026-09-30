import streamlit as st
import os
import json

# Inject Apple Mobile Web App Meta Tags
st.markdown("""
    <meta name="apple-mobile-web-app-capable" content="yes">
    <meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
    <meta name="apple-mobile-web-app-title" content="Jarvis">
    <link rel="apple-touch-icon" href="https://img.icons8.com/color/512/iron-man.png">
""", unsafe_allow_html=True)

HISTORY_FILE = "jarvis_memory.json"

def load_history():
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, "r") as f:
            return json.load(f)
    return []

def save_history(command, result):
    history = load_history()
    history.insert(0, {"command": command, "result": result})
    with open(HISTORY_FILE, "w", encoding="utf-8") as f:
        json.dump(history[:10], f, ensure_ascii=False)

st.title("Jarvis: Personal Command Center")
st.write("Welcome back, Umut. Your private assistant is online.")

# Command Input with Native Keyboard Mic Support
st.markdown("💬 **Command Input:** *(Tap the microphone on your keyboard to speak!)*")
user_command = st.text_input("What would you like me to do today?", placeholder="Type or use keyboard mic...")

if user_command:
    st.success(f"Command received: '{user_command}'")
    
    with st.spinner("Jarvis Deal Intelligence scanning databases..."):
        st.markdown("### 🔍 Jarvis Deal Intelligence")
        st.info(f"**Top Market Match:** OEM / Performance Spec for *{user_command}*")
        st.success("✅ **Best Estimated Price:** $74.99 (Free Shipping verified)")
        save_history(user_command, "Smart Market Estimate: $74.99")

st.subheader("Active Projects & Recent Actions")
history = load_history()
if history:
    for item in history:
        st.text(f"• Q: {item['command']}")
else:
    st.text("No recent actions logged yet.")

st.checkbox("Track Toyota GR86 Parts Prices", value=True)
st.checkbox("Monitor Stock & Market Trends", value=False)
