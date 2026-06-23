import streamlit as st
import requests

api_key = "e0db8060c45ea86dd0212153e0bfb43a"
ip_url = "http://ip-api.com/json/"
response = requests.get(ip_url)
data = response.json()
city = data["city"]
weather_url = "https://api.openweathermap.org/data/2.5/weather"
params = {
    "q": city,
    "appid": api_key,
    "units": "metric"
}
response = requests.get(weather_url, params=params)
weather_data = response.json()
temp = weather_data["main"]["temp"]
humidity = weather_data["main"]["humidity"]
wind = weather_data["wind"]["speed"]
weather_desc = weather_data["weather"][0]["description"]

st.title("🌤️ Weather App")
st.write("---")
st.subheader(f"📍 Weather for {city}")
st.write("")
st.write("## Temperature 🌡️")
st.write(f"### {round(temp,1)} °C")
st.write("## Humidity 💧")
st.write(f"### {humidity} %")
st.write("## Wind 💨")
st.write(f"### {wind} m/s")
st.write("## Weather Description ⛅️")
st.write(f"### {weather_desc.capitalize()}")
st.write("---")
st.write("Note: This app automatically detects locations based on IP address.")
st.write("---")