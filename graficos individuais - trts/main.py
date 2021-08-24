import numpy as np

import matplotlib
import pandas as pd

matplotlib.use('TkAgg')
import matplotlib.pyplot as plt


def plot_graphs(x, y, num_trt):
    ax1.pie(x, labels=y, autopct='%1.1f%%',
            shadow=True, startangle=90)

    ax1.axis('equal')
    ax1.set_title(f'TRT{num_trt}', fontweight="bold", fontname="Times New Roman")

    plt.show()


def verification(dataframe, columns, row_position, col_position):
    if str(dataframe.iloc[row_position][columns[col_position]]).upper() == 'NAN':
        return 0
    else:
        return dataframe.iloc[row_position][columns[col_position]]


if __name__ == '__main__':
    df = pd.read_excel('tabela.xlsx')

    cols = df.columns
    labels = []
    for i in range(1, 6):
        labels.append(cols[i])

    print(labels)

    fig1, ax1 = plt.subplots()

    dados_uber = []
    dados_99 = []
    dados_ifood = []
    dados_loggi = []
    dados_rappi = []

    for i in range(24):
        dados_uber.append(df.iloc[i][labels[0]])
        dados_99.append(df.iloc[i][labels[1]])
        dados_ifood.append(df.iloc[i][labels[2]])
        dados_loggi.append(df.iloc[i][labels[3]])
        dados_rappi.append(df.iloc[i][labels[4]])

    index = int(input('Digite um trt: '))
    index -= 1
    if dados_uber[index] != 0 or dados_99[index] != 0 or dados_ifood[index] != 0 or dados_loggi[index] != 0 or dados_rappi[index] != 0:
        sizes = [dados_uber[index], dados_99[index], dados_ifood[index], dados_loggi[index], dados_rappi[index]]
        for x in range(len(sizes)-1):
            if sizes[x] == 0:
                del labels[x]
                del sizes[x]

        plot_graphs(sizes, labels, index)



