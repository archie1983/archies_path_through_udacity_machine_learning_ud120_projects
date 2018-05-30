#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

print "Number of people in dataset: ",len(enron_data)
#print "People's names: ",enron_data.keys()
print "Number of features per person: ",len(enron_data["CORDES WILLIAM R"])

pois = 0
for person, features in enron_data.iteritems():
    if features["poi"] == 1:
        pois += 1

print "Numner of POIs: ",pois

#print "Features of James Prentice: ",enron_data["PRENTICE JAMES"]
print "Total value of the stock belonging to James Prentice: ", enron_data["PRENTICE JAMES"]["total_stock_value"]
print "Number of email messages from Wesley Colwell to POIs: ", enron_data["COLWELL WESLEY"]["from_this_person_to_poi"]
print "Value of stock options exercised for Jeffrey K Skilling: ", enron_data["SKILLING JEFFREY K"]["exercised_stock_options"]
