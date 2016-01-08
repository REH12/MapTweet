
# coding: utf-8

# In[77]:

# imports modules and reads in dataframe
import numpy
import csv
file = open('geotweets.csv')
data = csv.reader(file)

data2 = [x for x in data if x != []]


# In[79]:

x = []
y = []

for row in data2:
    items = row[2].split()
    if (len(items) != 0) and (items[3][1:-1] != "type'"):
        x.append(float(items[3][1:-1]))
        y.append(float(items[4][:-2]))
        


# In[80]:

array_x = numpy.asarray(x)
array_y = numpy.asarray(y)


# In[81]:

data = numpy.array([array_x, array_y])


# In[82]:

data = data.transpose()


# In[83]:

print(data)


# In[84]:

numpy.savetxt('coords.txt', data)


# In[ ]:

# check where date and time is
for row in data2:
    items = row[2].split()
    if (len(items) != 0) and (items[3][1:-1] != "type'"):
        x.append(float(items[3][1:-1]))
        y.append(float(items[4][:-2]))

