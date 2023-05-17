import random
msg=input("Enter message: ")
og_msg=list(msg)
flag=random.choice(msg)

new_msg=[flag]
for i in range (len(msg)):
    new_msg.append(og_msg[i])
if flag in new_msg:
    x=og_msg.index(flag)
    new_msg.insert(x+1,flag)
new_msg.append(flag)
stuffed=''.join(new_msg)
print(stuffed)

flag=stuffed[0]
destuff=[]
i=1
while i<len(stuffed)-1:
    if stuffed[i]==flag:
        i+=1
    destuff.append(stuffed[i])
    i+=1
OP=''.join(destuff)
print(OP)