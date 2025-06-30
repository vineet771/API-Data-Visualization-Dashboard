import requests
import matplotlib.pyplot as plt
import seaborn as sns


API_KEY = "41967bb11f781c7d979d0ed6118b643c"  # yahan apna actual API key daalo
city = "NOIDA"


url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

# API request bhejna
response = requests.get(url)
data = response.json()

# Data extract karna
temp = data['main']['temp']
humidity = data['main']['humidity']
pressure = data['main']['pressure']
weather = data['weather'][0]['main']

# Data visualize karne ke liye prepare karo
labels = ['Temperature (°C)', 'Humidity (%)', 'Pressure (hPa)']
values = [temp, humidity, pressure]
#  Graph banana
sns.set(style="whitegrid")
plt.figure(figsize=(8, 5))
sns.barplot(x=labels, y=values, palette="coolwarm")
plt.title(f"Current Weather in {city} - {weather}")
plt.ylabel("Value")
plt.tight_layout()
plt.show()
