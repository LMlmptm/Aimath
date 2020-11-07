#输入一个字符串,按字典序打印出该字符串中字符的所有排列。例如输入字符串abc,则按字典序打印出由字符a,b,c所能排列出来的所有字符串abc,acb,bac,bca,cab和cba
#输入一个字符串,长度不超过9(可能有字符重复),字符只包括大小写字母

a="abcd"
a=list(a)
lens=len(a)

def StrSort(a):
    if len(a)==0:
        return []
    lista=[]
    for i in range(len(a)):
        if i>0 and a[i]==a[i-1]:
            continue

        temp=StrSort("".join(a[:i])+"".join(a[i+1:]))
        print(temp)
        for l in a:
            lista.append("".join(temp)+"".join(l))

    # print(lista)
    return lista

StrSort(a)



# class Solution:
#     def Permutation(self, ss):
#         # write code here
#         if len(ss)==0: return []
#         lst = list(ss)
#         lst.sort()
#         res = []
#         for i in range(0, len(ss)):
#             if i > 0 and lst[i]==lst[i-1]:
#                 continue
#             temp = self.Permutation(''.join(lst[:i]) + ''.join(lst[i+1:]))
#             if len(temp)==0:
#                 res.append(lst[i])
#             for str in temp:
#                 res.append(lst[i]+str)
#         return res
#
# ss = 'abcd'
# a = Solution()
# print(a.Permutation(ss))