from bs4 import BeautifulSoup
import pandas as pd
import requests
from io import StringIO
from datetime import datetime
from datetime import date
import datetime
from dateutil.relativedelta import relativedelta
from datetime import datetime, timedelta
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_selection import RFE


from sklearn import linear_model
from sklearn import svm
from itertools import combinations
import itertools
import numpy as np
import scipy as sp
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.feature_selection import VarianceThreshold

from math import radians, cos, sin, asin, sqrt, atan, isclose
# from OddsCalculator import OddsCalculator as util
import collections
import matplotlib.pyplot as plt
from time import time, ctime
from pandas.io.json import json_normalize
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


pd.set_option('display.max_rows', 300)
pd.set_option('display.max_columns', 300)
pd.set_option('display.max_colwidth', -1)

n_5ft = pd.read_csv(r'C:\Users\irfan\mma_ml\historical_data\n_5_ft.csv')

full_training = n_5ft[['a_HT', 'a_KD', 'a_body_stra', 'a_body_strl', 'a_clinch_stra', 'a_clinch_strl', 'a_ctrl_time', 'a_dist_stra', 'a_dist_strl', 'a_ground_stra', 'a_ground_strl', 'a_head_stra', 'a_head_strl', 'a_is_Open-Stance', 'a_is_Orthodox', 'a_is_Sideways', 'a_is_Southpaw', 'a_is_Switch', 'a_leg_stra', 'a_leg_strl', 'a_reach', 'a_ssa', 'a_ssl', 'a_str', 'a_stra', 'a_subatt', 'a_td', 'a_tda', 'a_weight', 'a_imp_proba', 'b_HT', 'b_KD', 'b_body_stra', 'b_body_strl', 'b_clinch_stra', 'b_clinch_strl', 'b_ctrl_time', 'b_dist_stra', 'b_dist_strl', 'b_ground_stra', 'b_ground_strl', 'b_head_stra', 'b_head_strl', 'b_imp_proba', 'b_is_Open-Stance', 'b_is_Orthodox', 'b_is_Sideways', 'b_is_Southpaw', 'b_is_Switch', 'b_leg_stra', 'b_leg_strl', 'b_reach', 'b_ssa', 'b_ssl', 'b_str', 'b_stra', 'b_subatt', 'b_td', 'b_tda', 'b_weight', '5_rf']]

outcomes = n_5ft[['a_outcome']]

for stat in list(full_training):
   full_training['{0}'.format(stat)] =  full_training['{0}'.format(stat)].fillna(0)
full_training = full_training.replace([np.inf, -np.inf], 0)

train_X, test_X, train_y, test_y = train_test_split(full_training, outcomes, test_size = 0.3, random_state = 42)

logistic_regression = linear_model.LogisticRegression()

scaler = StandardScaler()

scaler.fit(train_X)
train_X = scaler.transform(train_X)
test_X = scaler.transform(test_X)

logistic_regression.fit(train_X, train_y)
predictions = logistic_regression.predict(test_X)
print(accuracy_score(predictions,test_y))
