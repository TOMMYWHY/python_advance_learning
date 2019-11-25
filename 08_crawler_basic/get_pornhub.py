import requests
from retrying import retry


class PronHub:
    def __init__(self):
        self.url = "https://www.pornhub.com/"
        # self.url = "https://www.ornhub.com/"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36"
        }


    @retry(stop_max_attempt_number=3)
    def __parse_url(self):
        print("*"*10)
        response = requests.get(self.url, self.headers, verify=False, timeout=3);
        assert response.status_code == 200
        return response.content.decode()

    def parse_url(self):
        try:
            html_str = self.__parse_url()
        except Exception as e:
            print(e)
            html_str = None
        return html_str

    def get_pornhub(self):
        response = self.__parse_url()
        print(response)

    # print(response.content)


def main():
    pron = PronHub()
    print(pron.parse_url())

if __name__ == '__main__':
    main()
