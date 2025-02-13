import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# Function to get diet recommendation
def get_diet(age, weight):
    if age < 18:
        diet = "Consult a pediatrician for a proper diet plan."
    elif age < 30:
        if weight < 50:
            diet = "High protein diet with moderate carbs and fats."
        elif weight < 70:
            diet = "Balanced diet with equal proportions of carbs, proteins, and fats."
        else:
            diet = "Low carb diet with high protein and moderate fats."
    elif age < 50:
        if weight < 50:
            diet = "High protein diet with moderate carbs and fats."
        elif weight < 70:
            diet = "Balanced diet with equal proportions of carbs, proteins, and fats."
        else:
            diet = "Low carb diet with high protein and moderate fats."
    else:
        if weight < 50:
            diet = "High protein diet with moderate carbs and fats."
        elif weight < 70:
            diet = "Balanced diet with equal proportions of carbs, proteins, and fats."
        else:
            diet = "Low carb diet with high protein and moderate fats."
    
    return diet

# Function to plot a circular graph (diet distribution)
def plot_circular_graph(age, weight):
    # Dummy data for proportions
    if age < 18:
        labels = ['Protein', 'Carbs', 'Fats']
        sizes = [20, 40, 40]
    elif age < 30:
        if weight < 50:
            labels = ['Protein', 'Carbs', 'Fats']
            sizes = [50, 30, 20]
        elif weight < 70:
            labels = ['Protein', 'Carbs', 'Fats']
            sizes = [33, 33, 34]
        else:
            labels = ['Protein', 'Carbs', 'Fats']
            sizes = [40, 30, 30]
    elif age < 50:
        if weight < 50:
            labels = ['Protein', 'Carbs', 'Fats']
            sizes = [50, 30, 20]
        elif weight < 70:
            labels = ['Protein', 'Carbs', 'Fats']
            sizes = [33, 33, 34]
        else:
            labels = ['Protein', 'Carbs', 'Fats']
            sizes = [40, 30, 30]
    else:
        labels = ['Protein', 'Carbs', 'Fats']
        sizes = [40, 30, 30]

    # Create a circular pie chart
    fig, ax = plt.subplots()
    ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90, colors=["#4CAF50", "#FF9800", "#2196F3"])
    ax.axis('equal')  # Equal aspect ratio ensures the pie chart is circular.

    return fig

# Streamlit web app UI
st.set_page_config(page_title="Diet Recommendation App", page_icon="🍏", layout="wide")

# Custom CSS to style the page
st.markdown("""
    <style>
    .stApp {
        background-color: #f0f0f5;
        font-family: 'Arial', sans-serif;
    }
    .title {
        font-size: 36px;
        color: #333;
        text-align: center;
        margin-top: 20px;
    }
    .header {
        font-size: 24px;
        color: #333;
        text-align: center;
        margin-top: 20px;
    }
    .footer {
        font-size: 14px;
        text-align: center;
        color: #777;
        padding: 20px;
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        font-size: 16px;
        padding: 10px 20px;
        border-radius: 5px;
    }
    .stButton>button:hover {
        background-color: #45a049;
    }
    .stTextArea>div>textarea {
        background-color: #ffffff;
        color: #333;
        font-size: 16px;
    }
    </style>
""", unsafe_allow_html=True)

# Title of the app
st.markdown('<h1 class="title">🍏 Diet Recommendation App</h1>', unsafe_allow_html=True)

# Input for age and weight
age = st.number_input("Enter your age:", min_value=1, max_value=120, value=25)
weight = st.number_input("Enter your weight (kg):", min_value=10, max_value=200, value=70)

# Display a logo (optional)
st.image('https://upload.wikimedia.org/wikipedia/commons/2/21/Apple_logo_black.svg', width=100)  # Example: Apple logo

# Button to trigger diet recommendation
if st.button("Get Diet", key="get_diet_button"):
    diet_info = get_diet(age, weight)
    
    # Show the diet info
    st.text_area("Diet Recommendation:", diet_info, height=150)

    # Plot the circular graph for diet proportions
    fig = plot_circular_graph(age, weight)
    st.pyplot(fig)

# Footer with custom design
st.markdown("""
    <div class="footer">
        <p>Created with ❤️ using Streamlit</p>
        <p>Diet data generated based on age and weight</p>
    </div>
""", unsafe_allow_html=True)
