import pandas as pd #failuapstrādei
import matplotlib.pyplot as plt # grafiki
import seaborn as sb # vizualizācijas

sb.set_style('whitegrid')
plt.rcParams['figure.figsize'] = (15,10)

fails1 = 'auto_simple.csv'
fails2 = 'auto_imports.csv'

def heat_map(datne):
    datu_fails = pd.read_csv(datne).select_dtypes('number')
    sb.heatmap(datu_fails.corr(), annot=True, cmap='magma')
    plt.show()
    return

def distrubution(datne, kolonna):
    datu_fails = pd.read_csv(datne)
    sb.histplot(datu_fails[kolonna], color="r")
    plt.show()



distrubution(fails1,"Car")