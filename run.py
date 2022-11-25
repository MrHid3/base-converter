num = int(input("number to convert: "))
base = int(input("base to convert to: "))
res = []
resstr = ""

while num > 0:
	res.append(num%base)
	num = (num - (num%base)) / 6
res.reverse()

for i in range(len(res)):
	resstr += str(int(res[i]))

print(resstr)
