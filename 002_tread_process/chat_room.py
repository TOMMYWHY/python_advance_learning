import socket
import threading


def recv_msg(udp_socket):
    while True:
        recv_data = udp_socket.recvfrom(1024)
        print(recv_data)


def send_msg(udp_socket, dest_ip, dest_port):
    while True:
        # send data
        send_data = input("enter msg: ")
        udp_socket.sendto(send_data.encode("utf-8"), (dest_ip, dest_port))


def main():
    """udp chatting room"""
    # create socket
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # udp

    # bind local info
    udp_socket.bind(("", 7890))

    # get other ip
    dest_ip = input("enter ip：")
    dest_port = int(input("enter port："))

    # 创建 子线程
    t_recv = threading.Thread(target=recv_msg, args=(udp_socket))
    t_send = threading.Thread(target=send_msg, args=(udp_socket,dest_ip,dest_port))

    # receive data
    t_recv.start()

    # send data
    t_send.start()


if __name__ == '__main__':
    main()
