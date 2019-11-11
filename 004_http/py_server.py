import socket


def service_client(new_socket, client_addr):
    request = new_socket.recv(1024)
    print(request)

    response = "HTTP/1.1 200 OK \r\n"
    response += "\r\n"
    response +="<h1>hello tommy</h1>"
    new_socket.send(response.encode("utf-8"))


def main():
    # create server side socket
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_socket.bind(("", 7890))
    tcp_socket.listen(128)
    new_socket, client_addr = tcp_socket.accept()
    service_client(new_socket, client_addr)
    pass


if __name__ == '__main__':
    main()
