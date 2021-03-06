#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 1 (Naive Bayes) mini-project. 

    Use a Naive Bayes Classifier to identify emails by their authors
    
    authors and labels:
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()

#print features_train[0][0:100], features_test[0][0:100], labels_train, labels_test



#########################################################
### your code goes here ###

# Creating and training a classifier
from sklearn.naive_bayes import GaussianNB
clf = GaussianNB()

# timing the training and then training
t0 = time()
clf.fit(features_train, labels_train)
print "training time:", round(time()-t0, 3), "s"

# creating a prediction vector for the test set and timing it
t0 = time()
pred = clf.predict(features_test)
print "prediction time:", round(time()-t0, 3), "s"

from sklearn.metrics import accuracy_score

# comparing the prediction vector with an accurate real answers vector
accuracy = accuracy_score(labels_test, pred)

print "Accuracy: "+str(accuracy)

#########################################################
