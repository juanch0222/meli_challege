import requests

def bestInGenre(genre: str) -> str:
    url = 'https://jsonmock.hackerrank.com/api/tvseries'
    response = requests.get(url)
    data = response.json()
    
    

    


      