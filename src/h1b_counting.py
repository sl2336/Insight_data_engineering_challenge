#!/usr/bin/env python
import csv
import sys

#SOC_NAME = occupation name
#if case status = CERTIFIED add to number of people in that occupation
# percentage = need to keep track of total number of certified applicants

occupations_dictionary = {}
state_dictionary = {}
total_number_of_certified_occupants = 0.0
fname = sys.argv[1]

def sort_by_value_for_occupations_dictionary(key):
    return occupations_dictionary[key]
def sort_by_value_for_state_dictionary(key):
    return state_dictionary[key]

with open(fname) as csvfile:
    reader = csv.DictReader(csvfile, delimiter=';')
    header = reader.next()
    if "STATUS" in header:
        header = ['STATUS', 'LCA_CASE_SOC_NAME', 'LCA_CASE_EMPLOYER_STATE']
    else:
        header = ['CASE_STATUS', 'SOC_NAME', 'EMPLOYER_STATE']
    for row in reader:
        if row[header[0]] == 'CERTIFIED':
            total_number_of_certified_occupants += 1
            if row[header[1]] not in occupations_dictionary:
                occupations_dictionary[row[header[1]]] = 1
            else:
                occupations_dictionary[row[header[1]]] += 1
            if row[header[2]] not in state_dictionary:
                state_dictionary[row[header[2]]] = 1
            else:
                state_dictionary[row[header[2]]] += 1
keylist_occupations = occupations_dictionary.keys()
keylist_occupations.sort(reverse=True, key=sort_by_value_for_occupations_dictionary)

keylist_states = state_dictionary.keys()
keylist_states.sort(reverse = True, key=sort_by_value_for_state_dictionary)

top_10_occupations = []
top_10_occupations_number_of_certified_applicants = []
top_10_occupations_percentages = []

top_10_states = []
top_10_states_number_of_certified_applicants = []
top_10_states_percentages = []
if len(keylist_occupations) > 10:
    for i in range(10):
        top_10_occupations.append(keylist_occupations[i])
        top_10_occupations_number_of_certified_applicants.append(occupations_dictionary[keylist_occupations[i]])
        top_10_occupations_percentages.append(str(round(100*(occupations_dictionary[keylist_occupations[i]]/total_number_of_certified_occupants), 1))+'%')
else:
    for occupation in keylist_occupations:
        top_10_occupations.append(occupation)
        top_10_occupations_number_of_certified_applicants.append(occupations_dictionary[occupation])
        top_10_occupations_percentages.append(str(round(100*(occupations_dictionary[keylist_occupations[i]]/total_number_of_certified_occupants), 1))+'%')
if len(keylist_states) > 10:
    for i in range(10):
        top_10_states.append(keylist_states[i])
        top_10_states_number_of_certified_applicants.append(state_dictionary[keylist_states[i]])
        top_10_states_percentages.append(str(round(100*(state_dictionary[keylist_states[i]]/total_number_of_certified_occupants), 1))+'%')
else:
    for state in keylist_states:
        top_10_states.append(state)
        top_10_occupations_number_of_certified_applicants.append(state_dictionary[state])
        top_10_occupations_percentages.append(str(round(100*(state_dictionary[state]/total_number_of_certified_occupants), 1))+'%')

f= open(sys.argv[2], "w+")
f.write("TOP_OCCUPATIONS;NUMBER_CERTIFIED_APPLICATIONS;PERCENTAGE\n")
for i in range(len(top_10_occupations)):
    f.write("%s;%d;%s\n" % (top_10_occupations[i], top_10_occupations_number_of_certified_applicants[i], top_10_occupations_percentages[i]))
f.close()

f2 = open(sys.argv[3], "w+")
f2.write("TOP_STATES;NUMBER_CERTIFIED_APPLICATIONS;PERCENTAGE\n")
for i in range(len(top_10_states)):
    f2.write("%s;%d;%s\n" % (top_10_states[i], top_10_states_number_of_certified_applicants[i], top_10_states_percentages[i]))
f2.close()
        
        
