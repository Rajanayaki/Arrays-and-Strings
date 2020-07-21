string1=input()
string2=input()
if len(string1)!=len(string2):
  print("No")
  exit()
hashMap1={}
hashMap2={}
for i in range(len(string1)):
  if string1[i] not in hashMap1:
    hashMap1[string1[i]]=1
  else:
    hashMap1[string1[i]]+=1
for i in range(len(string2)):
  if string2[i] not in hashMap2:
    hashMap2[string2[i]]=1
  else:
    hashMap2[string2[i]]+=1
if hashMap1==hashMap2:
  print("yes")
else:
  print("No")
