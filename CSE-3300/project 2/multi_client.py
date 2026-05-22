from socket import *

SERVER_HOST = 'localhost'
SERVER_PORT = 26382

def client():
    '''
    connect to port, send query, and print response

    sources:
    https://stackoverflow.com/questions/7749341/basic-python-client-socket-example
    https://www.geeksforgeeks.org/socket-programming-python/
    https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers
    '''

    # initialize socket connection on client side (used stack overflow to help)
    sock = socket(AF_INET, SOCK_STREAM)
    sock.connect((SERVER_HOST, SERVER_PORT))
    
    # keep querying while user doesn't exit
    while True:
        query = input("enter your query (or 'exit' to quit): ").strip()
        if query.lower() == 'exit':
            break # exit loop

        # sends request (header format from mozilla developer)
        request = f"GET /search?q={query} HTTP/1.1\r\nHost: {SERVER_HOST}:{SERVER_PORT}\r\n\r\n"
        
        # send query and print response
        sock.send(request.encode()) # used geeksforgeeks to know to encode
        response = sock.recv(4096).decode() # used geeksforgeeks to know to decode
        print("server response:\n", response)
    
    # close connection
    sock.close()

client()