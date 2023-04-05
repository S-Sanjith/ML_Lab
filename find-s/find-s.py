# import csv

# def updateHypothesis(x, h):
#     if h == []:
#         return x
#     for i in range(0, len(h)):
#         if x[i].upper() != h[i].upper():
#             h[i] = '?'
#     return h

# if __name__ == '__main__':
#     data = []
#     h = []

#     #read csv file
#     with open('enjoysport.csv', 'r') as file:
#         reader = csv.reader(file)
#         print('Data:')
#         for row in reader:
#             data.append(row)
#             print(row)

#     if data:
#         for x in data:
#             if x[-1].upper() == 'YES':x.pop()
#             h = updateHypothesis(x, h)

#     print('\nHypothesis: ', h)

import csv
a = []
with open('enjoysport.csv', 'r') as csvfile:
    for row in csv.reader(csvfile):
        a.append(row)
    print(a)

print("\n The total number of training instances are : ",len(a))
num_attribute = len(a[0])-1
print("\n The initial hypothesis is : ")
hypothesis = ['0']*num_attribute
print(hypothesis)
for i in range(0, len(a)):
    if a[i][num_attribute] == 'yes':
        for j in range(0, num_attribute):
            if hypothesis[j] == '0' or hypothesis[j] == a[i][j]:
                hypothesis[j] = a[i][j]
            else:
                hypothesis[j] = '?'
    print("\n The hypothesis for the training instance {} is : \n" .format(i+1),hypothesis)

print("\n The Maximally specific hypothesis for the training instance is ")
print(hypothesis)
