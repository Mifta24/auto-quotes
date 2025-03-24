import requests
import json

API_URL = "https://zenquotes.io/api/quotes"

def get_quote():
    response = requests.get(API_URL)
    if response.status_code == 200:
        data = response.json()
        return f'> "{data[0]["q"]}"\n\n- {data[0]["a"]}'
    return "Failed to fetch quote."

if __name__ == "__main__":
    quote = get_quote()
    with open("quotes.md", "w") as file:
        file.write(quote)
        
    print("Quote saved to quotes.md")
