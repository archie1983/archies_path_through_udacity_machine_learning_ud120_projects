#!/usr/bin/python


"""
    Starter code for the evaluation mini-project.
    Start by copying your trained/tested POI identifier from
    that which you built in the validation mini-project.

    This is the second step toward building your POI identifier!

    Start by loading/formatting the data...
"""

import pickle
import sys
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit

data_dict = pickle.load(open("../final_project/final_project_dataset.pkl", "r") )

### add more features to features_list!
features_list = ["poi", "salary"]

data = featureFormat(data_dict, features_list)
labels, features = targetFeatureSplit(data)



### your code goes here 
# Conditioning data into test and training sets
from sklearn.model_selection import train_test_split
train_features, test_features, train_labels, test_labels = train_test_split(features, labels, test_size=0.3, random_state=42)

# Importing SKlearn tree classifier and fitting
from sklearn import tree
clf = tree.DecisionTreeClassifier()
clf.fit(train_features, train_labels)

# Importing SKlearn metrics to calculate accuracy
from sklearn.metrics import accuracy_score
acc = accuracy_score(test_labels, clf.predict(test_features))
print "Accuracy of a non-overfitted tree: ",acc

pois_in_test_set = clf.predict(test_features)

import numpy
unique, counts = numpy.unique(pois_in_test_set, return_counts=True)
ucounts = dict(zip(unique, counts))

print "Predicted POIs in test set: ",ucounts[1.0]
print "Total number of people predicted in set: ",len(pois_in_test_set)

print "POIs in test labels: ",test_labels.count(1)
print "Non POIs in test labels: ",test_labels.count(0)
acc_if_0 = (len(test_labels) - test_labels.count(1)) * 1.0 / len(test_labels)
print "If my classifier predicted 0 (Non-POI) in all cases, it's accuracy would be (correct predictions / total predictions): ",acc_if_0
