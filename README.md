# Multinational Retail Data Centralisation Project

![Static Badge](https://img.shields.io/badge/Welcome%20To-blue)

![Static Badge](https://img.shields.io/badge/The%20Multinational%20Retail%20Data%20Centralisation%20Project-blue)

![Static Badge](https://img.shields.io/badge/A%20Data%20Training%20Project%20By-blue)

![Static Badge](https://img.shields.io/badge/Giles%20Williams-blue)

## Introduction 

![Static Badge](https://img.shields.io/badge/Project%20Summary%3A-blue)

For a (fictional) multinational retail business, produce a system that stores their current sales data in a database so it acts as the single source of truth and can be accessed from one centralised location by the team.  

![Static Badge](https://img.shields.io/badge/Project%20Scope%3A-blue)

A multinational retail business, selling a range of just under 2,000 products across multiple vertical markets (including home goods and applicances, health and beauty, food and beverages and sports and leisure), is looking to update how they manage and use their data.

Currently, their sales data is spread across many different data sources making it not easily accessible or analysable by current members of the team.
In an effort to become more data-driven, the organisation would like to make its sales data accessible from one centralised location, allowing senrior management to view up-to-date metrics and help inform business decisions.

The project is divided into 4 milestones:

![Static Badge](https://img.shields.io/badge/Milestone%201%3A%20set%20up%20the%20dev%20environment-blue)

![Static Badge](https://img.shields.io/badge/Milestone%202%3A%20extract%20and%20clean%20the%20data-blue)

![Static Badge](https://img.shields.io/badge/Milestone%203%3A%20create%20the%20database%20schema-blue)

![Static Badge](https://img.shields.io/badge/Milestone%204%3A%20analyse%20the%20data-blue)



A description of the project: what it does, the aim of the project, and what you learned

## Installation Instructions
Python3 is required to run this pipeline.

Follow these instruction to [clone this repository](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository#cloning-a-repository) to your local machine.

## Usage Instructions

### How to run the pipeline

### Task considerations and related decisions made

NOTES for the cleaning part of the task

Task 3: clean up sales data.
Formatted dates correctly and removed any that were now null values
Needed correct wrong GB country code

Task 4: clean card details pdf
Formatting dates created NULL values for incorrect date, removed those
removed ? from front of some card details
Converted card number column to int

Task 5: clean store data
Dropping 'lat' column that was mostly null values and the 'lattitude' column had this data
Formet date with datetime stamp and remove rows with Null datatime stamp
Correct continent code errors to replace eeAmerica and eeEurope with the correct continents

Task 6: extract and clean product details
converted the weights as they were in multiple measurements (g, kgs, oz, ml)
concerted the date added column to datatimestamp and the weight column to a float

Task 7: retrieve and clean the orders_table
USed the same read_rds_table method as in the task 3 to read the table from the AWS RDS 

## File structure of the project

.
 * hangman
   * milestones                             #archive of each milestone file
     * milestone_2.py
     * milestone_3.py
     * milestone_4.py
     * milestone_5.py    
   * hangman_game.py                 
 * README.md
 * .gitignore



## License Information
This repo is unlicensed as it was intended only for training purposes.


