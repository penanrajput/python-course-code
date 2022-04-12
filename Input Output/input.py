data = open("csv_data.txt",'r')
lines = data.readlines()
print(lines)
data.close()
# ['No,Days,Languages,Progress\n', '1,21-12-2018,C++,Completed\n', '2,22-12-2018,Java,Completed\n', '3,23-12-2018,SQL,Completed\n', '4,24-12-2018,Python,Completed\n', '5,25-12-2018,JavaScript,Completed\n', '6,26-12-2018,R,Ongoing\n', '7,27-12-2018,Ruby,-\n', '8,28-12-2018,Github,-']

data = open("csv_data.txt",'r')
lines = data.readlines()
data.close()
print(lines[1:])
data = open("csv_data.txt",'r')
lines = data.readlines()
data.close()
lines = [line.strip() for line in lines[1:]]