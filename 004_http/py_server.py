import socket
import re
import gevent
from gevent import monkey

monkey.patch_all()


def service_client(new_socket, request):
    # request = new_socket.recv(1024).decode("utf-8")
    request_lines = request.splitlines()
    file_name = ""
    # ['GET /index HTTP/1.1', 'Host: 192.168.88.102:7890', 'Connection: keep-alive', 'Cache-Control: max-age=0', 'Upgrade-Insecure-Requests: 1', 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36', 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3', 'Accept-Encoding: gzip, deflate', 'Accept-Language: en-NZ,en;q=0.9,zh-CN;q=0.8,zh;q=0.7,en-GB;q=0.6,en-US;q=0.5', '']
    ret = re.match(r"[^/]+(/[^ ]*)", request_lines[0])
    # re: 从头开始^匹配多次+到/   /   从头开始^匹配到空格 可以0-多次
    if ret:
        file_name = ret.group(1)
    # print(">>"*30)
    print(file_name)

    # 读取 html
    try:
        f = open("./cv-blog" + file_name, "rb")
    except:
        response = "HTTP/1.1 404 NOT FOUND\r\n"
        response += "\r\n"
        response += "404"
        new_socket.send(response.encode("utf-8"))  # 转码

    else:
        content = f.read()
        f.close()

        response_body = content
        response_header = "HTTP/1.1 200 OK \r\n"  # 协议头
        response_header += "Content-Length: %d \r\n" % len(response_body)  # 设置长度，以便于长连接的结束
        response_header += "\r\n"  # 空行
        response = response_header.encode("utf-8") + response_body

        new_socket.send(response)  # 发送 body

        # new_socket.close()


def main():
    # create server side socket
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_socket.bind(("", 7890))
    tcp_socket.setblocking(False)  # 设置非阻塞
    tcp_socket.listen(128)

    client_socket_list = list()  # 单线程 非阻塞
    while True:
        try:
            new_socket, client_addr = tcp_socket.accept()
        except Exception as ret:
            print("no one connect yet...")
        else:
            new_socket.setblocking(False)
            client_socket_list.append(new_socket)

        for client_socket in client_socket_list:
            try:
                recv_data = client_socket.recv(1024).decode("utf-8")
            except Exception as ret:
                print("not receive yet...")
            else:
                if recv_data:
                    service_client(client_socket, recv_data)
                else:
                    client_socket.close()  # 断开 connect
                    client_socket_list.remove(client_socket)  # 移除
        # 创建协程
        # gevent.spawn(service_client, new_socket, client_addr)

        # service_client(new_socket, client_addr)

    tcp_socket.close()  # 关闭 socket。。。


if __name__ == '__main__':
    main()
