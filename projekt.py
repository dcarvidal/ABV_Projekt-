from pylab import bar, title, xlabel, ylabel, figure
import numpy as np

         
def read2(filename, column):
    file= []
    f = list(open(filename))
    for line in f:
        line= line.strip().split(';')
        number = float(line[column])
        if number > 0:
            file.append(number)
    return file 

directoryn = '/Users/Daniel/Desktop/Projekt/names/' #Location of the babynames files
directorym = '/Users/Daniel/Desktop/Projekt/' #Location of the ‘Mortalitaet’ file

name = input('''Please write your name below:
''') +','
    
gender = ',' + input('''Please write your gender below (M or F):
''') + ','

count={}
drates= read2(directorym + 'Mortalitaet.txt', 2)

for year in range(2015-len(drates), 2015):
    filename = directoryn + 'yob{}.txt'.format(year)
    for line in open(filename):
        if name in line:
            if gender in line:
                a = line.strip().split(',')
                count['count{}'.format(year)] = int(a[2])
    
countvalues = [value for (key, value) in sorted(count.items(), reverse=True)]


if len(countvalues) == len(drates):
    
    a = np.array(countvalues)
    b = np.array(drates)    
    
    figure()

    x = list(range(len(drates)))
    y = list(map(int,list(a * b)))

    bar(x, y)

    name = name.strip(',')
    title('Estimate: People named ' + name + ' by Age in the U.S. (2014)')
    xlabel('Age')
    ylabel('Count')


    print('''Assuming all''', name + 's','''face the same death rate as the whole population. 
Data retrieved from https://www.ssa.gov/oact/STATS/table4c6.html''')

else: 
    print("Sorry, there is not enough data for " + name.strip(',') + 's')


