n=[20,64,34,65,88,2,5,66,77,4,28]
count=0
loopcount=0
while True:
	loopcount+=1
	for i in range(len(n)):
		loopcount+=1
		try:
			if n[i]>n[i+1]:
				n[i],n[i+1]=n[i+1],n[i]
				count+=1
		except IndexError:
			break
	if count==0:
		break
	count=0
print(n)
print(loopcount)

	