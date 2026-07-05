import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.cluster import KMeans
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, classification_report

# Configure pandas display
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', 50)

# Configure matplotlib
plt.style.use('fivethirtyeight')
plt.rcParams['figure.figsize'] = (12, 8)

print("All required libraries imported successfully.")