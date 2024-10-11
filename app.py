from dash import Dash, html, dcc, callback, Input, Output
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt
import plotly.express as px

app = Dash(__name__, external_stylesheets=[dbc.themes.CERULEAN])
app.title = "Assignment3"
server = app.server

  df = pd.read_csv("/kaggle/input/gdp-of-all-countries19602020/gdp_1960_2020.csv")

df.info()
df.head()
df.tail()

subset_2000 = df[df['year'].isin([2000])]
average_2000 = np.mean(subset_2000['gdp'])
subset_2010 = df[df['year'].isin([2010])]
subset_2020 = df[df['year'].isin([2020])]
subset_2020.info()

subset_2020.head()
subset_2020.tail()
average_2020 = np.mean(subset_2020['gdp'])
print(average_2020)
subset_Malaysia = df[df['country'].isin(["Malaysia"])]

plt.scatter(subset_Malaysia['year'], subset_Malaysia['gdp'])
px.scatter(subset_Malaysia, x="year", y="gdp")
subset_China = df[df['country'].isin(["China"])]
plt.scatter(subset_China['year'], subset_China['gdp'])
subset_China = df[df['country'].isin(["Indonesia"])]
plt.scatter(subset_China['year'], subset_China['gdp'])
plt.bar(subset_2020['country'], subset_2020['gdp'])
px.bar(subset_2020, x="country", y="gdp")


subset_2020_Asia = subset_2020[subset_2020['state'].isin(["Asia"])]
subset_2020_Africa = subset_2020[subset_2020['state'].isin(["Africa"])]
subset_2020_America = subset_2020[subset_2020['state'].isin(["America"])]
subset_2020_Europe = subset_2020[subset_2020['state'].isin(["Europe"])]
subset_2020_Oceania = subset_2020[subset_2020['state'].isin(["Oceania"])]

pie_data = [sum(subset_2020_Asia['gdp']),sum(subset_2020_Africa['gdp']),sum(subset_2020_America['gdp']),sum(subset_2020_Europe['gdp']),sum(subset_2020_Oceania['gdp'])];
mylabels = ["Asia", "Africa", "America", "Europe","Oceania"]
plt.pie(pie_data, labels = mylabels)
pie_df = {'Continent': mylabels,
        'GDP': pie_data}
px.pie(pie_df,values="GDP",names="Continent")
