import requests
from datetime import datetime

API_KEY = "YOUR_NEWSAPI_KEY"

url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={API_KEY}"

response = requests.get(url)

data = response.json()

message = f"Top 5 News Headlines ({datetime.now().strftime('%d-%m-%Y')})\n\n"

for i, article in enumerate(data["articles"][:5], start=1):
    message += f"{i}. {article['title']}\n\n"

print(message)
