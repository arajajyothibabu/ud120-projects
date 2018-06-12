#!/usr/bin/python

import pickle
import sys
import matplotlib.pyplot
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit


### read in data dictionary, convert to numpy array
data_dict = pickle.load( open("../final_project/final_project_dataset.pkl", "r") )
data_dict.pop('TOTAL') #removing outlier
features = ["salary", "bonus"]
data = featureFormat(data_dict, features)

from operator import itemgetter

#print data_dict
l = []
for key in data_dict.keys():
    d = data_dict[key]
    if d['bonus'] != 'NaN':
        d['jyothi'] = key
        l.append(d)

print sorted(l, key=itemgetter('bonus'), reverse=True)


### your code below
for point in data:
    salary = point[0]
    bonus = point[1]
    matplotlib.pyplot.scatter( salary, bonus )

matplotlib.pyplot.xlabel("salary")
matplotlib.pyplot.ylabel("bonus")
matplotlib.pyplot.show()


