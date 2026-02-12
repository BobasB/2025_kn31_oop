import math
import random 

# Це все вбудовані бібліотеки, які не потрібно встановлювати через pip

# в нас ще немає Flask, встановимо її пізніше
#from flask import Flask

# є бібліотеки які не є вбудованими, але їх можна встановити через pip
import httpx
r = httpx.get('https://www.google.com/')
print(f"httpx: {r}")

import requests
r = requests.get('https://www.google.com/')
print(f"requests: {r}")
