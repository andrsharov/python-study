n = input()
s1 = int(n[1]) + int(n[2])
s2 = int(n[0]) + int(n[1])
if s1 > s2:
    print(s1, s2, sep="")
elif s1 < s2:
    print(s2, s1, sep="")
else:
    print(s1, s2, sep="")