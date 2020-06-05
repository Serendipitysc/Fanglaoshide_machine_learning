import csv


def odd_generator(n):
    list = []
    for i in range(n):
        if (i%2 == 1):
            list.append(i)
    print(list)


def read_sort_byfirst_csv():
    list = []
    with open('students.csv') as csvfile:
        readCSV = csv.reader(csvfile)
        for row in readCSV:
            list.append(row)
        list.sort()
    print(list)


def read_sort_byage_csv():
    list = []
    with open('students.csv') as csvfile:
        readCSV = csv.reader(csvfile)
        for row in readCSV:
            row[1] = int(row[1])
            list.append(row)
    list.sort(key = lambda row: row[1])
    print(list)

def freq_char(string):
    freq = {}
    for i in string:
        if i in freq:
            freq[i]+=1
        else:
            freq[i] = 1
    print(freq)
    print(max(freq, key = freq.get))



#Part 1:


#1
#odd_generator(10)


#2a
#read_sort_byfirst_csv()

#2b
#read_sort_byage_csv()


#3
#freq_char("fdsfasdfdasfa")

