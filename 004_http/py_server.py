import socket
import re


def service_client(new_socket, client_addr):
    request = new_socket.recv(1024).decode("utf-8")
    request_lines = request.splitlines()
    # ['GET /index HTTP/1.1', 'Host: 192.168.88.102:7890', 'Connection: keep-alive', 'Cache-Control: max-age=0', 'Upgrade-Insecure-Requests: 1', 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36', 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3', 'Accept-Encoding: gzip, deflate', 'Accept-Language: en-NZ,en;q=0.9,zh-CN;q=0.8,zh;q=0.7,en-GB;q=0.6,en-US;q=0.5', '']
    ret = re.match(r"[^/]+(/[^ ]*)", request_lines[0])
    # re: 从头开始^匹配多次+到/   /   从头开始^匹配到空格 可以0-多次
    if ret:
        file_name = ret.group(1)
    # print(">>"*30)
    print(file_name)

    # 读取 html
    try:
        f = open("./cv-blog"+file_name, "rb")
    except:
        response = "HTTP/1.1 404 NOT FOUND\r\n"
        response += "\r\n"
        response += "404"
        new_socket.send(response.encode("utf-8"))  # 转码

    else:
        content = f.read()
        f.close()
        response = "HTTP/1.1 200 OK \r\n"  # 协议头
        response += "\r\n"  # 空行
        new_socket.send(response.encode("utf-8"))  # 转码
        new_socket.send(content)  # 发送 body
        new_socket.close()




def main():
    # create server side socket
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_socket.bind(("", 7890))
    tcp_socket.listen(128)

    while True:
        new_socket, client_addr = tcp_socket.accept()
        service_client(new_socket, client_addr)

    tcp_socket.close()  # 关闭 socket。。。


if __name__ == '__main__':
    main()
