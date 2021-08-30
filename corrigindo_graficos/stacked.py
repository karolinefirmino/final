
# importing packages
import pandas as pd
import matplotlib.pyplot as plt

# load dataset
df = pd.read_excel("stack_bar_ceat.xlsx", header=0, delim_whitespace=True)
headers = ['TRIBUNAIS','UBER','TAXIS99','IFOOD','LOGGI', 'RAPPI']
df.columns = headers 
df.to_csv('newsource.txt')


#trts = ['TRT1', 'TRT2', 'TRT3', 'TRT4', 'TRT5', 'TRT6', 'TRT7', 'TRT8', 'TRT9', 'TRT10', 'TRT11', 'TRT12','TRT13', 'TRT14', 'TRT15', 'TRT16', 'TRT17', 'TRT18', 'TRT19', 'TRT20', 'TRT21', 'TRT22', 'TRT23', 'TRT24']

# plot a Stacked Bar Chart using matplotlib
df_1 = pd.read_csv('newsource.txt')
df_1.plot(
    x = 'TRIBUNAIS',
    kind = 'bar',
    stacked = True,
    title = 'Processos - TRTs',
    mark_right = True)

#plt.show()

import plotly.graph_objects as go
from kaleido.scopes.plotly import PlotlyScope
scope = PlotlyScope(
    plotlyjs="https://cdn.plot.ly/plotly-latest.min.js")

x=df_1['TRIBUNAIS']
fig = go.Figure(go.Bar(x=x, y=df_1['UBER'], name='Uber'))
fig.add_trace(go.Bar(x=x, y=df_1['TAXIS99'], name='99Taxis'))
fig.add_trace(go.Bar(x=x, y=df_1['IFOOD'], name='Ifood'))
fig.add_trace(go.Bar(x=x, y=df_1['LOGGI'], name='Loggi'))
fig.add_trace(go.Bar(x=x, y=df_1['RAPPI'], name='Rappi'))

fig.update_layout(barmode='stack')
fig.show()

with open("processos_grafico.jpg", "wb") as f:
    f.write(scope.transform(fig, format="jpg"))


fig.write_html("processos_grafico_01_total.html")
