import requests

API_KEY = "YOUR_NEWSAPI_KEY"

url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={API_KEY}"

response = requests.get(url)

data = response.json()

print("TOP 5 NEWS HEADLINES")
print("-" * 40)

for i, article in enumerate(data["articles"][:5], start=1):
    print(f"{i}. {article['title']}")
