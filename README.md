# Titanic-Survival Prediction
The survival status of individual passengers on the Titanic. The titanic data frame does not contain information from the crew, but it does contain actual ages of half of the passengers.
i have used LOGISTIC REGRESSION to build the model...
FOR MORE DETAILED EXPLAINATION OD EXPLAROTARY DATA ANALYSIS
https://www.kaggle.com/javagarm/my-first-note-titanic-survival-prediction-eda
Variable	Definition	Key,

survival	Survival	0 = No, 1 = Yes , 
pclass	Ticket class	1 = 1st, 2 = 2nd, 3 = 3rd , 
sex	Sex	,nb 
Age	Age in years	,
sibsp	# of siblings / spouses aboard the Titanic	,
parch	# of parents / children aboard the Titanic	,
ticket	Ticket number	,
fare	Passenger fare	,
cabin	Cabin number	,


embarkedN	Port of Embarkation	C = Cherbourg, Q = Queenstown, S = Southampton,
Variable Notes,


pclass: A proxy for socio-economic status (SES),
1st = Upper.
2nd = Middle
3rd = Lower.
,
age: Age is fractional if less than 1. If the age is estimated, is it in the form of xx.5,

sibsp: The dataset defines family relations in this way...,
Sibling = brother, sister, stepbrother, stepsister,
Spouse = husband, wife (mistresses and fiancés were ignored),

parch: The dataset defines family relations in this way...
Parent = mother, father,
.
Child = daughter, son, stepdaughter, stepson,
Some children travelled only with a nanny, therefore parch=0 for them.
