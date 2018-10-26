#!/usr/bin/env python
import csv
import sys


def sort_by_value_for_occupations_dictionary(key):
    '''
    Sorting function SPECIFICALLY for occupations_dictionary.
    Sorts by number of certified applicants.
    '''
    return occupations_dictionary[key]

def sort_by_value_for_state_dictionary(key):
    '''
    Sorting function SPECIFICALLY for states_dictionary.
    Sorts by number of certified applicants first, then alphabetically by state.
    '''
    return (state_dictionary[key], key)


def calculate_h1b_statistics(path_to_csvfile, path_to_occupationsfile, path_to_statesfile):
    '''
    Calculates h1b Visa statistics and write them to text files(details on Github).
    '''
    occupations_dictionary = {} #stores the number of certified applicants for each occupation
    state_dictionary = {} #stores the number of certified applicants for each state
    total_number_of_certified_occupants = 0.0 
    fname = path_to_csvfile
    
    with open(fname) as csvfile:
        reader = csv.DictReader(csvfile, delimiter=';')
        header = reader.fieldnames
        if "STATUS" in header:
            #Files provided by Department of Labor uses these header names
            header = ['STATUS', 'LCA_CASE_SOC_NAME', 'WORKSITE_STATE']
        else:
            #Files provided by Insight uses these header names. 
            header = ['CASE_STATUS', 'SOC_NAME', 'WORKSITE_STATE']
        for row in reader:
            if row[header[0]] == 'CERTIFIED':
                total_number_of_certified_occupants += 1 #increment count of total certified applicants
                #make appropriate occupation dictionary addition
                if row[header[1]] not in occupations_dictionary:
                    occupations_dictionary[row[header[1]]] = 1 
                else:
                    occupations_dictionary[row[header[1]]] += 1
                #make appropriate state dictionary addition
                if row[header[2]] not in state_dictionary:
                    state_dictionary[row[header[2]]] = 1
                else:
                    state_dictionary[row[header[2]]] += 1
    keylist_occupations = occupations_dictionary.keys() #list of keys i.e list of unique occupations
    #sort keys by number of applicants first, then alphabetically
    keylist_occupations.sort(reverse=True, key=sort_by_value_for_occupations_dictionary)
    
    keylist_states = state_dictionary.keys() #list of keys i.e list of unique states
    #sort keys by number of applicants first, then alphabetically
    keylist_states.sort(reverse = True, key=sort_by_value_for_state_dictionary)
    
    top_10_occupations = [] #top 10 occupations with the most number of certified h1b visa applicants
    top_10_occupations_number_of_certified_applicants = [] #the number of certified applicants for each top 10 occupation
    top_10_occupations_percentages = [] #percentage each top 10 occupation make up of all certified h1b visa applicants
    
    top_10_states = [] #top 10 states with the most number of certified h1b visa applicants
    top_10_states_number_of_certified_applicants = [] #the number of certified applicants for each top 10 state
    top_10_states_percentages = [] #percentage each top 10 state make up of all certified h1b visa applicants
    if len(keylist_occupations) > 10:
        #if there are more 10 unique occupations, then add top 10 to appropriate array
        for i in range(10):
            top_10_occupations.append(keylist_occupations[i])
            top_10_occupations_number_of_certified_applicants.append(occupations_dictionary[keylist_occupations[i]])
            top_10_occupations_percentages.append(str(round(100*(occupations_dictionary[keylist_occupations[i]]/total_number_of_certified_occupants), 1))+'%')
    else:
        #else, add top occupation information to appropriate array
        for occupation in keylist_occupations:
            top_10_occupations.append(occupation)
            top_10_occupations_number_of_certified_applicants.append(occupations_dictionary[occupation])
            top_10_occupations_percentages.append(str(round(100*(occupations_dictionary[occupation]/total_number_of_certified_occupants), 1))+'%')
    if len(keylist_states) > 10:
        #if there are more 10 unique states, then add top 10 to appropriate array
        for i in range(10):
            top_10_states.append(keylist_states[i])
            top_10_states_number_of_certified_applicants.append(state_dictionary[keylist_states[i]])
            top_10_states_percentages.append(str(round(100*(state_dictionary[keylist_states[i]]/total_number_of_certified_occupants), 1))+'%')
    else:
        #else, add top state information to appropriate array
        for state in keylist_states:
            top_10_states.append(state)
            top_10_states_number_of_certified_applicants.append(state_dictionary[state])
            top_10_states_percentages.append(str(round(100*(state_dictionary[state]/total_number_of_certified_occupants), 1))+'%')
    #write to top_10_occupations.txt
    f= open(path_to_occupationsfile, "w+")
    f.write("TOP_OCCUPATIONS;NUMBER_CERTIFIED_APPLICATIONS;PERCENTAGE\n")
    for i in range(len(top_10_occupations)):
        f.write("%s;%d;%s\n" % (top_10_occupations[i], top_10_occupations_number_of_certified_applicants[i], top_10_occupations_percentages[i]))
    f.close()
    
    #write to top_10_state.txt
    f2 = open(path_to_statesfile, "w+")
    f2.write("TOP_STATES;NUMBER_CERTIFIED_APPLICATIONS;PERCENTAGE\n")
    for i in range(len(top_10_states)):
        f2.write("%s;%d;%s\n" % (top_10_states[i], top_10_states_number_of_certified_applicants[i], top_10_states_percentages[i]))
    f2.close()
    
calculate_h1b_statistics(sys.argv[1], sys.argv[2], sys.argv[3])
        
        
