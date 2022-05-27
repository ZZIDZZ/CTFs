import requests

url = "https://jupiter.challenges.picoctf.org/problem/13594"

r = requests.get(url)

print(r.text)