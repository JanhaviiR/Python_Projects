import requests
import streamlit as st
from datetime import datetime

# Function to get weather data
def get_weather(city):
    api_key = "9063f69b6b0e4507bbc427b227cd1062"  # Replace with your OpenWeatherMap API key
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = base_url + "q=" + city + "&appid=" + api_key + "&units=metric"
    response = requests.get(complete_url)
    data = response.json()
    
    if data["cod"] != "404":
        main = data["main"]
        weather = data["weather"][0]
        temp = main["temp"]
        pressure = main["pressure"]
        humidity = main["humidity"]
        description = weather["description"]
        icon = weather["icon"]
        
        weather_info = f"**Temperature**: {temp}°C\n**Pressure**: {pressure} hPa\n**Humidity**: {humidity}%\n**Description**: {description.capitalize()}"
        icon_url = f"http://openweathermap.org/img/wn/{icon}@2x.png"
        return weather_info, icon_url
    else:
        return "City Not Found!", None

# Streamlit web app UI
st.set_page_config(page_title="Weather App", page_icon="☀️", layout="wide")

# Custom background image and styling for the app
st.markdown(
    """
    <style>
    .stApp {
        background-color: #ADD8E6; /* Light blue background color */
        color: black;
    }
    .stButton>button {
        background-color: #1E90FF; /* Blue background for the button */
        color: black; /* Black text color for the button */
        font-size: 16px;
        border-radius: 8px;
        padding: 10px 20px;
        font-weight: bold;
        border: none;
    }
    .stButton>button:hover {
        background-color: #4682B4; /* Darker blue when hovered */
    }
    .stTextArea textarea {
        background-color: #f0f0f0; /* Light gray background for the text area */
        color: black;
        font-size: 14px;
        padding: 10px;
        border-radius: 6px;
        border: 1px solid #ccc;
    }
    .footer {
        font-size: 14px;
        text-align: center;
        color: #A9A9A9;
        padding: 20px;
    }
    </style>
    """, unsafe_allow_html=True
)

# Title with an icon
st.title("🌤️ Weather App")

# Input for city name
city = st.text_input("Enter city name:", placeholder="e.g. London, New York", max_chars=50)

# Using expanders for better organization
with st.expander("Instructions", expanded=True):
    st.write("""
        1. Type the city name in the input box above.
        2. Click on **'Get Weather'** to fetch the data.
        3. The temperature, humidity, pressure, and description will be displayed.
    """)

# Button to trigger weather info
if st.button("Get Weather"):

    if city:
        # Fetch weather data
        weather_info, icon_url = get_weather(city)

        # Display dynamic temperature and weather info
        if icon_url:
            st.image(icon_url, width=100)  # Display weather icon
            st.subheader(f"Weather in {city.title()} ({datetime.now().strftime('%Y-%m-%d %H:%M:%S')})")

        st.text_area("Weather Info", weather_info, height=150, max_chars=500)
    else:
        st.warning("Please enter a valid city name to get weather data.")

# Footer with custom design
st.markdown("""
    ---
    <div class="footer">
        <p>Created with ❤️ using Streamlit</p>
        <p>Weather data from <a href="https://openweathermap.org/">OpenWeatherMap API</a></p>
    </div>
    """, unsafe_allow_html=True)
