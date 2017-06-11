import socket


def get_free_port():
    s = socket.socket(socket.AF_INET)
    s.bind(('', 0))
    s.listen(1)
    _, port = s.getsockname()
    s.close()
    return port


if __name__ == "__main__":
    print get_free_port()
