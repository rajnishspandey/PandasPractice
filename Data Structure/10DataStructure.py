"""
Create a DataFrame from a CSV file containing information about movies (Title, Genre, Rating). 
Select and display the movies with a rating higher than a certain threshold.
"""
import pandas as pd

df = pd.read_csv("Data Structure/movies.csv")
print(df)

threshold = 8

df = df[df["IMDB_Rating"]>threshold]
print(df)