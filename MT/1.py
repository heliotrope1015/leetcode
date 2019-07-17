# s=raw_input()
# t=raw_input()
# print s,t
s="aA?a?fds"
t="Aa"

begin=0
position=0
root=0
count=0
while position<len(s):
    if s[position]!=t[root] and s[position]!='?':
        position=begin+1
        begin=position
        root=0
    elif root==len(t)-1:
        count+=1
        position=begin+1
        begin=position
        root=0
    else:
        position+=1
        root+=1

print count

