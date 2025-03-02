## Product Engagement Prediction Model
This classification project aims to predict customer subscription engagement with a new banking product using machine-learning techniques.

## Problem Statement and Project Overview
Within the competitive banking sector it is essential to understand customer engagement with new product is essential to optimise marketing strategies. However, predicting customer engagement is difficult due to  varied demographical, behavioural, and financial data.

This project aims to develop a machine-learning model to predict customer engagement with a new term loan introduced by a bank using customer historical data. By accurately classifying customers into engaged and non-engaged categories the model will help:
- Optimise marketing strategies to improve efficiency.
- Enhance sales strategies to focus on high-probably customers
- Improve customer experience by offering targeted innovative products to the correct demographic

The model is trained using customer data and leverages algorithms such as Random Forest Classifier and XGBoost Classifier for predictive accuracy, with the project goal to provide data-driven insights driving higher engagement rates for improved business outcomes.

## Dataset
The dataset used in this project is bank.csv, which contains information about customers and their responses to a marketing campaign. The dataset includes the following features:

**Age:** Numeric
- **Job:** Categorical (e.g., 'admin.', 'technician', etc.)
- **Marital Status:** Categorical (e.g., 'married', 'single')
- **Education Level:** Categorical (e.g., 'secondary', 'tertiary')
- **Balance:** Numeric
- **Housing Loan Status:** Binary ('yes'/'no')
- **Personal Loan Status:** Binary ('yes'/'no')
- **Contact Duration:** Numeric (duration of the last contact in seconds)
- **Number of Contacts:** Numeric (number of contacts performed during this campaign)
- **Previous Outcome:** Categorical (outcome of the previous marketing campaign)
- **Target Variable:** Binary ('yes'/'no' indicating subscription to a term deposit)


The dataset contains 11,162 rows and 17 columns.

## Setup Instructions
To set up and run the model locally, follow these steps:

1. Clone the repository and navigate to the product_engagement_prediction_model directory:
git clone https://github.com/aanshulls/product_engagement_prediction_model.git
cd product_engagement_prediction_model

2. Create and activate a virtual environment
python3 -m venv env
sourve env/bin/activate

3. Install dependencies:
Ensure you have Python 3.8+ installed. Install the required libraries using:
pip install -r requirements.txt

## Data Preprocessing and Exploratory Data Analysis (EDA)
The EDA process involved:
- Understanding the dataset structure and visualisation.
- Visualising  categorical and numerical features to find trends and relationships with the target variable (deposit).
- Handling missing values and outliers.

Key insights from EDA:
- Most customers contacted were in management roles, married, and had a secondary education.
- Retired customers showed the highest interest in term deposits.
- Customers with longer contact durations were more likely to subscribe to the product.

## Feature Engineering
The following steps were performed to prepare the data for modeling:

- Dropping irrelevant features: default and pdays were removed due to low relevance or high outliers.
- Handling categorical variables: Categorical features were converted into a numerical format using one-hot encoding.
- Boolean conversion: Boolean features like housing and loan were converted to binary values (0 or 1).
- Outlier removal: Outliers in features like campaign and previous were removed to improve model performance.

## Model Selection and Evaluation
- Models implemented: Random Forest Classifier, XGBoost Classifier
- Hyperparameter tuning: GridSearchCV to automate tuning via hyperparameter grids.
- Evaluation metrics: Accuracy, Precision, Recall and F1-Score
- Cross-validation: Utilising 5-fold cross-validation to help reduce overfitting for model robustness.

## Results
**Random Forest Classifier**
- Accuracy: 0.85
- Precision: 0.85
- Recall: 0.85
- F1-Score: 0.85

**XGBoost Classifier**
- Accuracy: 0.86
- Precision: 0.86
- Recall: 0.86
- F1-Score: 0.86

## Final Model
The XGBoost Classifier was selected as the final model due to its higher accuracy score. The optimal hyperparameters were:
- learning_rate: 0.1165
- n_estimators: 156
- max_depth: 7
- subsample: 0.8217
- colsample_bytree: 0.6069

## Next Steps
Model Improvements:
- Further hyperparameter tuning using Bayesian Optimization.
- Utilising different models such as LightGBM.

Deployment:
- Converting the model into a FastAPI web app
- Deploying onto AWS

## Contributing
Contributions welcomed - please fork the repository 




