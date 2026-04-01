import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY_STEAM")
STEAM_ID = os.getenv("STEAM_ID")

url = f"https://api.steampowered.com/IPlayerService/GetOwnedGames/v1/?key={API_KEY}&steamid={STEAM_ID}&include_appinfo=true&include_played_free_games=true"

response = requests.get(url)

print("Status Code:", response.status_code)
print(response.json())  # Imprime a resposta JSON para depuração

if response.status_code == 200:
    data = response.json()
    games = data.get("response", {}).get("games", [])
    
    for game in games:
        print(f"Game: {game['name']}, Playtime: {game['playtime_forever']} minutes")
else:
    print(f"Failed to retrieve data: {response.status_code}")
