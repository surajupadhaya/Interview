'''
a=[-1,-2,1,3,4,1,2,431,2,2,21,-4,-5,-6,77,8,9,10,-11,-12,-13,-14,-15,-16,17,18,19,20]
positive=[]
negative=[]
for i in a:
    if i>0:
        positive.append(i)
    else:
        negative.append(i)
mergerlist=positive+negative
print(mergerlist)


test_data = ["swiss", "aabbcc", "v", "", "Success"]

def first_unique_char(s):
    char_count = {}
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    for char in s:
        if char_count[char] == 1:
            return char
    return None

for s in test_data:
    result = first_unique_char(s)
    print(f"First unique character in '{s}': {result}")

'''
'''
a=[[10,12,123],[1,2,3],[4,5,6]]
flat=[]
for i in a:
    for j in i:
        flat.append(j)
print(flat)

'''
'''
a=[2,1,3,4,5]
k=3
l=0
r=k-1
n=len(a)
result=[]
while r <n :
    result.append(max(a[l:r+1]))
    l+=1
    r+=1
print(result)
'''
'''
a=[2,3,4,5,6]
target=9
result=[]
l=0
r=len(a)-1
while l<r:
    current_sum=a[l]+a[r]
    if current_sum==target:
        result.append((a[l],a[r]))
        l+=1
        r-=1
    elif current_sum<target:
        l+=1
    else:
        r-=1
print(result)
'''
'''
a = [5, 2, 6, 3, 4]
target = 9
result=[]
seen ={}
for num in a :
    comp= target - num
    if comp in seen:
        result.append((comp,num))
    seen[num]=True
print(result)

'''

import copy


names = [["Alice"], "Bob", "Charlie", "David", "Eve"]

print(names)
shallow_copied_names = names.copy()
shallow_copied_names[0].append("Smith")
print("After modifying shallow copy:")

print("Shallow copied names:", shallow_copied_names)
print("Original names:", names)
deep_copied_names = copy.deepcopy(names)
deep_copied_names[1] = "Yara"
print("After modifying deep copy:")
print("Deep copied names:", deep_copied_names)
print("Original names:", names)

