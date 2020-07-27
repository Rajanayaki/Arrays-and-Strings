string=input()
hashMap={}
for i in range(len(string)):
  if string[i] not in hashMap:
    hashMap[string[i]]=1
  else:
    print("no")
    exit()
print("yes")
