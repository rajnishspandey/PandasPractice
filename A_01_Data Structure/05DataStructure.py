"""
Create a Series with student names as the index and their exam scores.
Find the mean score and list the students who scored above the mean.
"""
import pandas as pd

students = {"Rajnish":80,"Manish":70,"Amit":70,"Prince":75}

series = pd.Series(students)

mean_scope = series.mean()
print(mean_scope)

above_mean = series[series>mean_scope]
print(above_mean)
