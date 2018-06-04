#!/usr/bin/python3

import requests
import sys

request = requests.get("https://www.gitignore.io/api/" + "%2C".join(sys.argv[1:]))
file = open(".gitignore", "w")
file.write(request.text)
file.close
