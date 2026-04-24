#flatten 
'''
a=[[1, 2, 3], [4, 5], [6, 7]]
b=[]
for i in a:
    for j in i:
        b.append(j)
print(b)
a=[[1, 2, 3], [4, 5], [6, 7]]
b=[j for i in a for j in i]
print(b)


from collections import Counter
s="hello world hello"
s1=s.split(' ')
print(Counter(s1))
'''
