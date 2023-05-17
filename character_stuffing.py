#character stuffing
import random
message=input("Enter the message: ")
og_message=list(message)
flag = random.choice(message)

new_message=[flag]
for i in range(len(message)):
  new_message.append(og_message[i])
if flag in new_message:
    x = og_message.index(flag)
    new_message.insert(x+1, flag)

new_message.append(flag)
stuffed_message=''.join(new_message)
print("stuffed message is ",stuffed_message)

flag = stuffed_message[0]
destuffed_message = []
i = 1
    
while i < len(stuffed_message) - 1:
    if stuffed_message[i] == flag:
        i += 1
    destuffed_message.append(stuffed_message[i])
    i += 1
OP=''.join(destuffed_message)
print("destuffed message is ",OP)