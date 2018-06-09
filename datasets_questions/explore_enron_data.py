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
import fileinput

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

print enron_data

#persons
print len(enron_data)

#person properties
print len(enron_data[enron_data.keys()[0]].keys())

# How many POIs are there in the E+F dataset?
pois = len([enron_data[person]["poi"] for person in enron_data.keys() if enron_data[person]["poi"] == True])
print pois

poi_names = open("../final_project/poi_names.txt", "r")

print len(poi_names.readlines()[2:])

print enron_data["PRENTICE JAMES"]['total_stock_value']

print enron_data["COLWELL WESLEY"]['from_this_person_to_poi']

print enron_data["SKILLING JEFFREY K"]['exercised_stock_options']

print len([enron_data[person]["salary"] for person in enron_data.keys() if enron_data[person]["salary"] != 'NaN'])

print len([enron_data[person]["email_address"] for person in enron_data.keys() if enron_data[person]["email_address"] != 'NaN'])

print len([enron_data[person]["total_payments"] for person in enron_data.keys() if enron_data[person]["total_payments"] == 'NaN']) * 100 / len(enron_data)

print len([enron_data[person]["total_payments"] for person in enron_data.keys() if enron_data[person]["total_payments"] == 'NaN' and enron_data[person]["poi"] == True]) * 100 / pois

