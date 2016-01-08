# imports modules and reads in dataframe
import numpy
import csv
file = open('geotweets.csv')
data = csv.reader(file)

data2 = [x for x in data if x != []]

#Create empty lists to append data to
x = []
y = []

#Loop to pull out coords, appending them to an empty list as floats
#The items are also stripped of unwanted characters such as brackets and commas
for row in data2:
    items = row[2].split()
    if (len(items) != 0) and (items[3][1:-1] != "type'"):
        x.append(float(items[3][1:-1]))
        y.append(float(items[4][:-2]))


#Convert lists into arrays
array_x = numpy.asarray(x)
array_y = numpy.asarray(y)


#Merge the x and y coordinate arrays
data = numpy.array([array_x, array_y])


#Transpose so that each coordinate has its own column
data = data.transpose()

print(data)

#Write out the merged array
numpy.savetxt('coords.txt', data)

# check where date and time is
time = []

for row in data2:
    items = row[0].split()
    items_lat = row[2].split()
    if (len(items) != 0) and (items_lat[3][1:-1] != "type'"):
        time.append(items[1])


# check that time has done what we wanted it to
print(time[1:10])

# firstly you need to create a file called time in the command line using
# touch time.txt

# this part saves each item in list time to time.txt and then starts a new line in that text file
dataFile = open('time.txt', 'w')

for item in time:
    dataFile.write(str(item) + '\n')

dataFile.close()

# checking that length time = length x and length y
assert(len(time) == len(x))

