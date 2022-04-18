from bs4 import BeautifulSoup
import requests
import json

j = '{"m": [{"alters": "&#x1d50;", "algs": ["NFKD", "NFKC"]}]}'

a = requests.get("https://appcheck-ng.com/wp-content/uploads/unicode_normalization.html")
soup = BeautifulSoup(a.content, "html.parser")
b = soup.find_all(['tr'])

output = {}

for i in range(1, len(b)):
    tds = BeautifulSoup(str(b[i]), "html.parser")
    td = tds.find_all(["td"])

    alters = []
    char = ""
    for j in range(len(td)):
        if j == 0:
            char = td[j].text
        elif j == 1:
            continue
        else:
            als = BeautifulSoup(str(td[j]), "html.parser")
            al = als.find_all(["font"])

            u = "&" + al[0].text.split("&")[1]
            t = al[1].text.split(",")
            #print(u)
            #print(t)
            alters.append(
                {
                    "alters": u,
                    "algs": t
                }
            )
    output[char] = alters

ccc = json.dumps(output)
f = open("test", "w")
f.write(ccc)



