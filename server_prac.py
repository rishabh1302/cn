import socket
def socket_program():
	host=socket.gethostname()
	port=1234
	server_socket=socket.socket()
	server_socket.bind((host,port))
	server_socket.listen(2)
	con,addr=server_socket.accept()
	print("Receiving name from client ",addr)
	msg=con.recv(1024).decode()
	print("Received data ",msg)
	f=open(msg)
	l=f.read()
	con.send(l.encode())
	con.close()
socket_program()
	
