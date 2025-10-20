#Permite ocupar el modulo requests, para hacer peticiones HTTP
import requests
#requests.get(url) sirve para hacer peticiones GET a una URL, y get() retorna la respuesta de la peticion
#genre: str es el parametro que recibe la funcion, en este caso el genero
#Funcion que retorna el nombre del mejor show de un genero
def bestInGenre(genre: str) -> str:
    best_show = "No encontrado"
    rating = 0
    page = 1
    #Se evalua la cantidad de paginas
    while True:
        #Se hace la peticion GET a la API, la f""" permite que la url tenga variables, como page
        response = requests.get(f"https://jsonmock.hackerrank.com/api/tvseries?page={page}")
        #response.json() retorna un diccionario con la respuesta de la peticion
        data = response.json()
        #print(data)
        #Se evalua la cantidad de shows
        for show in data["data"]:
            # el if evalua si el genero ingresado esta en el show, .lower() permite que no importe si esta en mayusculas o minusculas
            if genre.lower() in show["genre"].lower():
                #rating_actual es el rating del show actual, float() permite convertir el rating a un numero decimal
                rating_actual = float(show["imdb_rating"])
                #Se evalua si el rating actual es mayor que el rating anterior
                if rating_actual > rating:
                    rating = rating_actual
                    best_show = show["name"]
                #Se evalua si el rating actual es igual que el rating anterior y el nombre del show es menor alfabeticamente
                elif rating_actual == rating and show["name"].lower() < best_show.lower():
                    best_show = show["name"]
        #Se evalua si la pagina es mayor o igual a 20
        if page >= 20:
            break   
        page += 1
    #Se retorna el nombre del mejor show
    return best_show

#Imprime el resultado de la funcion
genre = input("Ingrese el genero: ")
print(bestInGenre(genre))



    

    

    


      