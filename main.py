# read first line of file
file = open('file.txt', 'r')
print("reading fisrt line...")
print(file.readline())
file.close()

# read first three lines of file
file = open('file.txt', 'r')
print("Reading muliple lines...")
print(file.readline())
print(file.readline())
print(file.readline())
file.close()

#looping through all the lines of the file
file = open('file.txt', 'r')
print("looping through the line...")
for line in file
print(line)
file.close() 