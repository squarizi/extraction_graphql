import requests


q = """
{ 
  website(url: "https://google.com/") {
    title
    image
    description
  }
}
"""


resp = requests.post("http://localhost:5000/", params={'query': q})
print(resp.text)
