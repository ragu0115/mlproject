# End to End Machine Learning Project

Dataset Source Link : [https://www.kaggle.com/datasets/shivamb/machine-predictive-maintenance-classification/data](https://archive.ics.uci.edu/dataset/601/ai4i+2020+predictive+maintenance+dataset)https://archive.ics.uci.edu/dataset/601/ai4i+2020+predictive+maintenance+dataset

# Approach for the project 

Modularly Programmed the following in created Anaconda Development Environment

1. Data Ingestion : 
    * In Data Ingestion phase the data is first read as csv. 
    * Then the data is split into training and testing and saved as csv files.

2. Data Transformation : 
    * In this phase a ColumnTransformer Pipeline is created.
    * for Numeric Variables first SimpleImputer is applied with strategy median , then Standard Scaling is performed on numeric data.
    * for Categorical Variables SimpleImputer is applied with most frequent strategy, then ordinal encoding performed , after this data is scaled with Standard Scaler.
    * This preprocessor is saved as pickle file.

3. Model Training : 
    * In this phase base model is tested with several different models. Models used Linear Regression, Lasso, Ridge, K-Nearest Neighbours, Decision Tree, Random Forest, XGBRegressor, and CatBoost.
    * After this hyperparameter tuning is performed on the models the best model is selected.
    * This model is saved as pickle file.

4. Prediction Pipeline : 
    * This pipeline converts given data into dataframe and has various functions to load pickle files and predict the final results in python.

5. Flask App creation : 
    * Flask app is created with User Interface to predict Machine Success or Failure inside a Web Application.
