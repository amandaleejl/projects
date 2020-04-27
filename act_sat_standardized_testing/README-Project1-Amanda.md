# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) 

# Project 1: SAT & ACT Analysis

### Context and Problem Statement

The ACT and SAT tests are used as a measure of college readiness and used a gauge for admission into college through these tests. The ACT includes an English Test, Reading Test, Mathematics Test and a Science Test. The SAT includes a Reading Test, Writing and Language Test and a Math Test. In recent years, the **ACT has had a higher frequency of full participation (100%) for more states as compared to the participation for the SATs.**

We are a non profit organisation with the goal to connect students to college success and expand access to higher education. With the interest to promote the participation of SATs, we aim to devise a strategic plan that targets areas where lower rates of participation for both tests are observed.

As such, to come up with an appropriate and targeted solution, we have decided to analyse the **SAT and ACT participation data** and **average scores by states** in 2017 and 2018.


---

## Executive Summary

### Contents:

- [Exploratory Data Analysis](#Exploratory-Data-Analysis)
- [2017-18 SAT and ACT Data Dictionary](#2017-18-SAT-and-ACT-Data-Dictionary)
- [Interpretation of Results](#Interpretation-of-Results)
- [Outside Research](#Outside-Research)
- [Conclusions and Recommendations](#Conclusions-and-Recommendations)
---

### Exploratory Data Analysis

After importing and cleaning the datasets, we have created and combined the SAT and ACT dataframes via 'State' for better comparison between the two tests. We have used the .describe() command to provide the descriptive statistics for the two dataframes.

We have also changed the data type from object to float for the participation columns in the respective dataframes to be more indicative of the values. Additional rows, duplicated data and incorrect data have been cleaned.

---

### 2017-18 SAT and ACT Data Dictionary

|Feature|Type|Dataset|Description|Feature|Type|Dataset|Description|
|---|---|---|---|---|---|---|---|
|act_2017_participation |float|ACT|State ACT Participation percentage, 2017|act_2018_updated_participation|float|ACT|State ACT Participation percentage, 2018|
|act_2017_english |float|ACT|State mean score for ACT English, 2017|act_2018_updated_english|float|ACT|State mean score for ACT English, 2018|
|act_2017_math|float|ACT|State mean score for ACT Math, 2017|act_2018_updated_math|float|ACT|State mean score for ACT Math, 2018|
|act_2017_reading|float|ACT|State mean score for ACT Reading, 2017|act_2018_updated_reading|float|ACT|State mean score for ACT Reading, 2018|
|act_2017_science|float|ACT|State mean score for ACT Science, 2017|act_2018_updated_science|float|ACT|State mean score for ACT Science, 2018|
|act_2017_comp|float|ACT|State mean score for ACT Composite, 2017|act_2018_updated_comp|float|ACT|State mean score for ACT Composite, 2018|
|sat_2017_participation|float|SAT|State SAT Participation percentage, 2017|sat_2018_participation|float|SAT|State SAT Participation percentage, 2018|
|sat_2017_ewb|int|SAT|State mean score for SAT Evidence-based reading and Writing, 2017|sat_2018_ewb|int|SAT|State mean score for SAT Evidence-based reading and Writing, 2018|
|sat_2017_math|int|SAT|State mean score for SAT Math, 2017|sat_2018_math|int|SAT|State mean score for SAT Math, 2018|
|sat_2017_total|int|SAT|State mean score for average total score for SAT, 2017|sat_2018_total|int|SAT|State mean score for average total score for SAT, 2018|

An updated ACT 2018 scoring data with the average scores of the individual components have been added.

---

### Interpretation of Results:

Evidently, there seems to be a higher percentage of participation among the individual states for the ACT Test. It is noted that a high participation for one test, will more often than not result in a lower participation in the other test.

The results obtained from the data provided do not result in a normal distribution. For normal distribution to be observed, the data should be around the central value with no left or right bias.

It is also noted that a high average score in a test is negatively correlated with the participation rates of the state. For the participation rates, places whereby the participation is high, the test scores are lower as a result of dilution of the quality of performance. This is true for the opposite where lower participation results in higher performance score. This could be indication of a selection bias, whereby the more academically inclined students form the larger population that is taking the tests.

Due to the non-normal distribution, the recommendations made subsequently to help increase the participation rates for the SAT will be heavily relied on the external research made.

---

### Outside Research:

Colorado and Illinois started with a higher participation rate for the ACT tests in 2017, but subsequently changed to have a 100% participation for the SATs in 2018. From further research, Colorado and the College Board partnered to administer the SAT as the state's accountability exam. This explains the increase in participation rates for the SAT in 2018. Similarly, there was a transition from ACT to SAT as the Illinois College Entrance Exam. In previous years, the exam mandated by the state of Illinois was the ACT. The major reason for the switch is due to the change of the composition of its mathematics curriculum.
Oregon has a low participation rate >50% participation for both the SATs and ACTs. From research, it is seen that Oregon schools rank in the bottom third nationally and the state has a weak financial contribution to schools. The low participation rate of Oregon might also be due to growing disparity among the rich and the poor, thus people are less able afford education.

---

### Conclusions and Recommendations:

Overall, the ACT and SAT participation distributions were similar. In instances where the particpation of a particular test was higher, it would result in a lower percentage of participation in the other. The ACTs had a higher baseline participation percentage, and seemed to be the more popular choice among the states. However, there seemed to be a slow change over to the SATS, with states like Colorado and Illinois making a switch over to the SATs from the ACTs.

Being a non-profit organisation with the goal to increase the overall participation for the SAT to provide an entrance to college, I would suggest for the college board to first target Oregon. Oregon has the lowest participation rate among the states for both the ACT and SAT test. This is due to the lack of funding for their education system and growing income disparity among the people. There is an opportunity for the College Board to come in and promote the SAT with intentions to help students achieve higher education access. The College Board can consider working with the schools in Oregon rolling out the SAT School Day programme to provide the option for a subsidised fee for the SAT. I believe that this might help change the mindset and priority placed on education to help increase the overall participation in the SAT test as well as to open up opportunities for further education. Achieving an improve SAT participation for Oregon and a greater emphasis for continued learning in Oregon will be the best way to spend resources.

---

### Sources:

- [College Board](https://www.collegeboard.org)
- [Oregon ranks low in Education, The Oregonian](https://www.oregonlive.com/education/2016/01/oregon_ranks_low_in_education.html)
- [Transition from ACT to SAT, Governors State University](https://opus.govst.edu/cgi/viewcontent.cgi?referer=https://www.google.com/&httpsredir=1&article=1333&context=capstones)


