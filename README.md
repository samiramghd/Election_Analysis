#Election_Analysis
Election analysis with Python

###Overview of Election Audit: Explain the purpose of this election audit analysis.

In this project we're trying to read election_results.csv, use for loops and conditional statements with membership and logical operators to find the requested results. Then, print the results to the command line and save them to election_results.txt file. In this election audit we're going to complete these tasks.
- Calculate total votes.
- Calculate, print and save each county, the county’s total votes, and the county’s percentage of total votes.
- Determine the largest county based on votes and print the information for that county.

and from PyPoll code we have all these information about candidates and we also have some information about the winnig candidate which we go through the code.


###Election-Audit Results: Using a bulleted list, address the following election outcomes. Use images or examples of your code as support where necessary.

Before answeing the questions let's get through some parts of the code and we'll review the rest by answering the questions.
by importing two libraries to our code we will be able to read the csv file and write on a txt file.

![name-of-you-image](https://github.com/samiramghd/Election_Analysis/tree/main/Resources/import.PNG)

and then we define two list to hold the names and two dictionary to keep the names as a key and votes as a value.

![name-of-you-image](https://github.com/samiramghd/Election_Analysis/tree/main/Resources/names.PNG)

here we use a for loop to go through our csv file, get the names, add it to the list, set their values to zero.

 ![name-of-you-image](https://github.com/samiramghd/Election_Analysis/tree/main/Resources/for1.PNG)

 and then by answering the questions we're having the rest of the code and the results. after printing each result we want to save that in our election_results.txt file, in resources folder. by using txt_file as a variable we're able to use write method to write the results in our text file.

 ![name-of-you-image](https://github.com/samiramghd/Election_Analysis/tree/main/Resources/save.PNG)


1. How many votes were cast in this congressional election?
    
    To calculate total votes we're using a for loop like this picture

    ![name-of-you-image](https://github.com/samiramghd/Election_Analysis/tree/main/Resources/total_votes1.PNG)

    and we're getting results for total_votes as shown here

    ![name-of-you-image](https://github.com/samiramghd/Election_Analysis/tree/main/Resources/total_votes2.PNG)

    Total Votes in this congressional election was 369,711

2. Provide a breakdown of the number of votes and the percentage of total votes for each county in the precinct.

    by using this part of code we can get county names, votes and the percentage of total votes.
    
    ![name-of-you-image](https://github.com/samiramghd/Election_Analysis/tree/main/Resources/county_results1.PNG)

    and here we can see the results which we print in the terminal

    ![name-of-you-image](https://github.com/samiramghd/Election_Analysis/tree/main/Resources/county_results2.PNG)
    
    - Jefferson: 10.5% of total percentage and total votes of 38,855
    - Denver: 82.8% of total percentage and total votes of 306,055
    - Arapahoe: 6.7% of total percentage and total votes of 24,801 

3. Which county had the largest number of votes?

    by using If loop and going through the votes we compare the votes and we keep the largest county name and then print it which we cn see in this part of the code.

    ![name-of-you-image](https://github.com/samiramghd/Election_Analysis/tree/main/Resources/largest1.PNG)
    
    and output is going to be like this

    ![name-of-you-image](https://github.com/samiramghd/Election_Analysis/tree/main/Resources/largest2.PNG)

    **Denver county had the largest number of votes (306,055)**

4. Provide a breakdown of the number of votes and the percentage of the total votes each candidate received.

    In this part of code we're doing the same thing we did in county votes, and by using a for loop we're counting the candidate votes and calculating the percentage of total votes for each candidate.

    ![name-of-you-image](https://github.com/samiramghd/Election_Analysis/tree/main/Resources/candidate1.PNG)

    and this is the output in terminal

    ![name-of-you-image](https://github.com/samiramghd/Election_Analysis/tree/main/Resources/candidate2.PNG)

    - Charles Casper Stockham: 23.0% of total percentage and total votes of 85,213
    - Diana DeGette: 73.8% of total percentage and total votes of 272,892
    - Raymon Anthony Doane: 3.1% of total percentage and total votes of 11,606

5. Which candidate won the election, what was their vote count, and what was their percentage of the total votes?

    In tis part of the code we're trying to find the winner candidate and by using if loop we're comparing votes and the percentages of votes and keep the highest one and choose it as a winner candidate.

    ![name-of-you-image](https://github.com/samiramghd/Election_Analysis/tree/main/Resources/winning1.PNG)

    this is the result in the terminal

    ![name-of-you-image](https://github.com/samiramghd/Election_Analysis/tree/main/Resources/winning2.PNG)


    **Diana DeGette won the election with the 73.8% of total percentage and total votes of 272,892**


###Election-Audit Summary: In a summary statement, provide a business proposal to the election commission on how this script can be used—with some modifications—for any election. Give at least two examples of how this script can be modified to be used for other elections.

If we want to use this script for any other election first we need to load the right csv file which has all the data and by using thsi part of the code here we can load our new data and save it in a new text file.

 ![name-of-you-image](https://github.com/samiramghd/Election_Analysis/tree/main/Resources/import2.PNG)

 and next in this part of code we need to find the candidate and county names wich can be vary in different csv files. so for another election we have to make sure which row we are using to get the names.

 ![name-of-you-image](https://github.com/samiramghd/Election_Analysis/tree/main/Resources/change2.PNG)

and of course with using any other election we need to modify our script to make sure we're gettig the results we want.
