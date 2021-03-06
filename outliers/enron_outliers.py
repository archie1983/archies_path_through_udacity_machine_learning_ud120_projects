#!/usr/bin/python

import pickle
import sys
import matplotlib.pyplot
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit


### read in data dictionary, convert to numpy array
data_dict = pickle.load( open("../final_project/final_project_dataset.pkl", "r") )
features = ["salary", "bonus"]

# we need to remove the "total" outlier
data_dict.pop("TOTAL", 0)

data = featureFormat(data_dict, features)
keys = data_dict.keys()

### your code below
#print data_dict
i = 0
for key,val in data_dict.items():
    if (val['salary'] > 1000000 and val['salary'] != "NaN"): print key,":s:",val['salary'],":b:",val['bonus']

for point in data:
    salary = point[0]
    bonus = point[1]
    matplotlib.pyplot.scatter( salary, bonus )

matplotlib.pyplot.xlabel("salary")
matplotlib.pyplot.ylabel("bonus")
matplotlib.pyplot.show()


