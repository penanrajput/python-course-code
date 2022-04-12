data = open("csv_data.txt",'r')
lines = data.readlines()
data.close()

data = open("csv_data.txt",'r')
lines = data.readlines()
data.close()
lines = [line.strip() for line in lines[1:]]

for line in lines:
    person_data = line.split(',')
    No = person_data[0]
    Days = person_data[1]
    Languages = person_data[2]
    Progress = person_data[3]
    print(f'{No},"|",{Days},"|",{Languages},"|",{Progress}.' )

