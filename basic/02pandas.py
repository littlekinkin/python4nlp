import urllib
import urllib.request

def load_data():
    url = "https://raw.githubusercontent.com/GokuMohandas/practicalAI/master/data/titanic.csv"
    resp = urllib.request.urlopen(url)
    html = resp.read()
    with open('titanic.csv', 'wb') as f:
        f.write(html)

import pandas as pd

'''
header : int, list of int, default ‘infer’
Row number(s) to use as the column names, and the start of the data. Default behavior is to infer the column names: if no names are passed the behavior is identical to header=0 and column names are inferred from the first line of the file, if column names are passed explicitly then the behavior is identical to header=None. Explicitly pass header=0 to be able to replace existing names. The header can be a list of integers that specify row locations for a multi-index on the columns e.g. [0,1,3]. Intervening rows that are not specified will be skipped (e.g. 2 in this example is skipped). Note that this parameter ignores commented lines and empty lines if skip_blank_lines=True, so header=0 denotes the first line of data rather than the first line of the file.
'''
df = pd.read_csv('titanic.cvs', header=0)
'''
DataFrame, head default 5
'''
df.head()

df.describe()
df.hist()
df['name'].hist()


