import requests
import pandas as pd


url = "https://jsonplaceholder.typicode.com/users"
response = requests.get(url)
print(response.status_code) # 200 = success


data = response.json()


df = pd.DataFrame(data)
print(df.head())