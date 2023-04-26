import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
import io

def barv_npsmean_by(dataframe, axisX):
    buf = io.BytesIO()

    axisX_labels = dataframe.groupby([f"{axisX}"]).mean()["NPS interno"].index
    nps_mean_by_axisX = dataframe.groupby([f"{axisX}"]).mean()["NPS interno"].values

    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.bar(axisX_labels, nps_mean_by_axisX, color='#eead2d', edgecolor='black', linewidth= 2)
    ax.set_ylabel("NPS interno mensal médio")
    ax.set_yticks(np.array(range(0, 11, 1)))
    ax.set_title(f"Média de NPS Interno Mensal por {axisX}")
    fig.savefig(buf, format='png')
    plt.close(fig)
    return buf

def barv_npsmean_by_contract(dataframe, axisX):
    buf = io.BytesIO()

    axisX_labels = dataframe.groupby([f"{axisX}"]).mean()["NPS interno"].index
    nps_mean_by_axisX = dataframe.groupby([f"{axisX}"]).mean()["NPS interno"].values

    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.bar(axisX_labels, nps_mean_by_axisX, color='#add8e6', edgecolor='black', linewidth= 2)
    ax.set_ylabel("Nps medio mensal por setor")
    ax.set_yticks(np.array(range(0, 11, 1)))
    ax.set_title(f"Média de NPS Interno Mensal por {axisX}")
    fig.savefig(buf, format='png')
    plt.close(fig)
    return buf

def hist_nps(dataframe):
    buf = io.BytesIO()

    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.hist(dataframe["NPS interno"])
    ax.set_title("Distribuição do NPS interno mensal")
    ax.set_xlabel("Nps Interno")
    fig.savefig(buf, format='png')
    plt.close(fig)
    return buf

def mean_age(dataframe):
    buf = io.BytesIO()
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
  
    x = dataframe.groupby(['Setor']).count().index
    y = [34.625, 34.0, 28.61904761904762, 33.88235294117647]
    ax.barh(x, y, color= "#90ee90", edgecolor='black', linewidth= 2)

   # teste = dataframe.groupby('Setor').mean(numeric_only=True)['Idade'].values
   # y = teste.tolist()
    
    ax.set_title("Média das idades dos colaboradores por departamento")
    ax.set_xticks(np.array(range(18, 54, 4)))
    ax.set_xlabel('Media da idade em anos')
    ax.set_ylabel('Departamento')
    
    fig.savefig(buf, format='png')
    plt.close(fig)
    return buf

def mean_salary(dataframe):
    buf = io.BytesIO()
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)

    x1 = dataframe.groupby(['Setor']).mean().index
    y = [6250, 9325.71428571, 8828.57142857, 5664.70588235]
    ax.barh(x1, y,  color = "#ff7f00", edgecolor='black', linewidth= 2)

#    y = dataframe.groupby('Setor').mean(numeric_only=True)['Salario Bruto'].values

    ax.set_title("Folha salarial média de cada setor")
    ax.set_xticks(np.array(range(5000, 11000, 1000)))
    ax.set_xlabel("Quantidade em reais R$")
    ax.set_ylabel("Departamento")
    
    fig.savefig(buf, format='png')
    plt.close(fig)
    return buf

def colab_sector(dataframe):
    
    buf = io.BytesIO()
   
    labels = dataframe.groupby(['Setor']).mean().index
    sizes = dataframe.groupby(["Setor"]).count()["Cargo"]
    total = np.sum(sizes)
    explode = (0.1, 0.1, 0.1, 0.1)


    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels, autopct= lambda p: '{:.0f}'.format(p*total/100) + ' ({:.1f})%'.format(p), shadow=True, radius=3.5, textprops= {'size':'8'}, colors=['orange', 'blue', 'purple', 'red', 'green'], startangle=180)
    plt.title("Porcentagem de Colaboradores por setor")
    ax1.axis('equal')
    
    plt.savefig(buf, format='png')
    plt.close(fig1)
    return buf

def contracts(dataframe):

    buf = io.BytesIO()

    contracts = dataframe.groupby(["Tipo de Contratação"]).mean().index
    amount_peoples = dataframe.groupby(["Tipo de Contratação"]).count()["Cargo"].values
    total = np.sum(amount_peoples)
    explode = (0.1, 0.1, 0.1)

    fig2, ax2 = plt.subplots()
    ax2.pie(amount_peoples, explode=explode, labels=contracts, autopct= lambda p: '{:.0f}'.format(p*total/100) + ' ({:.1f})%'.format(p), shadow=True, radius=3.5, textprops= {'size':'8'}, colors=['purple', 'red', 'green'], startangle=180)
    plt.title("Porcentagem de Tipos de Contratos")
    ax2.axis('equal')

    plt.savefig(buf, format='png')
    plt.close(fig2)
    return buf
