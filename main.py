from modules import matches, anova as a, multiple_linear_regression as mlr, random_forest as rf
import time

"""start_time = time.time()
matches.get_matches()
end_time = time.time()
print(f"get_matches() took {end_time - start_time} seconds.")"""

start_time = time.time()
rf.random_forest()
end_time = time.time()
print(f"Random Forest took {round(end_time - start_time, 4)} seconds.")

start_time = time.time()
mlr.multiple_linear_regression()
end_time = time.time()
print(f"Multiple Linear Regression took {round(end_time - start_time, 4)} seconds.")

start_time = time.time()
a.anova()
end_time = time.time()
print(f"ANOVA took {round(end_time - start_time, 4)} seconds.")