import os , sys
file = list(open("name.txt",encoding = "utf-8"))
file1 = []
i = 0
while i < len(file):
    file1.append(file[i])
    i += 2        
file2 = []
for i in range(0,len(file1)):
    file2.append(file1[i].replace("\n",""))    
print(file2)    
path = "病毒图片"
files = []
for i in range(1,335):
    files.append("39298919_"+str(i)+".jpg")
for i in range(0,len(files)):
    os.rename(os.path.join(path,files[i]),os.path.join(path,file2[i]+".jpg"))



