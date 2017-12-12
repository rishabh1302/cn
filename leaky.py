import time 
a=[200,500,450,400,700,200]
b=a[::-1]
print("Initial packets",b)
while len(b)!=0:
	n=1000
	while n>b[0]:
		print("Packet of size ",b[0],"  sent over the network")
		print("Queue after sending packet ",b[0])
		n=n-b[0]
		print("Size of updated bucket ",n)
		b.remove(b[0])
		#print("Queue after sending packet ",b[0])
		print(b)
		time.sleep(5)
		if len(b)==0:
			break
		if n<b[0]:
			print("Packet size",b[0]," larger than bucket size ",n,".Resetting timer ")
	time.sleep(10)
