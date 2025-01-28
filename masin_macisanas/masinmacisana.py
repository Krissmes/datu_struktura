import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb
import pickle

from termcolor import colored as cl
from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LinearRegression
from sklearn.metrics import explained_variance_score as evs
from sklearn.metrics import r2_score as r2

def sagatavot_datus(fails, kolona_x, kolona_y):
    datu_fails = pd.read_csv(fails)
    datu_fails.dropna(inplace=True)
    x_var = datu_fails[kolona_x]
    y_var = datu_fails[kolona_y]
    x_train, x_test, y_train, y_test = train_test_split(x_var, y_var, test_size=0.2, random_state=0)
    
    return (x_train, x_test, y_train, y_test)


def modela_kvalitate(y_test, results):
    print(cl(f"Dispersija: {evs(y_test, results)}",'red', attrs=['bold']))
    print(cl(f"Kvadrātiskā novirze: {r2(y_test, results)}",'yellow', attrs=['bold']))
    return


def trenet_modeli(modelis, x_train, y_train):
    modelis.fit(x_train, y_train)
    return modelis


def parbaudit_modeli(modelis, x_test):
    results = modelis.predict(x_test)
    return results


datne1 = "auto_simple.csv"
kol_x1 = ['Volume','Weight']
kol_y1 = ['CO2']



x_train, x_test, y_train, y_test = sagatavot_datus(datne1, kol_x1, kol_y1)


modelis = LinearRegression()

modelis = trenet_modeli(modelis, x_train, y_train)
rezultats = parbaudit_modeli(modelis, x_test)

modela_kvalitate(y_test, rezultats)