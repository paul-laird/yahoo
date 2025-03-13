import requests
import json
import pandas as pd
import time

url=f'https://query2.finance.yahoo.com/v8/finance/chart/NVDA?period1=1739494200&period2={int(time.time())}&interval=5m&includePrePost=true&events=div%7Csplit%7Cearn&&lang=en-US&region=US'

headers={'accept': '*/*',
'accept-encoding': 'gzip, deflate, br, zstd',
'accept-language': 'en-US,en;q=0.9',
'cache-control': 'no-cache',
'cookie': f'GUCS=ASTF5w0L; GUC=AQABCAFnuaRn6UIdogSV&s=AQAAAFGXNzqT&g=Z7hfuA; A1=d=AQABBK5fuGcCEIgFWNQR6ZF7ISuvyCWpcCoFEgABCAGkuWfpZ-Ijb2UBAiAAAAcIqF-4Z9txERE&S=AQAAAkwUiSG1FZkE-D2bD3shBhM; EuConsent=CQNLZQAQNLZQAAOACKENBdFgAAAAAAAAACiQAAAAAAAA; A1S=d=AQABBK5fuGcCEIgFWNQR6ZF7ISuvyCWpcCoFEgABCAGkuWfpZ-Ijb2UBAiAAAAcIqF-4Z9txERE&S=AQAAAkwUiSG1FZkE-D2bD3shBhM; A3=d=AQABBK5fuGcCEIgFWNQR6ZF7ISuvyCWpcCoFEgABCAGkuWfpZ-Ijb2UBAiAAAAcIqF-4Z9txERE&S=AQAAAkwUiSG1FZkE-D2bD3shBhM; cmp=t={int(time.time())}&j=1&u=1---&v=67; PRF=t%3DNVDA',
'origin': 'https://finance.yahoo.com',
'pragma': 'no-cache',
'priority': 'u=1, i',
'referer': 'https://finance.yahoo.com/quote/NVDA/',
'sec-ch-ua': '"Not(A:Brand";v="99", "Google Chrome";v="133", "Chromium";v="133"',
'sec-ch-ua-mobile': '?0',
'sec-ch-ua-platform': '"Windows"',
'sec-fetch-dest': 'empty',
'sec-fetch-mode': 'cors',
'sec-fetch-site': 'same-site',
'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36'}


resp=requests.get(url, headers=headers)

j=json.loads(resp.content)

df=pd.DataFrame(j['chart']['result'][0]['indicators']['quote'][0],index=j['chart']['result'][0]['timestamp'])

df.to_csv('NVDA.csv')