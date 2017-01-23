import os
import textwrap
from main.models import Book
import random

path = 'main/static/images/'
path_images = 'main/static/images/books'

genre = [
    "Fiction",
    "Fantasy",
    "History",
    "Horror",
    "Boring",
    "Realistic"
]



def generate():
    with open(os.path.join(path, 'names.txt'), "r") as file:
        names = file.read().split('\n')

    with open(os.path.join(path, 'authors.txt'), "r") as file:
        authors = file.read().split('\n')

    with open(os.path.join(path, 'descs.txt'), "r") as file:
        descs = textwrap.wrap(file.read(), 200)

    # print ( descs )

    images = list(filter( lambda x : "jpg" in x , next(os.walk(path_images))[2]))

    # print(images)

    for i in range(10):
        t = Book()
        t.name = random.choice(names)
        t.author = random.choice(authors)
        t.genre = random.choice(genre)
        t.imageUrl = os.path.join("images/books", random.choice(images))
        t.desc = random.choice(descs)
        t.save()