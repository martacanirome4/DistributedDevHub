# p8/servcli/serv.py

import socket
import os
import sys
import time
from kata import Kata

p1 = Kata()
bufferSize = 4096

def server(server_address, server_port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.bind((server_address, server_port))
    except OSError as e:
        print(f"Error: Failed to bind the socket to {server_address}:{server_port}.")
        print(e)
        return
    
    s.listen(2)
    
    print(f"Server listening on {server_address}:{server_port}")

    while True:
        conn, addr = s.accept()
        print(f"Connection established with {addr}")
        child_pid = os.fork()
        if child_pid == 0:
            s.close()
            handle_client(conn)
            conn.close()  # Close connection in child process
            os._exit(0)
        else:
            conn.close()  # Close connection in parent process

def handle_client(conn):
    try:
        nombre_fichero = conn.recv(1024).decode("utf-8").strip()
        try:
            with open(nombre_fichero, "r") as fichero:
                palindromes = []
                vowels_count = 0
                starts_with_a = []
                words_gt_7_chars = []
                mixed_case_words = []

                for line in fichero:
                    words = line.strip().split()
                    for word in words:
                        if p1.esPalindromo(word):
                            palindromes.append(word)
                        vowels_count += p1.esVocal(word)
                        if p1.startsWithA(word):
                            starts_with_a.append(word)
                        if p1.palabrasQueTenganTamañoMayorQue7(word):
                            words_gt_7_chars.append(word)
                        if word.lower() != word and word.upper() != word:
                            mixed_case_words.append(word)

                response = "\n".join(palindromes) + "\n"
                response += str(vowels_count) + "\n"
                response += "\n".join(starts_with_a) + "\n"
                response += "\n".join(words_gt_7_chars) + "\n"
                response += "\n".join(mixed_case_words) + "\n"
                response += p1.entero_a_romano(2021) + "\n"
                response += p1.entero_a_romano(1094) + "\n"
                response += p1.entero_a_romano(47) + "\n"

                conn.sendall(response.encode("utf-8"))
        except FileNotFoundError:
            conn.sendall(b"Error: File not found or unable to open.\n")
    except Exception as e:
        print("An error occurred while handling client request:")
        print(e)
    finally:
        conn.close()


if __name__ == "__main__":
    if len(sys.argv) == 1:
        address = "0.0.0.0"
        port = 5111
    elif len(sys.argv) == 3:
        address = sys.argv[1]
        port = int(sys.argv[2])
    else:
        print("Usage: python Kata.py [address] [port]")
        exit(1)

    server(address, port)