import streamlit as st
from PIL import Image

# --- Page Configuration ---
st.set_page_config(page_title="🚍 Mumbai Bus Delay Dashboard", layout="wide")

# --- Custom Styling ---
st.markdown("""
<style>

/* Gradient background for entire app */
.stApp {
    background: linear-gradient(to right, #f3f9ff, #ffffff);
    font-family: 'Segoe UI', sans-serif;
}

/* Stylish Title with Button-like Look */
h1 {
    font-size: 3rem;
    background-color:lightgreen;
    color: white;
    padding: 15px 25px;
    border-radius: 12px;
    text-align: center;
    box-shadow: 2px 4px 20px rgba(0,0,0,0.1);
    margin-bottom: 10px;
}

/* Subheading text */
h4, h3 {
    color: #003566;
    margin-top: 1rem;
}

/* Sidebar Styling */
[data-testid="stSidebar"] {
    background: linear-gradient(to bottom, #cce0ff, #e6f0ff);
    padding: 2rem 1rem;
    border-right: 2px solid #aac4e6;
}

[data-testid="stSidebar"] h1, .sidebar .css-1d391kg {
    color: #003566;
    font-weight: bold;
}

/* Sidebar radio buttons hover effect */
.css-1aumxhk, .css-16idsys {
    transition: all 0.2s ease-in-out;
}

.css-1aumxhk:hover {
    background-color: #f0f8ff;
    color: #003566;
}

/* Image Effects */
img {
    border-radius: 10px;
    box-shadow: 0px 8px 20px rgba(0, 0, 0, 0.1);
    transition: transform 0.2s ease-in-out;
}

img:hover {
    transform: scale(1.02);
}

/* Footer Styling */
footer {
    text-align: center;
    font-size: 0.9rem;
    color: #666;
    padding-top: 2rem;
}

/* Container Padding */
.block-container {
    padding: 2rem 3rem;
}
</style>
""", unsafe_allow_html=True)

# --- Sidebar ---
st.sidebar.image("Pictures/bus.jpg", width=90)
st.sidebar.markdown("""
<div style='font-size:1.5rem; font-weight:bold; color:#002B5B; text-align:center; padding-bottom:10px;'>
🚦Dashboard Menu
</div>
""", unsafe_allow_html=True)
view = st.sidebar.radio("🧭 Select a Chart", (
    "📍 Average Delay per Bus Stop",
    "📊 Delay Category Distribution",
    "🕒 Average Delay by Hour",
    "📈 Power BI Dashboard"
))


# --- Page Title ---
st.title("Mumbai Public Transport Delay Analysis")
st.write("#### ⏱️ Understand the real-world delay patterns of BEST buses in Mumbai using historical GPS data.")

# --- Chart Display Logic ---
if view == "📍 Average Delay per Bus Stop":
    st.header("📍 Average Delay per Bus Stop in Mumbai")
    image = Image.open("Pictures/Figure_1.png")
    st.image(image, caption='Delay per Bus Stop', use_column_width=True)

elif view == "📊 Delay Category Distribution":
    st.header("📊 Delay Category Distribution by Bus")
    image = Image.open("Pictures/Figure_2.png")
    st.image(image, caption='Delay Category Breakdown', use_column_width=True)

elif view == "🕒 Average Delay by Hour":
    st.header("🕒 Hour-wise Delay Trends")
    image = Image.open("Pictures/Figure_3.png")
    st.image(image, caption='Delays by Hour of Day', use_column_width=True)

elif view == "📈 Power BI Dashboard":
    st.header("📈 Power BI Dashboard Snapshot")
    st.markdown("Explore a high-level Power BI dashboard visualization of delay trends.")
    image = Image.open("Pictures/PowerBi_Dashboard.png")
    st.image(image, caption="Exported Power BI Dashboard", use_column_width=True)


# --- Footer ---
st.markdown("""---  
<center>🚀 Made by <strong>Sujal Tankaria</strong> | Powered by <a href="https://streamlit.io" target="_blank">Streamlit</a> 💡</center>
""", unsafe_allow_html=True)
