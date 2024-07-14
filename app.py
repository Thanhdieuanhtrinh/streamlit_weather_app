import streamlit as st
import requests

APIkey = st.secrets["APIkey"]
st.title("Weather App")
st.header("My weather app")

location = st.text_input("Enter your city location", value="Your city")
language = st.selectbox("Language selection", ["English", "Vietnamese"])
st.write("You entered:", location)


if language == "English":
    language = "en"
else:
    language = "vi"        
response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={location}&appid={APIkey}&units=metric&lang={language}")


# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Extract the weather data from the response
    weather_data = response.json()
    st.metric("Temperature", str(weather_data["main"]["temp"])+"°C", "1.2 °C")
    st.write(weather_data["weather"][0]["description"])

else:
    print("Error: Failed to retrieve weather data")

# st.write(weather_data["main"]["temp"])


