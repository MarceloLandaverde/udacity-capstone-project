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

![alt text]()



### Access
*TODO*: Explain how you are accessing the data in your workspace.

## Automated ML
*TODO*: Give an overview of the `automl` settings and configuration you used for this experiment

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
