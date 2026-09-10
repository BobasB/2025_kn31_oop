import math
import random 
import os

# Це все вбудовані бібліотеки, які не потрібно встановлювати через pip

# в нас ще немає Flask, встановимо її пізніше
#from flask import Flask

# є бібліотеки які не є вбудованими, але їх можна встановити через pip
import httpx

u = os.getenv('URL_TEST')
r = httpx.get(u)
print(f"httpx: {r} коли доступаємось до URL_TEST: {u}")

import requests
r = requests.get(u)
print(f"requests: {r} коли доступаємось до URL_TEST: {u}")

def nonConventionalFunction(x):
    return math.sin(x) + random.random()


print(f"Витягуємо змінні TEST: {os.getenv('TEST')}")
