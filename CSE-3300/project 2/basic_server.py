import re
from socket import *

HOST = ''
PORT = 26382


def find_matching_words(query, wordlist):
    '''
    search for matching words based on the wildcard query
    
    sources:
    https://stackoverflow.com/questions/12677178/regular-expression-with-wildcards-to-match-any-character
    '''

    # convert '?' to '.' for pattern matching, used stack overflow to understand regex wildcard
    pattern = query.replace("?", ".")
    matches = [word for word in wordlist if re.fullmatch(pattern, word) and len(word) == len(query)]
    return matches


def parse_http_request(request):
    '''
    parses an HTTP-like request and extracts the query

    sources:
    https://www.geeksforgeeks.org/write-regular-expressions/
    '''
    lines = request.split("\r\n")
    if not lines:
        return None
    
    # check if request follows the format: GET /search?q=word HTTP/1.1
    match = re.match(r"GET /search\?q=([a-zA-Z?]+) HTTP/1\.1", lines[0]) # used geeksforgeeks to build regex
    if match:
        return match.group(1)  # extract query
    return None


def handle_client(conn, addr, wordlist):
    '''
    handles connecting to client and returning client's query

    sources:
    https://www.geeksforgeeks.org/socket-programming-python/
    https://www.w3schools.com/python/python_regex.asp
    https://developer.mozilla.org/en-US/docs/Web/HTTP/Status
    https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers
    '''

    print(f"connected by {addr}")
    while True:

        # get client data
        data = conn.recv(1024).decode().strip() # process message (recv and decode from geeksforgeeks)
        if not data:
            break # exit if client disconnects

        print(f"received query: {data}") # for testing
        
        # find and send response, using HTTP codes (HTTP codes and formats referenced from mozilla web docs)
        query = parse_http_request(data)
        if query is None:
            response = "HTTP/1.1 400 Bad Request\r\nContent-Type: text/plain\r\n\r\n400 Bad Request"
            
        else:
            matches = find_matching_words(query, wordlist)
            if matches: # send matching words
                response = f"HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\nContent-Length: {len(matches)}\r\n\r" + "\n".join(matches)
            else: # no content :(
                response = "HTTP/1.1 204 No Content\r\nContent-Type: text/plain\r\n\r\n204 No Content"

        conn.send(response.encode()) # send response
    conn.close()


def server():
    '''
    creates the server to handle a client

    sources:
    https://www.geeksforgeeks.org/socket-programming-python/
    https://www.datacamp.com/tutorial/a-complete-guide-to-socket-programming-in-python
    '''

    # open wordlist and read it
    with open('wordlist.txt', "r") as file:
        wordlist = set(file.read().splitlines()) # save into set for speed
    
    # initialize socket and set host, port, and connections (used datacamp tutorial to initialize)
    sock = socket(AF_INET, SOCK_STREAM)
    sock.bind((HOST, PORT))
    sock.listen(1) # takes only one connection
    
    print(f"server up on port {PORT}...")

    # process clients while server is active
    while True:
        conn, addr = sock.accept() # accept client (used geeksfor geeks to understand how to do this)
        handle_client(conn, addr, wordlist) # process client

server()