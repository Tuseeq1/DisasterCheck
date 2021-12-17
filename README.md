# Disaster Response Pipeline Project

### Table of Contents

1. [Installation](#installation)
2. [Project Motivation](#motivation)
3. [File Descriptions](#files)
4. [Results](#results)
5. [Instructions](#instructions)
5. [Licensing, Authors, and Acknowledgements](#licensing)

## Installation <a name="installation"></a>

You can run this code with Anaconda distribution of Python or in case you want to use pip, using requirement file should help you get all the libraries you need.  The code should run with no issues using Python versions 3.*. 

## Project Motivation<a name="motivation"></a>

For this project, I was using Data Provided by [Figure Eight](https://www.figure-eight.com/). This data inculed two files message.csv and categories.csv contain info of past messages recieved during disasters and how they were classified into different categories. I am using this data to create a ML system that can predict the nature of a message during the disaster to help understand how to respond quickly accordingly.


## File Descriptions <a name="files"></a>

There are three folders in this project.<br>
app<br>
| - template<br>
| |- master.html # main page of web app<br>
| |- go.html # classification result page of web app<br>
|- run.py # Flask file that runs app<br>

data<br>
|- disaster_categories.csv # data to process<br>
|- disaster_messages.csv # data to process<br>
|- process_data.py # ETL Pipeline that process clean and save data into db<br>
|- InsertDatabaseName.db # database to save clean data to

models<br>
|- train_classifier.py # ML Pipeline that generate appropriate model, train and save it pkl file<br>
|- classifier.pkl # saved model<br>
README.md<br>

The data set used for this project is also included in the project.

## Results<a name="results"></a>

You can run flask app to see the results and use model to predict.

## Instructions<a name="instructions"></a>:
1. Run the following commands in the project's root directory to set up your database and model.

    - To run ETL pipeline that cleans data and stores in database
        `python data/process_data.py data/disaster_messages.csv data/disaster_categories.csv data/DisasterResponse.db`
    - To run ML pipeline that trains classifier and saves
        `python models/train_classifier.py data/DisasterResponse.db models/classifier.pkl`

2. Run the following command in the app's directory to run your web app.
    `python run.py`

3. Go to http://0.0.0.0:3001/



## Licensing, Authors, Acknowledgements<a name="licensing"></a>

Must give credit to Figure Eight for the data.



