from modules import algorithms, matches
"""import pandas as pd
import numpy as np"""

"""features = pd.read_csv('matches.csv')
# One-hot encode the data using pandas get_dummies
features = pd.get_dummies(features['Koppen Climate'])
# Display the first 5 rows of the last 12 columns
print(features.iloc[::])"""

"""import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

# Load your dataset (replace 'matches.csv' with your actual file)
features = pd.read_csv('matches.csv')

# Assuming 'Avg Rating' is your target variable
X = features.drop(columns=['Away Avg Rating'])  # Features (excluding target)
y = features['Away Avg Rating']  # Target variable

# One-hot encode categorical features (like Koppen Climate)
X_encoded = pd.get_dummies(X, columns=['Koppen Climate'])

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X_encoded, y, test_size=0.2, random_state=42)

# Initialize and train the Random Forest model
rf_model = RandomForestRegressor(n_estimators=100, max_depth=10, random_state=42)
rf_model.fit(X_train, y_train)

# Example: Predict average rating for a new team with Koppen Climate 'Cfa'
new_team_koppen = 'Cfa'
new_team_encoded = pd.get_dummies(pd.DataFrame({'Koppen Climate': [new_team_koppen]}))
predicted_rating = rf_model.predict(new_team_encoded)

print(f"Predicted average rating for the new team: {predicted_rating[0]:.2f}")"""

import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split

# Step 1: Load data
df = pd.read_csv('matches.csv')

# Step 2: Preprocessing
climate_le = LabelEncoder()
team_le = LabelEncoder()

df['Koppen Climate'] = climate_le.fit_transform(df['Koppen Climate'])
df['Home Team'] = team_le.fit_transform(df['Home Team'])
df['Away Team'] = team_le.fit_transform(df['Away Team'])

# Step 3: Define the target variable
df['Winner'] = (df['Home Avg Rating'] < df['Away Avg Rating']).astype(int)

# Selecting features
features = ['Koppen Climate', 'Home Team', 'Away Team', 'Home Avg Rating', 'Away Avg Rating']
X = df[features]
y = df['Winner']

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 4: Train the Random Forest Model
clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X_train, y_train)

# Step 5: Predict on test data
predictions = clf.predict(X_test)

# Add predictions to test dataframe
test_df = X_test.copy()
test_df['Predicted Winner'] = predictions

# Output the predictions
test_df.to_csv('predictions.csv', index=False)
