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
import math 

#get email list
#execfile("../final_project/poi_email_addresses.py")

#get enron data
enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

# print(enron_data["SKILLING JEFFREY K"]["total_payments"])
# print(enron_data["LAY KENNETH L"]["total_payments"])
# print(enron_data["FASTOW ANDREW S"]["total_payments"])

print(enron_data["SKILLING JEFFREY K"])

nan_count =0;
total_count = 0;

for person_name in enron_data :
	#if(enron_data[person_name]["poi"] == True):
		total_count += 1
		if(str(enron_data[person_name]["total_payments"]) == "NaN"):
			nan_count +=1
	
print(nan_count)			
print(total_count)
print((float(nan_count)/total_count)*100)

# """

# true_poi = 0
# false_poi = 0
# for person_name in enron_data :
# 	poi_status = enron_data[person_name]['poi']
# 	if(poi_status == True):
# 		true_poi +=1
# 	else :
# 		false_poi +=1

# print("True POI : " + str(true_poi))
# print("False POI : " + str(false_poi))

# """
