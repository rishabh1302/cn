import socket
def client_program():
	host=socket.gethostname()
	port=1234
	client_socket=socket.socket()
	client_socket.connect((host,port))
	name=input("Enter the name of the file")
	client_socket.send(name.encode())
	msg=client_socket.recv(1024).decode()
	print("Contents received from the server", msg)
	client_socket.close()
client_program()
