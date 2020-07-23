import requests

url = 'http://10.10.167.171/note.php?note='

for i in range (0, 100):
    r = requests.get(url + str(i))
    print(f"Requesting for {i}")
    if r.text:
        print(r.text)
        break
   