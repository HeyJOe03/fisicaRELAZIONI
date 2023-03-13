import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from interpolazione2 import RettaInterpolata

import os

dir_path = os.path.dirname(os.path.realpath(__file__))
FILE = dir_path + '/../CSV/' + 'parabole.csv'
fr = pd.read_csv(FILE)

d = np.array(fr['d1(cm)'])
print(d)
t1 = np.array(fr['t1'])
t2 = np.array(fr['t2'])

plt.plot(d,t1,label="t1")
plt.plot(d,t2,label='t2')
plt.legend()
plt.xticks(d)
plt.show()