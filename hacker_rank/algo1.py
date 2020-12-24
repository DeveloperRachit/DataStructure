s="eiuaooo"
k=4
#print(s[1:k+1])
vowel_counts={}
check_vowels={}
ls=[s[i:j+1] for i in range(len(s)) for j in range(i,len(s)) ]
#print(ls)
list_of_ele=[i for i in ls if len(i)==k]
print(list_of_ele)
print("_______listinf______")
#print([ i for i in list_of_ele])
max_vowel={}
count_value={}
for ele in list_of_ele:
    for vowel in 'aeiou':
        count=ele.count(vowel)
        max_vowel[vowel]=count

    count_value[ele]=sum(max_vowel.values())
print("______maximum value_________")
print(count_value)
print("substring is",max(count_value,key=count_value.get))



'''
for i in range(len(s)):
    print(s[i:k+1])
    if len(s[i:k+i])==k:
        for vowel in 'aeiou':
            count =s[i:k+i].count(vowel)
            vowel_counts[vowel]=count
        check_vowels[s[i:k+i]]=sum(vowel_counts.values())
lst={}
for keys,values in check_vowels.items():
        if values==max(check_vowels.values()):
              #print(keys,values)
              lst[values]=keys
print(lst)    
if max(lst.keys())==0:
    print 'Not found!'
else:
    print(lst.values()[-1])

'''         
