#import socket module
from socket import *
serverPort=80
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('',serverPort))
serverSocket.listen(1)
while True:
	print 'Ready to serve...'
	connectionSocket, addr = serverSocket.accept()
	try:
	    # message => GET /FILENAME HTTP/1.1
		message = connectionSocket.recv(1024)
		filename = message.split()[1]
		f = open(filename[1:])
		outputdata = f.read()
        #Send the content of the requested file to the client
		for i in range(0, len(outputdata)):
			connectionSocket.send(outputdata[i])
		connectionSocket.close()
	except IOError:
		#Send response message for file not found
		connectionSocket.send('\nHTTP/1.1 404 Not Found\n\n')
		connectionSocket.close()
connectionSocket.close()
