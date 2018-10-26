# Problem
Editor needs statistics on immigration data, so we need to come up with a script that takes in immigration data from the Department of Labor, and output the following statistics:  

1.) Top 10 occupations  
2.) The number of H1b visa applicants that have been certified for each of (1)  
3.) What percentage of the total number of certified H1b applicants make up (2)  
**AND**  
4.) Top 10 states  
5.) The number of H1b visa applicants that have been certified for each of (4)  
6.) What percentage of the total number of certified H1b applicants make up (5)

1,2,3 will go in a text file called **top_10_occupations.txt**, located in ./output/top_10_occupations.txt. An example looks like this:
```
TOP_OCCUPATIONS;NUMBER_CERTIFIED_APPLICATIONS;PERCENTAGE
SOFTWARE DEVELOPERS, APPLICATIONS;6;60.0%
ACCOUNTANTS AND AUDITORS;1;10.0%
COMPUTER OCCUPATIONS, ALL OTHER;1;10.0% 
COMPUTER SYSTEMS ANALYST;1;10.0%
DATABASE ADMINISTRATORS;1;10.0%
```
4,5,6 will go in a text file called **top_10_states.txt**, located in ./output/top_10_states.txt. An example looks like this:
```
TOP_STATES;NUMBER_CERTIFIED_APPLICATIONS;PERCENTAGE
FL;2;20.0%
AL;1;10.0%
CA;1;10.0%
DE;1;10.0%
GA;1;10.0%
MD;1;10.0%
NJ;1;10.0%
TX;1;10.0%
WA;1;10.0%
```

# Approach

We will read in the csv file row by row and each time we encounter a certified H1b visa applicant, record the state and their occupation in the form of two dictionaries. One dictionary(called occupations_dictionary in the code) will use occupation as the key and map it to the total number of certified H1b visa applicants in that occupation. Similarly, the other dictionary(called states dictionary) will use the state abbreviation as the key and map it to the total number of ceritfied h1b visa applicants in that state. We also keep track of the total number of all certified h1b visa applicants regardless of occupation and state, so that we can calculate percentages later. To get the top 10 occupations and states, we must sort both our dictionaries first by the values. We first create a list of the keys for both dictionaries and then we can use .sort() and set the **key** parameter to a function that sorts the list of keys by value. For the state dictionary, if there is a tie in the value, we need to then sort alphabetically by state, so our function that is used for key parameter will sort by value first, and then by state.  

After sorting the list of keys for occupations and states, we will then the 10 largest occupations and states or all occupations and states in the list, whichever is smaller, and append the state/occupation to an array and it's dictionary value to another array. Then store the percentage of total number of certified applicants in another array by dividing the dictionary value by the total number of all certified h1b visa applicants, which we calculated earlier. Note: we round the percentage to 1 decimal place and store the percentage as a string, so that it follows the output format. 

Lastly, we just iterate through the 6 arrays we made(3 for occupations and 3 for states) and write each entry of each array into their respective files. 

**Technical Notes:**
O(N) storage, where N is the total number of unique occupations or states(whichever is larger)
Runtime is O(nlogn): which comes from sorting the dictionary keys

# How to Run
In order to run: One must run this in the terminal:
```/path/to/run.sh /path/to/h1b_counting.py /path/to/top_10_occupations.txt /path/to/top_10_states.txt```
Note: having the **top_10_occupations.txt** or **top_10_states.txt** already made is not required, the script will create a text file called the **top_10_occupations.tx** and **top_10_states.txt** in the directory you specified.
