import numpy as np
temp = []

def get_mssg(d):
    mssg = input("Enter message : ")
    key = input("Enter keyword : ")

    mssg = mssg.replace(" ","_")
    divisor = int( len(mssg) / len(key) ) + 1
    calc = len(key) * divisor - len(mssg)
    mssg = mssg + "_" * calc  if len(mssg) % len(key) != 0 else mssg

    mssg_matrix = np.array( list(mssg) ).reshape(-1,len(key)) if d ==0 else np.array( list(mssg) ).reshape(len(key),-1)
    if d != 0:
        mssg_matrix = np.transpose(mssg_matrix)
    print(mssg_matrix)
    return mssg,key,mssg_matrix           


def get_lst(myMssgMatrix):
    mssg_lst = []

    for j in range(len(myMssgMatrix[0])):   # j
        temp = []
        for i in range(len(myMssgMatrix)):  # i
            temp.append(myMssgMatrix[i][j])
    
        mssg_lst.append(temp)
    
    temp = []
    print(mssg_lst)
    return mssg_lst

def get_dict(myKey,mssg_lst,d):

    mssg_dict = {}
    if d == 0:
        for i in range(len(key)):
            mssg_dict[myKey[i]] = mssg_lst[i] 
    else:
        myKey = list(myKey)
        mykey_sorted = myKey.copy()
        mykey_sorted.sort()
        for i in range(len(key)):
            mssg_dict[mykey_sorted[i]] = mssg_lst[i] 
    print(mssg_dict)    
    return mssg_dict

def Final_MSSG(myMSSG,d):
    final_mssg = ""
    if d == 0:
        p = myMSSG
        q = myMSSG[0]
    else:
        p = myMSSG[0]
        q = myMSSG

    for i in range(len(p)):
        for j in range(len(q)):
            final_mssg += myMSSG[i][j] if d ==0 else myMSSG[j][i]
    return final_mssg


mssg,key,mssg_matrix = get_mssg(0)
mssg_lst = get_lst(mssg_matrix)
mssg_dict = get_dict(key,mssg_lst,0)
key_lst = list(key)
key_lst.sort()
encrypted_mssg_lst = [mssg_dict[i] for i in key_lst]
print(encrypted_mssg_lst)
encrypted_mssg = Final_MSSG(encrypted_mssg_lst,0)
encrypted_mssg = encrypted_mssg.replace("_"," ")
print(encrypted_mssg)

mssg,key,mssg_matrix = get_mssg(1)
mssg_lst = get_lst(mssg_matrix)
mssg_dict = get_dict(key,mssg_lst,1)
decrypted_mssg_lst = [mssg_dict[i] for i in key]
print(mssg_dict,decrypted_mssg_lst)
decrypted_mssg = Final_MSSG(decrypted_mssg_lst,1)
decrypted_mssg = decrypted_mssg.replace("_"," ")
print(decrypted_mssg)




            








