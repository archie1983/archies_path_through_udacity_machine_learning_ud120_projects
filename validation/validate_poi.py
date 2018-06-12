#!/usr/bin/python


"""
    Starter code for the validation mini-project.
    The first step toward building your POI identifier!

    Start by loading/formatting the data

    After that, it's not our code anymore--it's yours!
"""

import pickle
import sys
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit

data_dict = pickle.load(open("../final_project/final_project_dataset.pkl", "r") )

### first element is our labels, any added elements are predictor
### features. Keep this the same for the mini-project, but you'll
### have a different feature list when you do the final project.
features_list = ["poi", "salary"]

data = featureFormat(data_dict, features_list)
labels, features = targetFeatureSplit(data)



### it's all yours from here forward!  

# importing and creating a DecisionTreeClassifier
from sklearn import tree
clf = tree.DecisionTreeClassifier()
clf.fit(features, labels)

# importing accuracy score and checking the accuracy of the decision tree (should be 100% because it's checked on training data)
from sklearn.metrics import accuracy_score
acc = accuracy_score(labels, clf.predict(features))
print "Accuracy of an overfitted tree: ",acc

# Now we will do better-- we will split the data into training and test sets and work with that
from sklearn.model_selection import train_test_split
train_features, test_features, train_labels, test_labels = train_test_split(features, labels, test_size=0.3, random_state=42)
clf.fit(train_features, train_labels)

pois_in_test_set = clf.predict(test_features)

acc = accuracy_score(test_labels, pois_in_test_set)
print "Accuracy of a non-overfitted tree",acc

import numpy
unique, counts = numpy.unique(pois_in_test_set, return_counts=True)
ucounts = dict(zip(unique, counts))

print "POIs in test set: ",ucounts[1.0]
