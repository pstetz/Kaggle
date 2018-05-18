| <img src="photos/carpool.png" alt="Counties with the highest number of carpoolers" style="float:left;"/> | 
|:--:| 
| *More Georgia and Texas than I was expecting* | 

# US Census Data ([Kaggle link](https://www.kaggle.com/muonneutrino/us-census-demographic-data))

This is a folder contains an exploration of the 2015 American Community Survey estimate.

The analysis is contained in different folders to try and stay organized.  For an overview of each notebook, see items 2-6 in the Table of Contents below.

# Table of Contents

1.) [Introduction](#intro)

   - [Background](#background)

   - [Tracts](#tracts)

   - [Questionnaire](#questionnaire)

   - [Dataset](#dataset)

2.) [State Focus](#state)

3.) [Racial Focus](#race)

4.) [Numeric Focus](#numeric)

   - [Income](#nu_income)

   - [Commute times](#nu_commute)

5.) [Focus on Fun!](#fun)

6.) [General Focus](#general)

7.) [Resources](#resources)

8.) [Criticism](#criticism)

<a name="intro"></a>
# Introduction

<a name="background"></a>
### Background

Every 10 years, the US government conducts a survey of the entire nation to understand the current distribution of the population.  Every citizen in the States receives a questionaire (see [questionaire below](#questionnaire)).

In 2005, the American Community Survey (ACS) was founded after many years of demand for more data.  The ACS is run by the US Census Bureau, but has a number of differences with the 10 year census.  The ACS sends out surveys to 295,000 addresses monthly (or 3.5 million per year).

The purpose of this data is somewhat different and has sparked [some controversy](https://www.lewrockwell.com/2004/07/ron-paul/its-none-of-your-business/) (to fellow Americans: take a guess who!).  The 10 year Census is a codified procedure that goes back to the forefathers and described in Article I, Section II of the US Constitution.  It's purpose is purely for redistricting and keeping the Electoral College updated with population shifts.  The ACS

As al


<a name="tracts"></a>
### Tracts

Tracts are.  They range from 3 to 53,812 people but are generally around 4,000 people

<a name="questionnaire"></a>
### Questionnaire

| <img src="photos/census.png" alt="2010 Census form" style="float:left;"/> | 
|:--:| 
| *The 2010 Census form ([photo](https://www.census.gov/history/pdf/2010questionnaire.pdf))* | 

<a name="dataset"></a>
### Dataset

In the exact words of Kaggle user [Muon Neutrino](https://www.kaggle.com/muonneutrino), the individual who hosts this [dataset](https://www.kaggle.com/muonneutrino/us-census-demographic-data) on Kaggle

"""

The data here are taken from the DP03 and DP05 tables of the 2015 American Community Survey 5-year estimates. The full datasets and much more can be found at the American Factfinder [website](https://factfinder.census.gov/faces/nav/jsf/pages/index.xhtml). Currently, I include two data files:

    1.) census_tract.csv: Data for each census tract in the US, including DC and Puerto Rico.
    1.) census_county.csv: Data for each county or county equivalent in the US, including DC and Puerto Rico.

The two files have the same structure, with just a small difference in the name of the id column. Counties are political subdivisions, and the boundaries of some have been set for centuries. Census tracts, however, are defined by the census bureau and will have a much more consistent size. A typical census tract has around 5000 or so residents.

The Census Bureau updates the estimates approximately every year. At least some of the 2016 data is already available, so I will likely update this in the near future.

"""


<a name="state"></a>
# State Focus

Focuses mostly on how relationships between States.  What state is the most populated?  Which state has the lowest unemployment?


| <img src="photos/state_unemployment.png" alt="States with the highest unemployment" style="float:left;"/> | 
|:--:| 
| *This data was collected before Hurrican Maria* | 


<a name="race"></a>
# Racial Focus

Focuses on the race columns.  Which State or County has the greatest representation of that race?  How does unemployment match up between the different races?

| <img src="photos/race_county.png" alt="Highest Black and Hispanic populations" style="float:left;"/> | 
|:--:| 
| *Highest Black and Hispanic populations (have you ever heard of Cook, Illinois?)* | 

<a name="numeric"></a>
# Numeric Focus

This notebook looks at the easily quantifiable columns and ignores labels like race, County, and State.

<a name="nu_income"></a>
### Income

To get a sense of 

| <img src="photos/income_kde.png" alt="Distribution of income" style="float:left;"/> | 
|:--:| 
| *Distribution of income* | 

Different

| <img src="photos/career_dist.png" alt="Distribution of careers based on income" style="float:left;"/> | 
|:--:| 
| *Distribution of careers based on income* | 

Furthermore we can see that the counties on the different ends of income have a different

| <img src="photos/sector_dist.png" alt="Distribution of sector work based on income" style="float:left;"/> | 
|:--:| 
| *Distribution of sector work based on income* | 

<a name="nu_comute"></a>
### Commute times

The

| <img src="photos/commute_kde.png" alt="Distribution of transportation methods by commute time" style="float:left;"/> | 
|:--:| 
| *Distribution of commute times* |

It would 

| <img src="photos/commute_dist.png" alt="Distribution of transportation methods by commute time" style="float:left;"/> | 
|:--:| 
| *Distribution of transportation methods by commute time* |  

<a name="fun"></a>
# Focus on Fun!

This notebook includes a lot of misc relationships and facts I didn't want to keep out.  The notebook contains a script that analyzes different selected counties.  The below graph looks at the counties with which I'm most familar.

| <img src="photos/selected_counties.png" alt="Famous counties to the Bay Area/World" style="float:left;"/> | 
|:--:| 
| *Famous counties of the Bay Area and California* | 

<a name="general"></a>
# General Focus

This notebook focuses on the data in general.  What are the missing values?  Do all percents add up to 100?

<a name="resources"></a>
# Resources

- The American Community Survey website ([link](https://www.census.gov/programs-surveys/acs/))
- The American Community Survey Information Guide ([link](https://www.census.gov/programs-surveys/acs/about/information-guide.html))
- The dataset for this project ([link](https://www.kaggle.com/muonneutrino/us-census-demographic-data)).  Thank you again to [MuonNeutrino](https://www.kaggle.com/muonneutrino) and [Kaggle](https://www.kaggle.com/)

<a name="critism"></a>
# Criticism

- How accurate is the data?  Many people flat out refuse to answer any [questions](https://www.youtube.com/watch?v=bYwdOxOBwgM).
- The estimated budget for 2019 is $3.8 billion ([link to census budget](https://www2.census.gov/about/budget/2019-Budget-Infographic-Bureau-Summary.pdf)).
- Here is a [sample form](https://www2.census.gov/programs-surveys/acs/methodology/questionnaires/2018/quest18.pdf) from 2018, you can decide how invasive the questions are for yourself