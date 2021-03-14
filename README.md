# Election_Analysis #
## **Project Overview** #
 
### A Colorado Board of Elections employee has given us the following task to complete the election audit of a recent local congressional election. ###

### 1.Calculate the total number of votes cast. ###
### 2.Get a complete list of the conadidates who received votes. ###
### 3.Calculate the total number of votes each candidate received. ###
### 4.Calculate the percentage of votes each candidate won . ###
### 5.Determine the winner of the election based on the popular vote. ###

## **Resources** ##
* Data Source: election_results.csv
* Software: Python 3.7.4, Visual Studio Code 1.54.1

## **Summary** ##

The anlaysis of the election show that:

* The cadidates were:
  * Charles Casper Stockham
  * Diana Degette
  * Raymon Athony Doane

* The candidate results were:
  * Charles Casper Stockham received 23.0% of the vote and 85,213 number of votes.
  * Diana Degette received 73.8% of the vote and 272,892 number of votes.
  * Raymon Athony Doane received 3.1% of the vote and 11,606 number of votes.
* The Winner of the election was:
  * Diana Degette who received 73.8% of the vote with 272,892 votes.

![Analysis Image](https://user-images.githubusercontent.com/78942457/111059295-83ede700-8462-11eb-9502-0817c789ef67.PNG)
  
## **Challenge Overview** ##
### The Challenge was to expand on the data to include a breakdown of county information. ###

## **Challenge Summary** ##
The county analysis of the election shows that:

* There were 369,711 votes cast in the election.

* The counties where votes were cast and outcomes were:
  * Jefferson county with 10.5% of the vote and 38,855 votes cast.
  * Denver county with 82.8% of the vote and 306,055 votes cast.
  * Arapahoe county with 6.7% of the vote and 24,801 votes cast.

* The county with the largest number of votes was Denver with 306,055 votes cast.

![County Info Determination](https://user-images.githubusercontent.com/78942457/111059342-d9c28f00-8462-11eb-94d7-c8ca20bbdb32.PNG)

* The candidate results were:
  * Charles Casper Stockham received 23.0% of the vote and 85,213 number of votes.
  * Diana Degette received 73.8% of the vote and 272,892 number of votes.
  * Raymon Athony Doane received 3.1% of the vote and 11,606 number of votes.

* The Winner of the election was:
  * Diana Degette who received 73.8% of the vote with 272,892 votes.

## **Election Audit Summary ** ##

As the code automatically pulls the county and candidate items from the rows of data, the code could easily be used for any congressional district, or with the addition of district numbers, could be used for the entire state.  With the addition of information such as state data, we could use this code for not only one district in Colorado, but the entire US.  If a date and time stamp data point could be added, this information could also be utilitized to determine vote patterns by district to help better staff polling stations based on previous demand.
