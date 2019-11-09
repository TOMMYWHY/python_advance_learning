"""socket"""
import socket


def main():
    # create tcp socket
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # server info
    dest_ip = input("enter download server IP: ")
    dest_port = int(input("enter download server Port: "))

    # connect server
    tcp_socket.connect((dest_ip, dest_port))

    # send file name
    download_file_name = input("enter download file name: ")
    tcp_socket.send(download_file_name.encode("utf-8"))  # encode

    # receive data from server
    recv_data = tcp_socket.recv(1024)
    if recv_data :
        # save data
        with open("[new]"+download_file_name,"wb") as f:  # with as 1. 处理异常，2.不用 close
            f.write(recv_data)

    # close socket
    tcp_socket.close()

if __name__ == "__main__":
    main()
