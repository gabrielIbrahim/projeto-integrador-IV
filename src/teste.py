import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
import io

def teste(dataframe):

    
    paises = dataframe.groupby(['Setor']).mean().index
    sizes = dataframe.groupby(["Setor"]).count()["Cargo"]

#    paises = ['angola' ,'senegal', 'luanda', 'zimbabue']
#    sizes = [8, 35, 21, 17]
    total = np.sum(sizes)
    explode = (0.1, 0.1, 0.1, 0.1)
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=paises, autopct= lambda p: '{:.0f}'.format(p*total/100) + ' ({:.1f})%'.format(p), shadow=True, radius=3.5, textprops= {'size':'8'}, colors=['orange', 'blue', 'purple', 'red', 'green'], startangle=180)
    ax1.axis('equal')
    plt.title("Porcentagem de Colaboradores por setor")
    ax1.axis('equal')
    return plt.show()

print(teste())

