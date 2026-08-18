# 1、外层循环i:0-len-1
# 2、内层循环0-i
# 3、两数比较，更大的放后面

s = [12, 5, -3, 10, 6]
for i in range(len(s)):
    for j in range(i):
        if s[j] > s[i]:
            s[j],s[i] = s[i],s[j]
print(s)