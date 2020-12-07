import csv
total=0
mil=0
hot=0
med=0
s=0
toppings=0
burritos=0
soda=[]
chips={}
with open('chipotle.tsv') as f:
     file_nested_list = [row for row in csv.reader(f, delimiter='\t')]
     header= file_nested_list[0]
     data=file_nested_list[1:]
num=len(set(row[0]for row in data))
for row in data:
    s+=float(row[4][1:])
avg=s/float(num-1)
print(round(avg,3))
for row in data:
    if 'Canned' in row[2]:
        soda.append(row[3][1:-1])
soda_list=set(soda)
print(soda_list)
for row in data:
    if("Burrito" in row[2] ):
        burritos+=1
        toppings+=row[3].count(',')+1
print(round((toppings/burritos),3))
for row in data:
    if 'Chips' in row[2]:
        if row[2] not in chips:
            chips[row[2]] = int(row[1])
        else:
            chips[row[2]] += int(row[1])    
print(chips)
print(type(chips))
#Bonus(Hot/Mild/Medium percentage)
for row in data: 
    if "Medium" in  row[3]:
        med+=1
    if "Hot" in row[3]:
        hot+=1
    if "Mild" in row[3]:
        mil+=1
total=med+mil+hot
medprc=med/total
milprc=mil/total
hotprc=hot/total
print("The mild salsa, medium salsa, hot salsa percentages are:%f1,%f2,%f3 " %(milprc,medprc,hotprc))
        
    
        