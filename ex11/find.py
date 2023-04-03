import requests

# Enter the name of a Pokemon: Pikachu
# Name: Pikachu
# Abilities:
# - Static
# - Lightning-rod

str = input("Enter the name of a Pokemon: ")
res = requests.get("https://pokeapi.co/api/v2/pokemon/" + str.lower())
print("Name: " + str)
print("Abilities:")
for i in res.json()["abilities"]:
	print("-", i["ability"]["name"])