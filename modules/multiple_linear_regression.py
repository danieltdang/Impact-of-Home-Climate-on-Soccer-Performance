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
    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
    print("[Multiple Linear Regression] Executing file...")
    # Load data
    print("[Multiple Linear Regression] Reading data...")
    df = pd.read_csv('matches.csv')

    print("[Multiple Linear Regression] Setting the features and target variables...")
    X = df[['Elevation (meters)', 'Temperature (c)', 'Humidity (g/kg)']]
    y = df['Away Avg Rating']

    # Box plots
    print("[Multiple Linear Regression] Processing Box plots...")
    fig1_1, axs1_1 = plt.subplots(1, figsize=(8, 2))
    sns.boxplot(x=df['Elevation (meters)'], ax=axs1_1)
    fig1_2, axs1_2 = plt.subplots(1, figsize=(8, 2))
    sns.boxplot(x=df['Temperature (c)'], ax=axs1_2)
    fig1_3, axs1_3 = plt.subplots(1, figsize=(8, 2))
    sns.boxplot(x=df['Humidity (g/kg)'], ax=axs1_3, )

    # Distribution plot
    print("[Multiple Linear Regression] Processing Distribution plots...")
    fig2, axs2 = plt.subplots(1)
    sns.histplot(df['Away Avg Rating'], ax=axs2, kde=True, stat="density", linewidth=0);
    plt.xlabel('Away Avg Rating')
    plt.ylabel('Density')  # The y-axis represents the density of the distribution
    plt.title('Distribution of Away Avg Rating')

    # Scatter plots
    print("[Multiple Linear Regression] Processing Scatter plots...")
    fig3_1, axs3_1 = plt.subplots(1, figsize=(8, 4))
    sns.scatterplot(df, x='Elevation (meters)', y='Away Avg Rating', ax = axs3_1)
    fig3_2, axs3_2 = plt.subplots(1, figsize=(8, 4))
    sns.scatterplot(df, x='Temperature (c)', y='Away Avg Rating', ax = axs3_2)
    fig3_3, axs3_3 = plt.subplots(1, figsize=(8, 4))
    sns.scatterplot(df, x='Humidity (g/kg)', y='Away Avg Rating', ax = axs3_3)

    # Heatmap plot
    print("[Multiple Linear Regression] Processing Heatmap...")
    fig4, axs4 = plt.subplots(1)
    sns.heatmap(df.corr(numeric_only = True), annot = True, cmap = 'coolwarm')

    # Save plots
    print("[Multiple Linear Regression] Saving plots into plots folder...")
    fig1_1.tight_layout()
    fig1_1.savefig('plots/box_plot_1.png')
    fig1_2.tight_layout()
    fig1_2.savefig('plots/box_plot_2.png')
    fig1_3.tight_layout()
    fig1_3.savefig('plots/box_plot_3.png')
    fig2.tight_layout()
    fig2.savefig('plots/distribution_plot.png')
    fig3_1.tight_layout()
    fig3_1.savefig('plots/scatter_plot_1.png')
    fig3_2.tight_layout()
    fig3_2.savefig('plots/scatter_plot_2.png')
    fig3_3.tight_layout()
    fig3_3.savefig('plots/scatter_plot_3.png')
    fig4.tight_layout()
    fig4.savefig('plots/heatmap.png')
    print("[Multiple Linear Regression]  Finished saving plots into plots folder.")

    # Multiple Multiple Linear Regression model
    print("[Multiple Linear Regression] Processing the multiple Multiple linear regression model...")
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state = 42)
    reg_model = LinearRegression().fit(X_train, y_train)
    print("-=-=-=-=-=-=-=-=-=-=-=-=-")
    print(f'Intercept: {reg_model.intercept_}')
    print(f'Coefficients: {reg_model.coef_}')
    print("-=-=-=-=-=-=-=-=-=-=-=-=-")
    list(zip(X, reg_model.coef_))

    y_pred = reg_model.predict(X_test)  
    x_pred = reg_model.predict(X_train) 

    reg_model_diff = pd.DataFrame({'Actual value': y_test, 'Predicted value': y_pred})

    mae = metrics.mean_absolute_error(y_test, y_pred)
    mse = metrics.mean_squared_error(y_test, y_pred)
    r2 = np.sqrt(metrics.mean_squared_error(y_test, y_pred))

    print("Multiple Multiple Linear Regression Model Evaluation:\n")
    print('Mean Absolute Error:', mae)
    print('Mean Square Error:', mse)
    print('Root Mean Square Error:', r2)
    print("-=-=-=-=-=-=-=-=-=-=-=-=-")


    print("\n \n [Multiple Linear Regression] Terminiating... \n \n")
    
if __name__ == "__main__":
    multiple_linear_regression()