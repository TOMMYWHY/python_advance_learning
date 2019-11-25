import requests
from retrying import retry


class PronHub:
    def __init__(self):
        # self.url = "https://www.pornhub.com/users/tommhwy/photos"
        self.url = "https://www.pornhub.com/users/tommhwy/videos/favorites"
        self.headers = {
            "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36",
            # "Cookie": " bs=72h3igjk9bmqk6x177at8owqlfel57pr; ss=476161289595463330; platform_cookie_reset=pc; platform=pc; RNLBSERVERID=ded6890; il=v1w0-3lcCkTLgo8FlnkdjoqpI5vEiNpjtAM9VitVNWChMxNTgyMTA5MzgyX0RZLTlQYXlyT3EwZ3Z1RVVNZnRqZ1RqaVQ3UGlSdWtsXzIzWW12ZQ..; expiredEnterModalShown=1; ua=babcfa814577ea16cf872ffdaf414057"
        }
        self.cookie_str =" bs=72h3igjk9bmqk6x177at8owqlfel57pr; ss=476161289595463330; platform_cookie_reset=pc; platform=pc; RNLBSERVERID=ded6890; il=v1w0-3lcCkTLgo8FlnkdjoqpI5vEiNpjtAM9VitVNWChMxNTgyMTA5MzgyX0RZLTlQYXlyT3EwZ3Z1RVVNZnRqZ1RqaVQ3UGlSdWtsXzIzWW12ZQ..; expiredEnterModalShown=1; ua=babcfa814577ea16cf872ffdaf414057"

        self.cookie_dict =  {i.split("=")[0]:i.split("=")[1] for i in self.cookie_str.split("; ")}

    @retry(stop_max_attempt_number=3)
    def __parse_url(self):
        print("*" * 10)
        response = requests.get(self.url, self.headers,
                                cookies = self.cookie_dict
                                # verify=False, timeout=3
                                );
        assert response.status_code == 200
        return response.content.decode()

    def parse_url(self):
        try:
            html_str = self.__parse_url()
        except Exception as e:
            print(e)
            html_str = None
        # return html_str
        print(self.cookie_dict)
        print(html_str)
        with open("pronhub_favorites.html", "w", encoding="utf-8") as f:
            f.write(html_str)

    def get_pornhub(self):
        response = self.__parse_url()
        print(response)

    # print(response.content)


def main():
    pron = PronHub()
    print(pron.parse_url())


if __name__ == '__main__':
    main()
