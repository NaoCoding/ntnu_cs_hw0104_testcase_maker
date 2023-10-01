import os

command = []
p = ["S: ","H: ","D: ","C: "]

for i in range(4):
	r = input(p[i]).split()
	for x in r:
		if(x=="A" or x=="a"):
			cmd = i*13 + 1
		elif(x=="K" or x == 'k'):
			cmd = i*13 + 13
		elif(x=='Q' or x=='q'):
			cmd = i*13 + 12
		elif(x=='J' or x =='j'):
			cmd = i*13 + 11
		else:
			cmd = i*13 + int(x)
		command.append(str(cmd)+"\n")
file = "./hw0104_testcase.txt"
with open(file,'w') as target:
	target.write("".join(command))

os.system("./hw0104 < ./hw0104_testcase.txt")
