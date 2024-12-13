import socket

def port_scan(host, start_port, end_port):
    # Перетворюємо ім'я хоста в IP-адресу (якщо це можливо)
    target_ip = socket.gethostbyname(host)
    print(f"Сканування хоста: {host} ({target_ip})")
    print(f"Діапазон портів: {start_port}-{end_port}")
    print("Відкриті порти:")

    for port in range(start_port, end_port + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)  # таймаут на пів секунди
        result = sock.connect_ex((target_ip, port))
        if result == 0:
            print(f"Порт {port} відкритий")
        sock.close()

if __name__ == "__main__":
    host = input("Введіть хост (наприклад, google.com або IP): ")
    start_port = int(input("Введіть початковий порт: "))
    end_port = int(input("Введіть кінцевий порт: "))

    port_scan(host, start_port, end_port)
