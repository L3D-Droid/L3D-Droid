import sys
import re
filename = sys.argv[1]
with open(filename,'r') as fp:
	lines = fp.readlines()
	y=len(lines)
	for i in lines[0:1]:
        	words = i.split()
        	word1 = int(words[0])
	m=y//(word1+2)
	S1=str(word1)
	fp.close()
a=input("Name of the output file : ")
x=input("%nprocshared : " )
z=input("%mem : ")
functional=input("functinal : ")
basisset=input("basis set : ")
charge=input("charge : ")
mult=input("Multiplicity : ")
for i in range(1,m+1):
    with open(filename,'r') as fp:
        lines = fp.readlines()
        
    f = open("{}_%i.gjf".format(a) %(i),"w")
    f.write("%nprocshared={}".format(x) + "\n%mem={}GB".format(z) + "\n# opt freq=noraman empiricaldispersion=gd3bj "+ "{}".format(functional)+"/{}".format(basisset)+ "\n \n{}".format(a) + "\n \n {}".format(charge)+ " {}".format(mult)+ "\n")
   

    for number, line in enumerate(lines):
        if number not in [0, 1]:
            f.write(line)
            if line.strip("\n") == "  {}".format(S1):
                break
    f.close()

    

    with open(filename,'w') as fp:
        fp.writelines(lines[word1+2:])
        
