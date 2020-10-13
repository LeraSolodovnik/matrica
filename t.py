a=[]
b=[]
c=[]
print ("Введите количество строк")
n=int(input())
print ("Введите количество столбцов")
m=int(input())
k=0

print ("Введите массив a")
for i in range (n):
	for j in range (m):
		a.append(int(input()))

print ("Введите массив b")
for i in range (n):
	for j in range (m):
		b.append(int(input()))

print ("Введите, что сделать с ними + - *")
dei=input()


if (dei=="+"):
	for i in range (n):
		for j in range (m):
			c.append(a[k]+b[k])
			k+=1
	l=0
	for i in range (n):
		for j in range(m):
			print(c[l], end=' ')
			l+=1
		print()

if (dei=="-"):
	for i in range (n):
		for j in range (m):
			c.append(a[k]-b[k])
			k+=1
	l=0
	for i in range (n):
		for j in range(m):
			print(c[l], end=' ')
			l+=1
		print()


if (dei=="*"):
	for i in range (n):
		for j in range (m):
			c.append(a[k]*b[k])
			k+=1
	l=0
	for i in range (n):
		for j in range(m):
			print(c[l], end=' ')
			l+=1
		print()


