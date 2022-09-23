# Election Audit Analysis

## Overview of Election Audit

This analysis uses Python to perform the task of auditing election results for certain Colorado counties and returns a summarized report. Python opens and reads a .csv file containing data on the ballot id, the county where the vote was cast and the candidate the vote was for and using looping obtains the total amounts of votes by county and for each candidate. Lastly the summarized report is exported to a .txt file for ease of access.

## Election Audit Analysis and Results
### Analysis

To start the analysis, two list variables were created, `candidate_options` and `county_list`, to hold each unique candidate and county respectively. Additionally two empty dictionaries were initialized, `candidate_votes` and `county_votes`, to later attach vote totals as the values to either candidate or county keys.

Using the csv library for Python, a `with` statement opens the file and the data is set to a variable using `reader = csv.reader(election_data)`. A `for` loop that iterates over every `row` in the `reader` variable begings summing the votes by every row minus the header into a `total_votes` integer variable initialized to 0 by:

```
total_votes = total_votes + 1
```

A variable that points at the column of data that contains the county data is created by `county_name = row[1]`; this used to identify the unique counties to add to the `county_list` created earlier. This is accomplished by establishing that there's no previous membership and appending the data. This value is also added as a key to the `county_votes` dictionary, starting with a value of 0 votes:

```
if county_name not in county_list:

    county_list.append(county_name)

    county_votes[county_name] = 0
```
The same is done for the candidates. Outside of the conditional votes are tallied by `county_votes[county_name] += 1`, so that each line that matches one of the unique counties a vote is added to the value associated with the county name key. Again, the same is done on the variables related to the candidates.

A second `with` statement opens the .txt file that the results variables will be saved in; first is the `total_votes` count, which is reported simply in an f-string, `f"Total Votes: {total_votes:,}\n"`.

To summarize the county data `for` loop is used to loop through each `county_name` in the `county_votes` dictionary. The value is retrieved and stored in a new variable `cty_votes`, using `cty_votes = county_votes.get(county_name)`. A percentage is calculated using this variable and the results saved into a variable that contains the formatted strings to save to the .txt file.
```
    cty_vote_percentage = float(cty_votes) / float(total_votes) * 100
    cty_results = (
        f"{county_name}: {cty_vote_percentage:.1f}% ({cty_votes:,})"
    )
```
Again a similar process is used to write a similar statement for the candidates. The last piece of data that is analyzed is the greatest total voter turnout, which is determined by checking if the votes in one county is greater than a `largest_turnout` that is initially set to 0 and if so updating the value of the `largest_turnout` to `cty_votes` and the `largest_county` to the `county_name`. The winning candidate is determined the same way.
```
        if (cty_votes > largest_turnout):
            largest_turnout = cty_votes
            largest_county = county_name
```

### Results

The results from the election analysis are as follows:
* A total of 369,711 votes were cast.
* Across the 3 counties:
    * Jefferson county had 38,855 votes with 10.5% of the total votes cast.
    * Denver county had 306,055 votes with 82.8% of the total votes cast.
    * Arapahoe county had 24,801 votes with 6.7% of the total votes cast.
* The county with the highest turnout is Denver County.
* For each candidate:
    * Charles Casper Stockham received 23.0% of the vote with 85,213 votes.
    * Diana DeGette received 73.8% of the vote with 272,892 votes.
    * Raymon Anthony Doane received 3.1% of the vote with 11,606 votes.
* The winner is Diana DeGette with 272,892 votes (73.8%).

## Election Audit Summary

This Python script succeeds at summarizing the important aspects of election in an easily digestible fashion: the winner along with details that breakdown the total votes cast per candidate. It also has information on which county the votes were cast in, information that is highly valuable to future campaigns for figuring out which populations are likely to turn up to elections. One of the strong aspects of this script is that it is generally adaptable to any election with minor changes, as long as the data is provided in a CSV file with at least a column that stores information on both the candidate the vote is for and the county the vote was cast in.

One of the adaptions that could improve this script is giving it the ability to scan the header row for the relevant columns instead of manually setting a variable using the list index such as was done with `candidate_name = row[2]`. Currently this script is specialized to run with a particular CSV file where the candidate for whom the vote was cast is the 3rd column, but in future elections it is likely this information may be stored in a different column. 

More pressing is cleaning up the script by using functions. Currently the script repeats tasks to extract information and write information relating to the number of votes cast in a county or for a candidate; a function that takes whatever aspect being analyzed from the election as an argument, uses that to determine which column to get data from, retrieves the unique values in the column, and then stores the amount of votes for those unique values would drastically cut out repeated code. Another function could be made specifically for writing the results to a .txt file. Making functions would also allow for easier adaptability for taking in new information if it was provided, though further adaptations would need to be made to incorpate potential data that might be reported with an election. 
