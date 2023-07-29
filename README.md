# Boston_house Price Prediction

### About the dataset:

The Boston Housing Dataset is a derived from information collected by the U.S. Census Service concerning housing in the area of Boston MA .This data includes information for 506 observations in relation to 12 attributes. 

We'll explore every feature of these data  in our quest for knowledge. Let's get started!

### Features :

CRIM - per capita crime rate by town

ZN - proportion of residential land zoned for lots over 25,000 sq.ft.

INDUS - proportion of non-retail business acres per town.

CHAS - Charles River dummy variable (1 if tract bounds river; 0 otherwise)

NOX - nitric oxides concentration (parts per 10 million)

RM - average number of rooms per dwelling

AGE - proportion of owner-occupied units built prior to 1940

DIS - weighted distances to five Boston employment centres

RAD - index of accessibility to radial highways

TAX - full-value property-tax rate per \$10,000

PTRATIO - pupil-teacher ratio by town

B - 1000(Bk - 0.63)^2 where Bk is the proportion of blacks by town

LSTAT - % lower status of the population

### Data Gathering :

![image](https://github.com/GayatriBJ/Boston_house/assets/125629830/f0b001ba-7159-48af-bf6b-ff61c2bc9789)


### EDA & Feature Engineering :
In this step, we have to analyze the data. We check for :

checking & handling missing values
identify outliers
remove outliers
encoding of categorical variables
Feature Transformation
Scaling
#### Feature Selection / Feature Extraction :
The goal of feature selection techniques in machine learning is to find the best set of features that allows one to build optimized models of studied phenomena. It helps Improves Model Performance It helps Optimizes Model Training Time

### Feature Selection Methods :

Filter Method
Wrapper Method
Embedded Method

###Model Training :
In this step, Model is train using different machine learning techniques. I have used Linear Regression.

After performing standardization, dataset is splited with a ratio of 0.2 that means 80% data for training and 20% data for validation process.

### Model Evaluation :
To check model is performing well on training data set as well as testing data data we need evaluate the model using metrics

Metrics used are :

Mean Square error
Mean Absolute error
Squareroot of Mean Square error
R2 score
Adjusted R2 score

### Web development Framework :
In this project flask method is used to write API's for the project so that user can interacte with help of html web to input the value and to get the output

### Deployment on AWS :
For public access we have used AWS service, so that anyone can access the website and can use to get the results.

#### Important Files

interface.py :-
In this file we have write the API's and by running this file you can start server.

util.py :-
This file contains the basic function that will help to interface file to get the results

config.py :-
In this file you can change the file path for the pickle file and json file. Also, you can change the port number according to the requirement

requirement.txt :-
This file contain necessary libraries and its version, user need to install this libraries while running this project.

source.html :-
This html file, contain website page coding.

