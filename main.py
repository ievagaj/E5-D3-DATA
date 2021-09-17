#open file#
f = open('users.dat')
#print("opened")
data = f.readlines()
#print("All the data copied to the data object")
f.close()
#print('closed')

#Now we operate with the data from data object

print(type(data))

#print(data[0]), data[4])

for i in data:
  print(i.split(";")[1].split('\n')[0].lstrip())
