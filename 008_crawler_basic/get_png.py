import requests

url = "https://www.baidu.com/img/baidu_jgylogo3.gif"
headers = {}
response = requests.get(url,headers=headers,timeout = 3, verify = False)
# print(response.content)
print(response.status_code)
print(response.request.headers)
print(response.headers)
print(response.url)
print(response.request.url)

# with open("baidu.gif","wb") as f:
#     f.write(response.content)

