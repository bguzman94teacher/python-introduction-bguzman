# https://pypi.org/
# python.exe -m pip install --upgrade pipx
# python -m venv python_introduction
# python_introduction\Scripts\activate
# pip install requests or pip install -r requirements.txt



import requests

response = requests.get('https://api.github.com')
print(response.status_code)
print(response.json())

# import aprendepython

# aprendepython.comenzar()