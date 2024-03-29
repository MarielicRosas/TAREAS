# -*- coding: utf-8 -*-
"""Actividad 4.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1C8r6_vOmV7mryDBP-fNPGrH15M-mi4sl

# ***PARTE 1***
"""

from matplotlib import pyplot as plt

slices =[120, 80, 30, 20]
labels = ['CDIA','CONT','AUTO', 'INFO']
colors = ['#d6f8b8', '#f8b195', '#9ab5c1', '#f67280']

plt.pie(slices, labels = labels, colors = colors, wedgeprops={'edgecolor':'#c1867b'})

plt.title('Mi Gráfico de pastel', color = "#74698c")
plt.tight_layout()
plt.show()

"""# ***PARTE 2***"""

from matplotlib import pyplot as plt

slices = [59219, 55466, 47544, 36443, 35917]
labels = ['JavaScript', 'HTML/CSS', 'SQL', 'Python', 'Java']
explode = [0, 0, 0, 0.1, 0]

plt.pie(slices, labels = labels, explode = explode, shadow = True, startangle=120, autopct='%1.1f%%', wedgeprops={'edgecolor':'#c1867b'})

plt.title('Mi Gráfico de pastel', color = "#74698c")
plt.tight_layout()
plt.show()