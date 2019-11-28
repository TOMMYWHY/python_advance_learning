import requests
import re
# import lxml
from lxml import etree
from queue import Queue
# import threading
from multiprocessing import Process
from multiprocessing import JoinableQueue as Queue
import time



class Goukr:
    def __init__(self):
        self.url_queue = Queue()
        self.html_queue = Queue()
        self.content_list_queue = Queue()
        self.url_temp = "https://www.guokr.com/ask/newest/?page={}"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36",
        }

    def get_url_list(self):
        # return [self.url_temp.format(i) for i in range(1, 101)]
        for i in range(1, 14):
            self.url_queue.put(self.url_temp.format(i))

    def parse_url(self):
        while True:
            url = self.url_queue.get()
            response = requests.get(url, headers=self.headers)
            print(response)
            # thml_str = response.content.decode()
            self.html_queue.put(response.content.decode())
            self.url_queue.task_done()  # queue -1

    def get_content_list(self):
        while True:
            html_str = self.html_queue.get()
            # content_list = re.findall(r'<h2><a target="_blank" href="(.*?)">(.*?)</a></h2>', html_str, re.S)
            html = etree.HTML(html_str)
            div_list = html.xpath("//ul[@class= 'ask-list']//div[@class='ask-list-detials']")
            content_list = []
            for div in div_list:
                item = {}
                item["tag"] = div.xpath(".//div/p/a/text()")
                item["question"] = div.xpath(".//h2/a/text()")
                item["timestamp"] = [i.strip() for i in div.xpath(".//div/p/span[@class= 'ask-list-time']/text()")]
                content_list.append(item)
            self.content_list_queue.put(content_list)
            self.html_queue.task_done()

    def save_content_list(self):
        while True:
            content = self.content_list_queue.get()
            print(content)
            self.content_list_queue.task_done()

    def run(self):
        thread_list = []
        t_url =Process(target=self.get_url_list)
        thread_list.append(t_url)
        for i in range(3):
            t_parse =Process(target=self.parse_url)
            thread_list.append(t_parse)

        t_content = Process(target=self.get_content_list)
        thread_list.append(t_content)

        t_save = Process(target=self.save_content_list)
        thread_list.append(t_save)

        for process in thread_list:
            process.daemon(True)
            process.start()

        for q in [self.url_queue,self.html_queue,self.content_list_queue]:
            q.join()  # main thread waiting....




def main():
    t1 = time.time()
    Goukr().run()
    print("times : ", time.time()-t1)

if __name__ == '__main__':
    main()
