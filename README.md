# Impact of Home Climate on Soccer Performance

## Köppen's Climate Classification System

| 1st             | 2nd                                                                        | 3rd                                                                 |
|-----------------|----------------------------------------------------------------------------|---------------------------------------------------------------------|
| A (Tropical)    | f (Rainforest) 
| |m (Monsoon)|
| |w (Savanna, dry winter)
| |s (Savanna, dry summer) |                                                                     |
| B(Dry)          | W (Arid Desert) | h (Hot)
||S (Semi-Arid or steppe)                                    | k (Cold)                                                    |
| C (Temperate)   | w (Dry winter) |a (Hot summer)
||f (No dry season) |b (Warm summer)
||s (Dry summer)                            | c (Cold summer)                      |
| D (Continental) | w (Dry winter) |a (Hot summer)
||f (No dry season) |b (Warm summer)
||s (Dry summer)|c (Cold summer)
||                            |    d (Very cold winter) |
| E (Polar)       |                                                                            | T (Tundra) 
|||F (Ice cap)                                              |

### Example Classification
- `Cfa` will be classified as `Temperate, no dry season, and hot summer`

## Getting Started

Follow these steps to run the code on your machine:

### Prerequisites
- Ensure you have Python 3.9 or above installed on your machine.
- Make sure you have the libraries in `requirements.txt` installed:

```bash
pip install -r requirements.txt
```

### Data Setup
- `matches.csv` is contained within the main directory of the repository
  - If missing, uncomment `matches.get_matches()` in `main.py` and then execute the code
- Ensure main file has access to read `matches.csv`
- If you want to setup matches from a different time and/or league, ensure to uncomment `matches.get_matches()` in `main.py` and update the URL (`https://www.fotmob.com/api/leagues?id={id}&ccode3={code}&season={year}`) on line 21 of `matches.py`

### Data Format
- `matches.csv` contains Koppen Climate, Elevation (meters), Temperature (c), Humidity (g/kg), Home Team, Away Team, Home Avg Rating, Away Avg Rating
- `combined.csv` contains Koppen Climate, Home Team, Away Team, Elevation (meters), Temperature (c), Humidity (g/kg), Actual Home Avg Rating, Predicted Home Avg Rating, Actual Away Avg Rating, Predicted Away Avg Rating

### Run the Code

Execute the `main.py` script to start running the Random Forest and Multiple Linear Regression models and the ANOVA test on the dataset:

```bash
python main.py
```

### Output

- Data Visualization plots can be found within the `/plots` directory

Example Output:

```yaml
    -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    [Random Forest] Executing file...
    [Random Forest] Loading data from matches.csv...
    [Random Forest] Split data into training and testing sets for Home Team
    [Random Forest] Trained the Random Forest Regressor for Home Team
    [Random Forest] Predicted on the test data for Home Team
    [Random Forest] Split data into training and testing sets for Away Team
    [Random Forest] Trained the Random Forest Regressor for Away Team
    [Random Forest] Predicted on the test data for Away Team      
    [Random Forest] Added predictions to the test dataframe       
    [Random Forest] Merged the dataframes based on common features
    [Random Forest] Saved the combined dataframe to a CSV file    
    [Random Forest] Evaluating the random forest model...
    -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    Random Forest Model Evaluation:

    True Positives (TP): 8
    False Positives (FP): 18
    True Negatives (TN): 47
    False Negatives (FN): 27
    TP/(FP+FN): 0.17777777777777778
    -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-


    [Linear Regression] Terminating...


    -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    [Multiple Linear Regression] Executing file...
    [Multiple Linear Regression] Reading data...
    [Multiple Linear Regression] Setting the features and target variables...
    [Multiple Linear Regression] Processing Box plots...
    [Multiple Linear Regression] Processing Distribution plots...
    [Multiple Linear Regression] Processing Scatter plots...
    [Multiple Linear Regression] Processing Heatmap...
    [Multiple Linear Regression] Saving plots into plots folder...
    [Multiple Linear Regression] Finished saving plots into plots folder.
    [Multiple Linear Regression] Processing the multiple Multiple linear regression model...
    -=-=-=-=-=-=-=-=-=-=-=-=-
    Intercept: 6.868754361971029
    Coefficients: [-0.00016047 -0.0027959   0.0059171 ]
    -=-=-=-=-=-=-=-=-=-=-=-=-
    Multiple Multiple Linear Regression Model Evaluation:

    Mean Absolute Error: 0.36543764161137554
    Mean Square Error: 0.19727387699870869
    Root Mean Square Error: 0.4441552397514958
    -=-=-=-=-=-=-=-=-=-=-=-=-


    [Multiple Linear Regression] Terminating...


    -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    [ANOVA] Executing Tests...
    [ANOVA] Reading data...
    [ANOVA] Setting the features and target variables...
    [ANOVA] Processing ANOVA...
    -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    ANOVA Results:
                    sum_sq     df         F    PR(>F)
    Elevation      1.390170    1.0  6.578776  0.010620
    Temperature    0.046874    1.0  0.221822  0.637867
    Humidity       0.005208    1.0  0.024648  0.875313
    Residual     102.485999  485.0       NaN       NaN
    -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-


    [ANOVA] Terminating...

```
