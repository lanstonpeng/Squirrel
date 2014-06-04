import pdb
S = "rabbbit"
T = "rabbit"
result = []
def combination(s,n):
    temp = ""
    for i in range(1,len(s)):
        temp = temp + combination(s[i:],n - i)
    if n == 0:
        result.append(temp)
        return ""
    else:
        return temp

t = []
r = []
def combination2(start,end):
    #pdb.set_trace()
    if start == end:
        r.append("".join(t))
        return
    for i in range(start,end):
        t.append(S[i])
        combination2(start + 1,end)
        t.pop()


#combination(S,len(S) - 1)
combination2(0,len(S))
print r



