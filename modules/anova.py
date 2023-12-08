import numpy as np 
import pandas as pd
import statsmodels.api as sm 
from statsmodels.formula.api import ols

def anova():
    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
    print("[ANOVA] Executing Tests...")

    print("[ANOVA] Reading data...")
    df = pd.read_csv('matches.csv')

    print("[ANOVA] Setting the features and target variables...")
    df.columns = df.columns.str.replace('Elevation (meters)', 'Elevation')
    df.columns = df.columns.str.replace('Temperature (c)', 'Temperature')
    df.columns = df.columns.str.replace('Humidity (g/kg)', 'Humidity')
    df.columns = df.columns.str.replace(' ', '_')

    # ANOVA
    print("[ANOVA] Processing ANOVA...")
    model = ols('Away_Avg_Rating ~ Elevation + Temperature + Humidity', data=df).fit()
    anova_result = sm.stats.anova_lm(model, typ=2)

    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
    print("ANOVA Results:")
    print(anova_result)
    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")

    print("\n \n [ANOVA] Terminating... \n \n")

if __name__ == "__main__":
    anova()