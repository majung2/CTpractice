scores = list(map(int,input().split()))

average = round((sum(scores)/len(scores)),2)
if average>=90:
	grade = 'A'
elif average >= 80:
	grade = 'B'
elif average >= 70:
	grade = 'C'
elif average >= 60:
	grade = 'D'
else:
	grade = 'F'

print(format(average,"5.2f"),end=' ')
print(grade)
	