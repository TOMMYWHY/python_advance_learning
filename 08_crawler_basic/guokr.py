import requests
import re


class Goukr:
    def __init__(self):
        self.url_temp = "https://www.guokr.com/ask/newest/?page={}"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36",
        }

    def get_url_list(self):
        # self.url_temp.format(0)
        return [self.url_temp.format(i) for i in range(1, 101)]

    def parse_url(self, url):
        reeponse = requests.get(url, headers=self.headers)
        thml_str = reeponse.content.decode()
        return thml_str

    def get_content_list(self, html_str):
        content_list = re.findall(r'<h2><a target="_blank" href="(.*?)">(.*?)</a></h2>', html_str, re.S)
        return content_list

    def save_content_list(self,content_list):
        for content in content_list:
            print(content)

    def run(self):
        url_list = self.get_url_list()
        for url in url_list:
            html_str = self.parse_url(url)
            content_list = self.get_content_list(html_str)
            self.save_content_list(content_list)

def main():
    Goukr().run()


if __name__ == '__main__':
    main()
