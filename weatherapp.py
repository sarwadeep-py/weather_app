import streamlit as st
import requests

API_KEY="c65ab5907553aeabfde0dc4adb9f6439"

def get_weather(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None
def clothing_recommendation(temp, humidity, weather_main, wind_speed):
    
    recommendation = []

    if temp > 30:
        recommendation.append("👕 Wear light cotton clothes")
        recommendation.append("🧢 Consider a cap or hat")
        
    elif 20 <= temp <= 30:
        recommendation.append("👚 Comfortable casual wear is perfect")

    elif 10 <= temp < 20:
        recommendation.append("🧥 Carry a light jacket")

    else:
        recommendation.append("🧣 Wear warm clothes / heavy jacket")


    if weather_main.lower() in ['rain', 'drizzle', 'thunderstorm']:
        recommendation.append("☔ Carry an umbrella")
        recommendation.append("👢 Waterproof footwear recommended")

    
    if humidity > 70:
        recommendation.append("💧 Wear breathable fabrics")

    if wind_speed > 10:
        recommendation.append("🧥 A windcheater is recommended")

    return recommendation

st.title("🌤️ Weather-Based Clothing Recommendation App")

city = st.text_input("Enter your city:")

if st.button("Get Recommendation"):
    
    if city:
        data = get_weather(city)

        if data:
            temp = data['main']['temp']
            humidity = data['main']['humidity']
            weather_main = data['weather'][0]['main']
            description = data['weather'][0]['description']
            wind_speed = data['wind']['speed']

            st.subheader(f"Weather in {city}")
            st.write(f"🌡️ Temperature: {temp}°C")
            st.write(f"🌥️ Condition: {description}")
            st.write(f"💧 Humidity: {humidity}%")
            st.write(f"🌬️ Wind Speed: {wind_speed} m/s")

            st.subheader("👗 Clothing Recommendation")

            recs = clothing_recommendation(temp, humidity, weather_main, wind_speed)

            for r in recs:
                st.write("✅", r)

        else:
            st.error("City not found. Please try again.")

    else:
        st.warning("Please enter a city name.")