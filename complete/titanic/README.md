| <img src="photos/titanic.jpg" alt="Titanic" style="float:left;"/> | 
|:--:| 
| *The Titanic* |

# Titanic Survival Classification ([Kaggle overview](https://www.kaggle.com/c/titanic/))

A very good starting point for Data Scientists.  A lot of the basics are covered in this project and it's kind of fun learning the history as well!

### Submission

My approach has a lot of inspiration from [Yassine](https://www.kaggle.com/yassineghouzam) ([his work](https://www.kaggle.com/yassineghouzam/titanic-top-4-with-ensemble-modeling)) and [Minsuk](https://github.com/minsuk-heo) ([his work](https://github.com/minsuk-heo/kaggle-titanic/blob/master/titanic-solution.ipynb)).

Minsuk was very helpful in the data processing step.  The data processing step includes gathering the Titles from Names, rescaling the data, filling in NaN values, and making categorical columns numeric.

Like a good team, Yassine really helped me create a stacked model consisting of Random Forest Classifier, SVC, Gradient Boost Classifier, and Extra Trees Classifer.  Stacked models offer the advantage of being less likely to overfit than a singular model.  The hyper parameters for each model were determined separately by Grid Search Cross Validation.  Finally all the models were combined by a Voting Classifier.

### Analysis

This notebook helps enlighten one how variables correlate with one other.  In this we will notice that women were more likely to survive than men, young were more likely to survive than old, the rich had better odds than the poor, and more!

### Logs

If for some reason you are so inclined, my iterations of success (or failure) are included in the logs
