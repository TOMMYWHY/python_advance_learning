import socket


def send_file_2_client(new_client_socket, client_addr):
    # receive data from client
    file_name = new_client_socket.recv(1024).decode("utf-8")
    print("client(%s) need download file: %s " % (str(client_addr), file_name))

    # send file data
    # new_client_socket.send("Nonviolent communication .....".encode("utf-8"))

    file_content = None
    try:
        f = open(file_name, "rb")
        file_content = f.read()
        f.close()
    except Exception as ret:
        print("cannot find the file: %s " % file_name)

    if file_content is not None:
        new_client_socket.send(file_content)


def main():
    # create tcp socket
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # bind server info
    tcp_server_socket.bind(("", 7890))

    # listen port
    tcp_server_socket.listen(128)  # 最大访问量

    while True:
        # get client
        new_client_socket, client_addr = tcp_server_socket.accept()

        # send data
        send_file_2_client(new_client_socket, client_addr)

        # close socket
        new_client_socket.close()

    tcp_server_socket.close()


if __name__ == '__main__':
    main()
