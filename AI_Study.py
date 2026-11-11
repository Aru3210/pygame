import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math

from sklearn import datasets
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split


#Load Datasets
iris = datasets.load_iris()

print(type(iris))
