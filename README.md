# Election Audit Analysis - Module 3 Challenge
## Overview of Election Audit

Python, VS Code and GitHub are powerful tools, and what better way to begin learning how to use them than by simulating a real-world use case. The ***election audit analysis*** incorporates key concepts and skills development that will help students build a foundation in coding and managing data. These include:

- Using the command line
- An introduction to using VS Code
- Installing Python and creating a Python file
- Creating and cloning a GitHub repository
- Understanding Python syntax and performing calculations
- Reviewing Data types and structures, including lists, tuples and dictionaries
- Working with Operators, For loops and If/Then statements in Python
- Understanding print formatting
- Reading in, working with, and writing out to data files.
- Using pseudocode to help structure thought and coding strategy
- Working with Python Dependencies, Modules, and Packages

The ***election audit analysis*** simulation models a real-world example where Tom, your boss, assigns a project for you to aggregate, calculate and prepare election information for presentment to the Colorado Board of Electors. Using Python, your job is to read a CSV data file, tabulate total number of votes cast, determine the number and percentage of votes cast for each candidate, and determine the winner. Tom also asks you to breakdown the number and percentage of votes by county. You must present the data and in a specified format that is then output to a text file.   

## Election-Audit Results 
### Here are the results of the ***election audit analysis***:

#### Votes cast in this congressional election: 369,711

#### Votes by County:
      - Jefferson: 10.5% (38,855)
      - Denver: 82.8% (306,055)
      - Arapahoe: 6.7% (24,801)

#### County with the largest number of votes:
      - Denver

#### Breakdown of the number of votes and the percentage of the total votes each candidate received:
      - Charles Casper Stockham: 23.0% (85,213)   
      - Diana DeGette: 73.8% (272,892)
      - Raymon Anthony Doane: 3.1% (11,606)
      
#### Winning candidate, their vote count, and percentage of the total votes:
      - Winner: Diana DeGette
      - Winning Vote Count: 272,892
      - Winning Percentage: 73.8%

The command line and text file output appears as follows:

![command line output](https://github.com/vjtrom/election_analysis/blob/main/resources/Screen%20Shot%204.png)

![text file output](https://github.com/vjtrom/election_analysis/blob/main/resources/Screen%20Shot%203.png)

## Other Applications

The ***election audit analysis*** script has other applications beyond what we are using it for here. It can be modified to produce aggregation, calculations and insights for other types of elections and analysis. For example, by appending the election_results.CSV file with additional data fields, the script might be used to draw insights from elections that are either larger or smaller than congressional district elections. In addition, the ***election audit analysis*** could be applied to party-level affiliation or primary elections. Some of these examples are:

- **Other congressional precincts** - If the necessary data is provided, the existing script can be used for other congressional district elections within the state. This would entail developing lists and dictionaries for the other counties within the state. 
- **Gubernatorial, US Senate and other state-wide office elections** – The script could be modified to track state-wide elections. This would require the aggregation all of the precincts within the state, so additional data would be needed. 
- **Township, county or other municipal elections** - You can also go the other way and use the script for tabulation of smaller level precincts at the sub-county level. Again, the data would need to be appended for these smaller increments. 
- **More than one elected official**  - For certain town or city councils, elected officials “at-large”, or judgeships where there is more than one elected office and more than on candidate, the script could be used to identify winners (plural) versus just one winner. 
- **Primary elections** - The script could be modified for use in primary versus general elections. If each ballot was coded with the political party affiliation, such as Republican, Democrat or Independent, the script could be used to tally the ballots by political party in order to figure out the winners of primary elections, not just general elections. 

Overall, the script is versatile and can be refactored, however, it is dependent on providing additional data in order to support these other uses.

![script mod 1](https://github.com/vjtrom/election_analysis/blob/main/resources/Screen%20shot%201a.png)
![script mod 2](https://github.com/vjtrom/election_analysis/blob/main/resources/Screen%20Shot%202a.png)
