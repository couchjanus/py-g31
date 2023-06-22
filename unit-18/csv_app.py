# 
import csv

with open('users.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    field = ['name', 'age', 'country']
    
    writer.writerow(field)
    writer.writerow(['John Doe', '32', 'USA'])
    writer.writerow(['Mary Ann', '18', 'GB'])
    writer.writerow(['Oksana Karpenko', '17', 'Ukraine'])


# with open('users.csv', 'w', newline='') as f:
#     writer = csv.writer(f)
    
#     row_list = [    
#         ['name', 'age', 'country'],
#         ['John Doe', '32', 'USA'],
#         ['Mary Ann', '18', 'GB'],
#         ['Oksana Karpenko', '17', 'Ukraine']
#     ]
    
#     writer.writerow(row_list)
    
mydict = [
    {'name':'John Doe', 'age':'32', 'country':'USA'},
    {'name':'Mary Ann', 'age':'18', 'country':'GB'},
    {'name':'Oksana Karpenko', 'age':'17', 'country':'Ukraine'}
]
field = ['name', 'age', 'country']
with open('user.txt', 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames= field)
    writer.writeheader()

with open('users.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
