import numpy as np 
import pandas as pd
import statsmodels.api as sm 
from statsmodels.formula.api import ols

def anova():
    print("--------------------------------------------------------")
    print("Starting the ANOVA tests.")
    # Load data
    print("Loading data from matches.csv...")
    df = pd.read_csv('matches.csv')

    print("Setting the features and target variables...")
    df.columns = df.columns.str.replace('Elevation (meters)', 'Elevation')
    df.columns = df.columns.str.replace('Temperature (c)', 'Temperature')
    df.columns = df.columns.str.replace('Humidity (g/kg)', 'Humidity')
    df.columns = df.columns.str.replace(' ', '_')

    # ANOVA
    print("Processing ANOVA...")
    model = ols('Away_Avg_Rating ~ Elevation + Temperature + Humidity', data=df).fit()
    anova_result = sm.stats.anova_lm(model, typ=2)

    # Printing results
    print("----------------------------")
    print("ANOVA results:\n")
    print(anova_result)
    print("----------------------------\n")

    print("Finished the ANOVA tests.")
    print("--------------------------------------------------------")

if __name__ == "__main__":
    anova()