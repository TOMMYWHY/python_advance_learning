import requests

#   https://ip.ihuan.me/


url = "http://pronhub.com/"
proxies = {
    "http": 'http://200.110.174.130:8080'
}
headers = {
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36"
# "user-agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1"
}
response = requests.get(url, proxies=proxies, headers=headers)
print(response.status_code)
print(response.content)
