#!/usr/bin/python

import pickle
import numpy
numpy.random.seed(42)


### The words (features) and authors (labels), already largely processed.
### These files should have been created from the previous (Lesson 10)
### mini-project.
words_file = "../text_learning/your_word_data.pkl" 
authors_file = "../text_learning/your_email_authors.pkl"
word_data = pickle.load( open(words_file, "r"))
authors = pickle.load( open(authors_file, "r") )



### test_size is the percentage of events assigned to the test set (the
### remainder go into training)
### feature matrices changed to dense representations for compatibility with
### classifier functions in versions 0.15.2 and earlier
from sklearn import cross_validation
features_train, features_test, labels_train, labels_test = cross_validation.train_test_split(word_data, authors, test_size=0.1, random_state=42)
#print features_train
## AE: At this point features_train is a set of stemmed, but still readable emails.

from sklearn.feature_extraction.text import TfidfVectorizer
vectorizer = TfidfVectorizer(sublinear_tf=True, max_df=0.5,
                             stop_words='english')
features_train = vectorizer.fit_transform(features_train)
features_test  = vectorizer.transform(features_test)
## AE: Now we have trained the TFIDF vectoriser with a full set of training data (~90% of all emails)
## AE: This vectoriser now has all the features, that could be gotten from 90% of all emails (that's a lot of words)
## AE: But "features_train" now contains vectorised (transformed) emails-- ALL of them.


#print features_train[:150]
### a classic way to overfit is to use a small number
### of data points and a large number of features;
### train on only 150 events to put ourselves in this regime
###
### #AE: Now we're taking only first 150 emails from the full training set (they're all vectorised at this point, btw).
### #AE: And correspondingly first 150 labels.
features_train = features_train[:150].toarray()
labels_train   = labels_train[:150]



### your code goes here
# Creating and overfitting a decision tree classifier
### AE: We are now training a DecisionTreeClassifier with the limited number (150) of vectorised emails
from sklearn import tree
clf = tree.DecisionTreeClassifier()
clf.fit(features_train, labels_train)

# printing out accuracy of the overfit decision tree classifier
from sklearn.metrics import accuracy_score
acc = accuracy_score(clf.predict(features_test), labels_test)
print "Accuracy of overfitted decision tree: ",acc

# going through feature_importances_ attribute and printing out all words, that are with
# importance of 0.2 or greater
### AE: The words, that appear often, will, of course, be present in almost each email and therefore
### we should have had them in the first 150 emails. We'll get the index of the most important feature
### (word) from these 150 emails.
i = 0
offending_importance_index = 0
for importance in clf.feature_importances_:
    if importance > 0.2: 
        print "coefficient: ",i," : ",importance
        offending_importance_index = i
    i += 1

# finding and printing out the feature (word) with the highest importance
### AE: And now we'll look up this most important word in the full set of features of a vectoriser,
### that is still fitted with the full set of emails.
print "offending feature (word): ",vectorizer.get_feature_names()[offending_importance_index]
