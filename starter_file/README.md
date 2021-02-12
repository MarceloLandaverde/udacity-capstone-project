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
  - Performs a logistic regression

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

- experiment_timeout_minutes:\
Refers to the maximum amount of time in minutes that all iterations combined can take before the experiment terminates. For this project the timeout was set to 20 Minutes

- max_concurrent_iterations: \
Refers to the maximum number of iterations that would be executed in parallel. Important to mention is that values for all experiments should be less than or equal to the maximum number of nodes of the compute cluster

- primary_metric: \
Refers to the metric that AutoML Process will optimize for model selection.For this project the primary metric selected was the accuracy. Other possibilities would have been the   following: \
  AUC_weighted \
  average_precision_score_weighted \
  norm_macro_recall \
  precision_score_weighted

Now let's move on with the AutoML Configuration and explain briefly those parameters:

- compute_target: \
Refers to the computer target resource name (notebook138164) on which we will let the model training run

- task: \
Refers to the type of task that we want to solve. In this case we are interested in classifiying (as accurate as possible) if someone would survive (1) or not (0). Therefore the type of taks entered is "classification"

- training_data: \
Refers to the dataset that we will use for training the model.Remeber that in this case we have stored the dataset in a variable call training_dataset

- label_column_name: \
Refers to name of the "dependent variable" of interest. In this case the name is "survived"

- path: \
Refers to the path in which our experiment is or will take place

- enable_early_stopping: \
dfasdf

- featurization: \
Setup as 'Auto'which is the default setting and specifies that, as part of preprocessing, so called data guardrails and featurization steps are to be done automatically. \
The guardrails help to identify potential issues with the data (for example, missing values or class imbalance). They also help to take corrective actions for improved results.\
Featurization steps provide techniques that are automatically applied to the input data as part of the pre-process.\
Plese for more details checked on the documentation,it is definetely worth it: 
https://docs.microsoft.com/en-us/azure/machine-learning/how-to-configure-auto-features#featurization \
In our project I decided to pre-process the data in advance to reduce computation and be able to save some ressources.\
The picture below shows the data guardrail states that were proved during trainig of the dataset. As you can see and due to the pre-process mentioned above all the states were flagged as "Passed" indicating that no data problems were detected, thus no additional action was required either from side nor from the automatic featurization process. \
![alt text](https://github.com/MarceloLandaverde/udacity-capstone-project/blob/master/Pictures/Data_Guardrails.PNG)

- debug_log: \
Refers to the name of log file to write debug information to.If not specified, 'automl.log' is used

- automl_settings: \
Kwargs allowing us to pass keyworded variable length of arguments to the configuaration. In this case the AutoML Settings.

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
