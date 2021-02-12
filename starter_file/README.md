*NOTE:* This file is a template that you can use to create the README for your project. The *TODO* comments below will highlight the information you should be sure to include.

# Titanic Survival Prediction

*TODO:* Write a short introduction to your project.
In this project we are going to train the same dataset but using two different approaches.

- Approach No. 1 will be AutoML API from Azure 
- Approach No. 2 will be HyperDrive API (also from Azure) 

For both approaches we will retrieve the best model and compare the best models among them. The winner of this comparison will be registered and deployed. 
Finally and after the deployement has taken place we are going to test the best model End Point by sending a request.

The chart below should visualize the above explanation:

![alt text](https://github.com/MarceloLandaverde/udacity-capstone-project/blob/master/Pictures/Diagram.PNG)

## Project Set Up and Installation
*OPTIONAL:* If your project has any special installation steps, this is where you should put it. To turn this project into a professional portfolio project, you are encouraged to explain how to set up this project in AzureML.

## Dataset
As you probably have guessed from the project title we will be working with the "Titanic Dataset" which is already a classical dataset to learn Machine Learning

### Overview
This data is an open source set which is available online through the "OpenML" Organization ( https://www.openml.org/ ) 
If you are interested on checking the dataset by yourself you can click on the following link: https://www.openml.org/data/get_csv/16826755/phpMYEkMl

### Task
*TODO*: Explain the task you are going to be solving with this dataset and the features you will be using for it.

The main task for this project will be to build a predictive model that answers the question: “what sorts of people were more likely to survive?” 
To answer the above stated question we are going to give the model different input variables such as age, type of cabin the passanger had, etc.

More specifically, we are going to concentrate on the following features:

![alt text](https://github.com/MarceloLandaverde/udacity-capstone-project/blob/master/Pictures/features.PNG)

The above features will be pre-processed to facilitate computation during training.If you are interested in this step you can take a look the the following files:

- pre-process.py:
This file contains different pre-process functions which will be then imported from the train.py file

- train.py:
This file imports the functions from the pre-process file and wraps all of them into a function which is then call the "clean_data" fuction.
In addition to the clean data function the script applies the following steps:
  - Scales the independent variables
  - Splits the data into train and test
  - Performs a logist regression

If you would like to take a look to the scripts here you will find the link to them:

- Pre-process file: \
https://github.com/MarceloLandaverde/udacity-capstone-project/blob/master/starter_file/pre_preprocess.py

- Train file: \
https://github.com/MarceloLandaverde/udacity-capstone-project/blob/master/starter_file/train.py



### Access
*TODO*: Explain how you are accessing the data in your workspace.
During the project two differents ways were implemented in order access the data set.

For the experiment using AutoML we just simply imported it to the notebook by using the TabularDatasetFactory class and the method ".fromDelimetedFiles"
Afterwards the dataset was registered

The following pictures displays the steps mentioneds above:

![alt text](https://github.com/MarceloLandaverde/udacity-capstone-project/blob/master/Pictures/dataset_AutoML.PNG)


For the experiment using the HyperDrive we did the same as with the AutoMl; the only difference is that it was performend within the "train.py" script (rows 31-33 from script: https://github.com/MarceloLandaverde/udacity-capstone-project/blob/master/starter_file/train.py )


## Automated ML
*TODO*: Give an overview of the `automl` settings and configuration you used for this experiment
First of all it is important to give a generic view of the AutoML settings and configuration that were used for this experiment.

The first step is to create the AutoML settings which will be afterwards passed to the AutoML Configuration as part of the parameters needed within the configuration.
Let's take briefly a look into the AuroML settings parameters used in this experiment:

- experiment_timeout_minutes
- max_concurrent_iterations
- primary_metric

Now let's move on with the AutoML Configuration and explain briefly those parameters:

- compute_target
- task
- training_data
- label_column_name
- path
- enable_early_stopping
- featurization
- debug_log 
- automl_settings

In the below picture you could see the code snippet which captures the AutoML Settings and Configuration:

![alt text](https://github.com/MarceloLandaverde/udacity-capstone-project/blob/master/Pictures/AutoML_Config.PNG)




### Results
*TODO*: What are the results you got with your automated ML model? What were the parameters of the model? How could you have improved it?

*TODO* Remeber to provide screenshots of the `RunDetails` widget as well as a screenshot of the best model trained with it's parameters.

## Hyperparameter Tuning
*TODO*: What kind of model did you choose for this experiment and why? Give an overview of the types of parameters and their ranges used for the hyperparameter search


### Results
*TODO*: What are the results you got with your model? What were the parameters of the model? How could you have improved it?

*TODO* Remeber to provide screenshots of the `RunDetails` widget as well as a screenshot of the best model trained with it's parameters.

## Model Deployment
*TODO*: Give an overview of the deployed model and instructions on how to query the endpoint with a sample input.

## Screen Recording
*TODO* Provide a link to a screen recording of the project in action. Remember that the screencast should demonstrate:
- A working model
- Demo of the deployed  model
- Demo of a sample request sent to the endpoint and its response

## Standout Suggestions
*TODO (Optional):* This is where you can provide information about any standout suggestions that you have attempted.
