Python 3.13.4 (v3.13.4:8a526ec7cbe, Jun  3 2025, 21:14:54) [Clang 16.0.0 (clang-1600.0.26.6)] on darwin
Enter "help" below or click "Help" above for more information.
import streamlit as st
import numpy as np

st.title("🧠 SuperKick AI Range Predictor")
st.write("Predict the next multiplier **range** in MSport's SuperKick game using AI pattern detection (simulated).")

st.subheader("📥 Enter Last 10 SuperKick Multipliers")
user_input = st.text_input("Comma-separated multipliers (e.g. 2.1, 1.5, 2.8, ...)")

... def predict_range(multiplier_list):
...     # Simulated logic based on AI prediction behavior
...     avg = np.mean(multiplier_list)
... 
...     # Simulated probabilities based on average
...     if avg <= 1.5:
...         probs = [0.8, 0.15, 0.04, 0.01]
...     elif avg <= 2.9:
...         probs = [0.1, 0.75, 0.1, 0.05]
...     elif avg <= 5.0:
...         probs = [0.05, 0.2, 0.6, 0.15]
...     else:
...         probs = [0.01, 0.1, 0.2, 0.69]
... 
...     labels = ["low (1.0–1.5x)", "medium (1.6–2.9x)", "high (3.0–5.0x)", "very high (5.1x+)"]
...     predicted_class = np.argmax(probs)
...     return labels[predicted_class], probs
... 
... if user_input:
...     try:
...         values = [float(x.strip()) for x in user_input.split(",")]
...         if len(values) != 10:
...             st.error("❌ Please enter exactly 10 multipliers.")
...         else:
...             prediction, probs = predict_range(values)
...             st.success(f"🔮 Predicted Range: **{prediction}**")
...             st.write("📊 Probabilities:")
...             st.write({
...                 "Low (1.0–1.5x)": f"{probs[0]*100:.2f}%",
...                 "Medium (1.6–2.9x)": f"{probs[1]*100:.2f}%",
...                 "High (3.0–5.0x)": f"{probs[2]*100:.2f}%",
...                 "Very High (5.1x+)": f"{probs[3]*100:.2f}%"
...             })
...     except ValueError:
...         st.error("❌ Invalid input. Please enter numbers only, separated by commas.")
... 
