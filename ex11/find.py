import requests

str = input("Enter the name of a Pokemon: ")
res = requests.get("https://pokeapi.co/api/v2/pokemon/" + str.lower())
print("Name: " + str)
print("Abilities:")
for i in res.json()["abilities"]:
	print("-", i["ability"]["name"])
