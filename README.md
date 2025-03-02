# product_engagement_prediction_model
This classification model predicts customer subscription engagement with a new banking product.

# Overview
This machine-learning project aims to predict whether customers will subscribe to a term deposit based on their demographics and banking behavior. The model uses a dataset based on a bank's marketing campaign and utilises Random Forest Classifier and XGBoost Classifier to make predictions.

# Dataset
The dataset used in this project is bank.csv, which contains information about customers and their responses to a marketing campaign. The dataset includes the following features:

Customer Information: Age, job, marital status, education level, etc.
Financial Information: Balance, housing loan status, personal loan status, etc.
Campaign Information: Duration of contact, number of contacts, outcome of previous campaigns, etc.
Target Variable: deposit (whether the customer subscribed to a term deposit: yes or no).

The dataset contains 11,162 rows and 17 columns.

# Set up
To set up and run the model locally, follow these steps:

1. Clone the repository and navigate to the product_engagement_prediction_model directory:
git clone https://github.com/aanshulls/product_engagement_prediction_model.git
cd product_engagement_prediction_model

2. Copy over the Dataset:
Place the bank.csv file in the data/ directory. The notebook will load the dataset from this location.

4. Install dependencies:
Ensure you have Python 3.8+ installed. Install the required libraries using:
pip install -r requirements.txt

5. Run the Jupyter Notebook:
Open the notebook src/code.ipynb to explore the code, run the model, and visualise the results:
jupyter notebook src/code.ipynb

# Exploratory Data Analysis (EDA)
The EDA process involved:
- Understanding the dataset structure and features.
- Visualising both categorical and numerical features.
- Identifying relationships between features and the target variable (deposit).
- Handling missing values and outliers.

Key insights from EDA:
- Most customers contacted were in management roles, married, and had a secondary education.
- Retired customers showed the highest interest in term deposits.
- Customers with longer contact durations were more likely to subscribe to the product.

# Feature Engineering
The following steps were performed to prepare the data for modeling:

- Dropping Irrelevant Features: Features like default and pdays were removed due to low relevance or high outliers.
- Handling Categorical Variables: Categorical features were converted into numerical format using one-hot encoding.
- Boolean Conversion: Boolean features like housing and loan were converted to binary values (0 or 1).
- Outlier Removal: Outliers in features like campaign and previous were removed to improve model performance.

## Model Selection and Training
Two models were evaluated:
- Random Forest Classifier
- XGBoost Classifier

# Hyperparameter tuning 
- Grid Search: Used to find the best hyperparameters for both models.

# Final Model
The XGBoost Classifier was selected as the final model due to its higher accuracy score. The optimal hyperparameters were:
- learning_rate: 0.1165
- n_estimators: 156
- max_depth: 7
- subsample: 0.8217
- colsample_bytree: 0.6069

# Model Performance
The final model achieved the following performance metrics on the test set:

- Accuracy: 85.61%
- Precision: 82% (class 1), 89% (class 0)
- Recall: 89% (class 1), 83% (class 0)
- F1-Score: 85% (class 1), 86% (class 0)


