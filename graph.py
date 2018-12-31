import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
import sys

if len(sys.argv) > 1:
    todo = sys.argv[1]
else:
    todo = "both"


#parse csv file
dataset = pd.read_csv("data.csv") 
#print(dataset.describe())

#create a subset and preform operations on it as descripbed in the problem
#i.e get what we need
#get the mean of the dataset based on the group we made before
purpose_mean = dataset.groupby("purpose").mean()[["int_rate"]]

# Plot 
bar_plot = purpose_mean.unstack().plot(kind='bar',title="Mean Intrest Rate Per Purpose",figsize=(8, 4))
bar_plot.set_xlabel(purpose_mean.index.name)
bar_plot.set_ylabel("mean(int_rate)")
#plt.show()

if todo == "graph":
  plt.show()
elif todo == "table":
  print(purpose_mean)
else:
  print(purpose_mean)
  plt.show()