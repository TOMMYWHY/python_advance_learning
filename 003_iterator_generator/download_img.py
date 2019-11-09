import urllib.request

import gevent
from gevent import monkey

monkey.patch_all()

def downloader(name,img_url):
    # url ="https://rpic.douyucdn.cn/live-cover/appCovers/2019/10/07/526583_20191007201520_small.jpg"
    req = urllib.request.urlopen(img_url)
    img_content = req.read()

    with open(name, "wb") as f:
        f.write(img_content)


def main():
     gevent.joinall([
         gevent.spawn(downloader,"1.jpg", "https://rpic.douyucdn.cn/live-cover/appCovers/2019/10/07/526583_20191007201520_small.jpg"),
         gevent.spawn(downloader,"2.jpg", "https://rpic.douyucdn.cn/live-cover/roomCover/2019/06/25/33610a984a21408ab9c0858b6452bb37_big.jpg")
     ])

     print("download completed~!")

if __name__ == '__main__':
    main()
