def Anagram(str1,str2):
    if(len(str1)==len(str2)):
        str1_sort = sorted(str1.lower())
        str2_sort = sorted(str2.lower())
        if(str1_sort == str2_sort):
            print('YES')
        else:
            print('NO')
    else:
        print('NO')
str1 = 'Mary'
str2 = 'Army'
Anagram(str1,str2)