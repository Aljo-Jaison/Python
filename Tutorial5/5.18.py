import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("weather.csv")

#  1) Print first 10 rows of weather data
print(" First 10 Rows of Weather Data:\n", df.head(10))

#  2) Find the maximum and minimum temperature
max_temp = df["temperature"].max()
min_temp = df["temperature"].min()
print("\n Maximum Temperature:", max_temp)
print("Minimum Temperature:", min_temp)

#  3) List the places with temperature less than 28°C
low_temp_places = df[df["temperature"] < 28]["place"].unique()
print("\n Places with Temperature Less Than 28°C:\n", low_temp_places)

#  4) List the places with weather = “Cloudy”
cloudy_places = df[df["weather"] == "Cloudy"]["place"].unique()
print("\nPlaces with Cloudy Weather:\n", cloudy_places)

#  5) Sort and display each weather type and its frequency
weather_freq = df["weather"].value_counts()
print("\nWeather Frequency:\n", weather_freq)

#  6) Create a bar plot to visualize temperature of each day
plt.figure(figsize=(10, 5))
plt.bar(df["date"], df["temperature"], color="blue")
plt.xlabel("Date")
plt.ylabel("Temperature (°C)")
plt.title("Temperature Trend Over Time")
plt.xticks(rotation=45)  
plt.show()
