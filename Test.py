import sys
import re
filename = sys.argv[1]
with open(filename,'r') as fp:
    lines = fp.readlines()
    y=len(lines)
    for i in lines[0:1]:
        words = i.split()
        word1 = int(words[0])
        m=(y)//(word1+2)
A = []
B = []
i=1

p=str(word1)

#Parameters
a=input("Name of the output file : ")
x=input("%nprocshared : " )
z=input("%mem : ")
functional=input("functinal : ")
basisset=input("basis set : ")
charge=input("charge : ")
mult=input("Multiplicity : ")


original_stdout = sys.stdout # Save a reference to the original standard output

for line in lines:
    l=line.strip()
    if l== p:
        A.append(B)
        
        if len(B) >= word1:
            B.pop(0)
            with open('{}_%i.com'.format(a) %(i), 'w') as f:
                f.write("%nprocshared={}".format(x) + "\n%mem={}GB".format(z) + "\n# opt freq=noraman "+ "{}".format(functional)+"/{}".format(basisset)+ "\n \n{}".format(a) + "\n \n{}".format(charge)+ " {}".format(mult)+ "\n")

                sys.stdout = f # Change the standard output to the file we created.
                print(*B, sep = "\n")
                sys.stdout = original_stdout # Reset the standard output to its original value
                f.write("\n \n")
                f.close()
                i=i+1
        B=[]
    else:
        B.append(l)

B.pop(0)
with open('{}_%i.com'.format(a) %(i), 'w') as f:
                f.write("%nprocshared={}".format(x) + "\n%mem={}GB".format(z) + "\n# opt freq=noraman "+ "{}".format(functional)+"/{}".format(basisset)+ "\n \n{}".format(a) + "\n \n{}".format(charge)+ " {}".format(mult)+ "\n")

                sys.stdout = f # Change the standard output to the file we created.
                print(*B, sep = "\n")
                sys.stdout = original_stdout # Reset the standard output to its original value
                f.write("\n \n")
                f.close()


	










