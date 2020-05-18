f = open("output.txt",'w')
for i in range(1,11):
    data = "%d번째 줄입니다.\n" % i
    f.write(data)
f.close()

f = open("input.txt",'r')
while True:
    line = f.readline()
    if not line: break
    print(line)
f.close()

f = open('input.txt','r')
f1 = open('output.txt','w')
lines = f.readlines()
for line in lines:
    f1.write(line)
f.close()