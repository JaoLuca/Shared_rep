import time
primos =  [1,2,3]
lim = abs(int(input("Quantos primos quer: ")))
ndvez = 5
count=3
countprim=0
t0= time.time()
while countprim!=lim:
	while count != ndvez:
		if ndvez % count==0:
			ndvez = ndvez+2
			count = 3
		else:
			count = count + 2
	primos.append(ndvez)
	# print (ndvez)
	ndvez = ndvez + 2
	count = 3
	countprim = countprim+1
t1= time.time()

print(primos)
print('A operação com {} primos demorou {} segundos'.format(lim,t1-t0))

# 63.185163497924805 segundos printando
# 61.18964219093323 segundos n prnt
# 28.501092195510864 segundos incremento de 2 print