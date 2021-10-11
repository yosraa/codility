from datetime import datetime
f = open("demo.txt", "r")
input_data = f.read()
i = 0
photos = []
data = {}
photo_slice = input_data.split('\n')
for element in photo_slice:

  row= element.split(',')
  key = row[1].lstrip() 
  if  key not in data:
                
        data[key] = [[i,row[0].lstrip(),row[1].lstrip(),datetime.strptime(row[2].lstrip(), '%Y-%m-%d %H:%M:%S'),row[0].split(".")[-1]]]
        i = i+1 
  else:
        data[key].append([i,row[0].lstrip(),row[1].lstrip(),datetime.strptime(row[2].lstrip(), '%Y-%m-%d %H:%M:%S'),row[0].split(".")[-1]])
        i = i+1

#sorted by date

for k, v in data.items():
    v.sort(key=lambda x:x[3])
    data[k]=v

new_list = []
for k, v in data.items():
    x =1
    for i in v:
        pWidth = len(str(len(v)))
        psequence = x
        x=x+1
        new_list.append([i[0],psequence,i[2],i[3],pWidth,i[4]])
# sorted by ID 
new_list.sort(key=lambda x:x[0])
strings =''
for row in new_list:
    updated_name = row[2]+str(row[1]).zfill(row[4])+'.'+str(row[5])
    strings+= updated_name +"\n"    

fichier = open("output.txt", "a")
fichier.write(strings)
fichier.close()        