import streamlit as st
from PIL import Image

# Page Configuration
st.set_page_config(page_title="Project Overview", layout="centered")

# Title and Banner Image
st.title("🏫 Fr. Conceicao Rodrigues College of Engineering")
st.subheader("Mumbai Flat Price Prediction and Recommendation")

# Load and Display Image
image = Image.open("img.png")
st.image(image, width=600, caption="Project Overview")

# Project Guide Section
st.markdown("## 👨‍🏫 Project Guide")
st.info("Professor **Jayan Modi Sir**")

# Team Members Section
st.markdown("## 👥 Team Members")
teammates = {
    "Aman Gupta": "9752",
    "Aditya Gurav": "9753",
    "Abdullah": "9759"
}

for name, roll in teammates.items():
    st.write(f"- **{name}** (Roll No: {roll})")

# Project Dataset Information
st.markdown("## 📊 Dataset & Methodology")
st.write("This project is built on Mumbai's **7500 flats dataset**.")

st.markdown("### 🏡 Data Collection")
st.write("- Scraped data from **Housing.com** using **Selenium** and **BeautifulSoup**.")

st.markdown("### 🔍 Data Cleaning & Analysis")
st.write("- Processed data using **Pandas** and **NumPy**.")
st.write("- Conducted **Univariate, Bivariate, and Exploratory Data Analysis (EDA)** using **Matplotlib** and **Seaborn**.")

st.markdown("### 🏗️ Feature Engineering & Outlier Detection")
st.write("- Applied **Box plots, Histograms, and IQR method** for outlier detection.")
st.write("- Utilized **ANOVA tests and Tree algorithms** for feature selection.")

st.markdown("### 🤖 Machine Learning Model")
st.write("- Tried multiple algorithms and achieved the best results with **SVR (Support Vector Regression)**.")
st.write("- Fine-tuned model using **GridSearchCV** for optimal parameters.")

# Project Sections
st.markdown("## 📌 Project Sections")
st.write("This project is divided into three main sections:")
sections = [
    "📊 Analysis & Data Exploration",
    "💰 Flat Price Prediction",
    "🏡 Flat Recommendation System"
]

for section in sections:
    st.markdown(f"- {section}")

# Footer
st.markdown("---")
st.write("🔹 Developed with ❤️ by Team Members")
