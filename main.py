import json
from statistics import mode
import numpy as np
import matplotlib.pyplot as plt

year = int(input("What decade do you want your film to be from? Say 1 for 1980s, 2 for 1990s, 3 for 2000s and 4 for 2010s"))

if year == 1:
    f = open("movies-1980s.json")
    data = list(json.load(f))
elif year == 2:
    f = open("movies-1990s.json")
    data = list(json.load(f))
elif year == 3:
    f = open("movies-2000s.json")
    data = list(json.load(f))
elif year == 4:    
    f = open("movies-2010s.json")
    data = list(json.load(f))

#first fav

favMovie = input("What is your favourite movie? (has to be from this decade)")

found = False

for i in data:
    if i["title"].lower() == favMovie.lower():
        favMovie = i
        found = True 
        break

if not found: 
    print("Sorry, but we couldn't find that movie. Did you make a typo?")
    exit()

#second fav

found = False
secondFavMovie = input("What is your second favourite movie? (has to be from this decade)")

for i in data:
    if i["title"].lower() == secondFavMovie.lower():
        secondFavMovie = i
        found = True 
        break

if not found: 
    print("Sorry, but we couldn't find that movie. Did you make a typo?")
    exit()

#code

possibleMovies = []

for i in data:
    for f in favMovie["genres"]:
        if f in i["genres"] or f in secondFavMovie["genres"]:
            possibleMovies.append(i)

genres = []

for i in possibleMovies:
    print(i["title"])
    for g in i["genres"]:
        genres.append(g)
    
genreFreq = {}

def countFreq(arr, dictionary):
   n = len(arr)

   visited = [False for i in range(n)]

   for i in range(n):
     if (visited[i] == True):
        continue

     count = 1
     for j in range(i + 1, n, 1):
        if (arr[i] == arr[j]):
          visited[j] = True
          count += 1

     dictionary[arr[i]] = count

countFreq(genres, genreFreq)

topfive = {}

x=list(genreFreq.values())
d=dict()
x.sort(reverse=True)
x=x[:5]

for i in x:
    for j in genreFreq.keys():
        if(genreFreq[j]==i):
            print(j)
            topfive[j] = genreFreq[j]

print(topfive)

topMovies = []

for i in possibleMovies:
    if all(item in list(topfive.keys()) for item in i["genres"]):
        
        if i not in topMovies:
            topMovies.append(i)
            print(i["title"])

    arr = []
    labels = []

    for i,v in enumerate(topfive.values()):
        if v != 0:
            labels.append(list(topfive.keys())[i])
            arr.append(v)

    y = np.array(arr)

    plt.pie(y, labels=labels, autopct="%1.1f%%")
    plt.title("Genres you may like based on your favourite films", fontsize=15)
    plt.show()