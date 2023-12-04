import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn import linear_model
from sklearn.linear_model import LinearRegression
from sklearn import metrics
from sklearn.metrics import mean_squared_error, mean_absolute_error
from sklearn.model_selection import train_test_split, cross_val_score

def multiple_linear_regression():
    print("--------------------------------------------------------")
    print("Starting the evaluation of the multiple linear regression model.")
    # Load data
    print("Loading data from matches.csv...")
    df = pd.read_csv('matches.csv')
    print(df.describe())

    print("Setting the features and target variables...")
    X = df[['Elevation (meters)', 'Temperature (c)', 'Humidity (g/kg)']]
    y = df['Away Avg Rating']

    # Box plots
    print("Processing Box plots...")
    fig1, axs1 = plt.subplots(3)
    sns.boxplot(x=df['Elevation (meters)'], ax = axs1[0])
    sns.boxplot(x=df['Temperature (c)'], ax = axs1[1])
    sns.boxplot(x=df['Humidity (g/kg)'], ax = axs1[2])

    # Distribution plot
    print("Processing Distribution plots...")
    fig2, axs2 = plt.subplots(1)
    sns.histplot(df['Away Avg Rating'], ax=axs2, kde=True, stat="density", linewidth=0);
    plt.xlabel('Away Avg Rating')
    plt.ylabel('Density')  # The y-axis represents the density of the distribution
    plt.title('Distribution of Away Avg Rating')

    # Scatter plots
    print("Processing Scatter plots...")
    fig3, axs3 = plt.subplots(3, figsize=(10, 10))
    sns.scatterplot(df, x='Elevation (meters)', y='Away Avg Rating', ax = axs3[0])
    sns.scatterplot(df, x='Temperature (c)', y='Away Avg Rating', ax = axs3[1])
    sns.scatterplot(df, x='Humidity (g/kg)', y='Away Avg Rating', ax = axs3[2])

    # Heatmap plot
    print("Processing Heatmap...")
    fig4, axs4 = plt.subplots(1)
    sns.heatmap(df.corr(numeric_only = True), annot = True, cmap = 'coolwarm')

    # Save plots
    fig1.tight_layout()
    print("Saving plots into plots folder...")
    fig1.savefig('plots/box_plots.png')
    fig2.tight_layout()
    fig2.savefig('plots/distribution_plot.png')
    fig3.tight_layout()
    fig3.savefig('plots/scatter_plots.png')
    fig4.tight_layout()
    fig4.savefig('plots/heatmap.png')
    print("Finished saving plots into plots folder.")

    # Multiple Linear Regression model
    print("Processing the multiple linear regression model...")
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state = 42)
    reg_model = LinearRegression().fit(X_train, y_train)
    print('Intercept: ', reg_model.intercept_)
    list(zip(X, reg_model.coef_))

    y_pred = reg_model.predict(X_test)  
    x_pred = reg_model.predict(X_train) 

    reg_model_diff = pd.DataFrame({'Actual value': y_test, 'Predicted value': y_pred})

    mae = metrics.mean_absolute_error(y_test, y_pred)
    mse = metrics.mean_squared_error(y_test, y_pred)
    r2 = np.sqrt(metrics.mean_squared_error(y_test, y_pred))

    print("----------------------------")
    print("Multiple Linear Regression Model Evaluation:\n")
    print('Mean Absolute Error:', mae)
    print('Mean Square Error:', mse)
    print('Root Mean Square Error:', r2)
    print("----------------------------")
    
    print("Finished evaluating the multiple linear regression model.")
    print("--------------------------------------------------------")