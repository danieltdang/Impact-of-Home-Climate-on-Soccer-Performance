import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
    
def anova():
    pass

def multiple_linear_regression():
    pass

def random_forest():
    # Load data
    print("Loading data from matches.csv...")
    df = pd.read_csv('matches.csv')


    climate_le = LabelEncoder()
    team_le = LabelEncoder()

    df['Koppen Climate'] = climate_le.fit_transform(df['Koppen Climate'])
    df['Home Team'] = team_le.fit_transform(df['Home Team'])
    df['Away Team'] = team_le.fit_transform(df['Away Team'])

    # Selecting features for the model
    features = ['Koppen Climate', 'Home Team', 'Away Team']
    X = df[features]

    # Separate targets for home and away ratings
    y_home = df['Home Avg Rating']
    y_away = df['Away Avg Rating']

    X_train_home, X_test_home, y_train_home, y_test_home = train_test_split(X, y_home, test_size=0.2, random_state=42)
    print("Split data into training and testing sets for Home Team")

    # Train the Random Forest Regressor for Home Team
    clf_home = RandomForestRegressor(n_estimators=100, random_state=42)
    clf_home.fit(X_train_home, y_train_home)
    print("Trained the Random Forest Regressor for Home Team")

    # Predict on the test data for Home Team
    home_predictions = clf_home.predict(X_test_home)
    print("Predicted on the test data for Home Team")

    # Split data into training and testing sets for Away Team
    X_train_away, X_test_away, y_train_away, y_test_away = train_test_split(X, y_away, test_size=0.25, random_state=42)
    print("Split data into training and testing sets for Away Team")

    # Train the Random Forest Regressor for Away Team
    clf_away = RandomForestRegressor(n_estimators=100, random_state=42)
    clf_away.fit(X_train_away, y_train_away)
    print("Trained the Random Forest Regressor for Away Team")

    away_predictions = clf_away.predict(X_test_away)
    print("Predicted on the test data for Away Team")

    # Add predictions to the test dataframe
    test_home_df = pd.DataFrame(X_test_home, columns=features)
    test_home_df['Actual Home Avg Rating'] = y_test_home
    test_home_df['Predicted Home Avg Rating'] = home_predictions

    test_away_df = pd.DataFrame(X_test_away, columns=features)
    test_away_df['Actual Away Avg Rating'] = y_test_away
    test_away_df['Predicted Away Avg Rating'] = away_predictions
    print("Added predictions to the test dataframe")

    # Merge the dataframes based on the common features
    combined_df = pd.merge(test_home_df, test_away_df, on=features)
    print("Merged the dataframes based on common features")

    # Save the combined dataframe to a CSV file
    combined_df.to_csv('combined.csv', index=False)
    print("Saved the combined dataframe to a CSV file")

    # Reading in Data from 'Combined.csv' and focusing four main fields
    cr = pd.read_csv('combined.csv', usecols=['Actual Home Avg Rating','Predicted Home Avg Rating', 'Actual Away Avg Rating', 'Predicted Away Avg Rating'])

    # Calculating tp, fp, tn, and fn values via pandas 
    print("Evaluating the random forest model...")
    tp = len(cr[((cr['Predicted Away Avg Rating'] > cr['Predicted Home Avg Rating']) & (cr['Actual Away Avg Rating'] > cr['Actual Home Avg Rating']))])
    fp = len(cr[((cr['Predicted Away Avg Rating'] > cr['Predicted Home Avg Rating']) & (cr['Actual Away Avg Rating'] < cr['Actual Home Avg Rating']))])
    tn = len(cr[((cr['Predicted Away Avg Rating'] < cr['Predicted Home Avg Rating']) & (cr['Actual Away Avg Rating'] < cr['Actual Home Avg Rating']))])
    fn = len(cr[((cr['Predicted Away Avg Rating'] < cr['Predicted Home Avg Rating']) & (cr['Actual Away Avg Rating'] > cr['Actual Home Avg Rating']))])

    ratio = tp / (fp + fn) if (fp + fn) > 0 else 'Undefined' 

    print("----------------------------")
    print(f"True Positives (TP): {tp}")
    print(f"False Positives (FP): {fp}")
    print(f"True Negatives (TN): {tn}")
    print(f"False Negatives (FN): {fn}")
    print(f"TP/(FP+FN): {ratio}")
    print("----------------------------")

    print("Finished evaluating the random forest model")