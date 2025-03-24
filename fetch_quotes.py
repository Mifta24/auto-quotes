import requests
import datetime

# Ambil data dari API
url = "https://zenquotes.io/api/random"
response = requests.get(url)
data = response.json()

# Ambil quote & author
quote = data[0]["q"]
author = data[0]["a"]

# Format markdown
timestamp = datetime.datetime.now().strftime("%d %B %Y ⏳")

formatted_quote = f"""# 📜 Daily Quote

> "{quote}"  
> — **{author}**

---

_Last updated: {timestamp}_
"""

# Simpan ke quotes.md
with open("quotes.md", "w", encoding="utf-8") as file:
    file.write(formatted_quote)
