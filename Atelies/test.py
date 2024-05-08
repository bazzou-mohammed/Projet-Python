
from unittest import TestCase
from main import add
import pytest
from random import choice
from tinydb import TinyDB, Query, where


db = TinyDB('data.json', indent =4)
db.insert({"name":"Patrick", "score":0})
print(db.all())
db.insert_multiple([{"name":"Julie", "score":50}, 
                    {"name":"paul", "score":56}])
print(db.all())
# # User = Query()
# # patrick_list = db.search(User.name == "Patrick")
# # print(patrick_list)
# # patrick_unique = db.get(User.name == "Patrick")
# # print(patrick_unique)
# # print(db.all())

# # high_scores = db.search(where("score")>50)
# # print(high_scores)

# db.update({"score":17}, where ('name')=='Patrick')

# db.update({"role":["Junior"]})
# db.remove()

import subprocess

# result = subprocess.run(['cd C:\\'],shell = True,capture_output=True,text=True)
# print(result.stdout)

# filename = 'exmple.txt'
# subprocess.run(['touch', filename])

# with open('output.txt', 'w') as output_file:
#     subprocess.run(['echo', 'Hello worrld' ], stdout=output_file)

# try:
#     subprocess.run(['cat', 'nonexistentfile.txt'], check=True)
# except subprocess.CalledProcessError as e:
#     print(f"Error: {e}")
import datetime 
import random
#list
# start_time = datetime.datetime.now()
# rand_elem = random.sample(range(0, 1000), 1000)
# list_seq = list(range(1000))
# counter = 0
# for ele in rand_elem:
#     if ele in list_seq:
#         counter+=1
# end_time = datetime.datetime.now()
# print(end_time-start_time)

#set
start_time = datetime.datetime.now()
rand_elem = random.sample(range(0, 1000), 1000)
list_seq = set(range(1000))
counter = 0
for ele in rand_elem:
    if ele in list_seq:
        counter+=1
end_time = datetime.datetime.now()
print(end_time-start_time)