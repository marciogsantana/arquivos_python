# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 22:21:10 2019

@author: Marcio Gomes de Sant
"""

import pandas as pd
import numpy as np

#nota = pd.read_table('nota.csv')
#produtos = pd.read_table('produtos.csv')
#nota = pd.read_table('apenas_peixes_codigo.csv')
#produto = pd.read_table('apenas_peixes_produtos.csv')

nota = pd.read_table('relatorio_notas.csv')
produtos = pd.read_table('relatorio_vendas.csv')

arquivo = open('teste1.txt', 'w') 


nota = nota.values.tolist()


  # converte dataframe em lista
produto = produtos.values.tolist()  # converte dataframe em lista







indice = 0

while (indice < nota.__len__()):    # tamanho do vetor

  if (indice != nota.__len__() - 1):    # tamanho do vetor menos 1


    if (nota[indice] == nota[indice + 1]):

        arquivo.writelines(produto[indice])
        arquivo.write(';')
        arquivo.writelines(produto[indice + 1])
        
        indice = indice + 2

        if (indice < nota.__len__()):   # tamanho do vetor

            if(nota[indice] == nota[indice -1]):

                 arquivo.write(';')
            else:
                 arquivo.write('\n')
        else:

            print("fim do programa")

    elif (nota[indice] == nota[indice - 1]):

        arquivo.writelines(produto[indice])
        arquivo.write('\n')
        indice = indice + 1



    else:

        arquivo.writelines(produto[indice])
        arquivo.write('\n')
        indice = indice + 1
  else:

      arquivo.writelines(produto[indice])
      print("fim do programa")
      indice = indice + 1



    # while for i in produtos:

# indice_anterior = nota[i]
# while (indice_anterior == nota[i]):
# itens = produtos[i]
# arquivo.write('produtos[i]' +',')
#    i = i+1
#  arquivo.write('\n')
#  arquivo.close()
# itens = produtos[i]
# print(itens)
# arquivo.writelines(itens + ',' + '\n')
arquivo.close()

#fim

