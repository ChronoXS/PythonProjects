
for row in range (3):

	for bos in range(int (2-int(row))):
		print (" ", end="")
	print("/",end="") 
	for arabos in range (int(int(row)*2)):
		print (" ",end="")
	print("\\",end="")	
	print("")
for row in range (3):
	
	for bos in range(int (row)):
		print(" ",end="")	
	print("\\",end="")
	for arabos in range ((int(2-int(row))*2)):
		print(" ",end="")
	print("/",end="")
	print("")	