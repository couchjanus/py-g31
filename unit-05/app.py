# files

# try:
#     file_hendler = open('data.txt', 'a')
#     added = 'some data to be written to the file'
#     file_hendler.write(added)
#     file_hendler.close()
# except FileNotFoundError:
#     pass
file_name = 'data.txt'

with open(file_name, 'r+') as file_hendler:
    added = '\nsome data to be written to the file\n'
    file_hendler.write(added)
    
    # for line in file_hendler:
    #     print(line)
    test = file_hendler.readlines()
    # text = file_hendler.readline()
    # print(text)
    
# print(test)

def search_str(file, word):
    with open(file) as fh:
        content = fh.read()
        if word in content:
            print(f'String {word} exist in the file')
        else: print(f'String {word} does not exist in the file')
        
search_str('sale.txt', 'laptop')

with open('sale.txt', 'r+') as f:
    file = f.readlines()
    for line in file:
        if 'mobile 20' in line:
            pos = file.index('mobile 20\n')
            # print(pos)
            file.insert(pos+1, 'USB 39\n')
            break
    f.seek(0)
    f.writelines(file)
    
import pickle

my_object = {"first": "a", "second": 2, "third": [1, 2, 3]}
my_pickled_object = pickle.dumps(my_object)  # Pickling the object
print(f"This is my pickled object:\n{my_pickled_object}\n")

my_unpickled_object = pickle.loads(my_pickled_object)  # Unpickling the object
print(f"This is a_dict of the unpickled object:\n{my_unpickled_object}\n")

list_of_dicts = [
   {"first": "a", "second": 2, "third": [1, 2, 3]},
   {"first": "b", "second": 3, "third": [2, 2, 3]},
   {"first": "c", "second": 4, "third": [3, 2, 3]}
]
# list_pickled_object = pickle.dumps(list_of_dicts)  # Pickling the object
# print(f"This is my pickled object:\n{list_pickled_object}\n")
# list_unpickled_object = pickle.loads(list_pickled_object)  # Unpickling the object
# print( f"This is a_dict of the unpickled object:\n{list_unpickled_object[1]}\n")

with open('db.pkl', 'wb') as output:
    pickle.dump(list_of_dicts, output)

# Read the data
#Open existing
list_unpickled = []
with open('db.pkl', 'rb') as file:
    list_unpickled = pickle.load(file)

print(f"This is list_unpickled of the unpickled object:\n{list_unpickled}\n")