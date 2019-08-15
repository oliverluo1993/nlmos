#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 30 15:08:31 2019

@author: zilingluo
"""

from matplotlib import pyplot as plt
import pandas as pd
import numpy as np


xls = pd.ExcelFile('/Users/zilingluo/Documents/GitHub/nlmos/figure.xlsx')

xls_sheet_names = ['Water', 'Diborane', 'Carborane', 'Propene', 'Benzene', 
                   'Heptane', 'Icosane', 'Graphene']



fig, axes = plt.subplots(2,4, figsize=(16,8))
figure_num = 0

for ax_row in axes:
    for ax in ax_row:
        df = pd.read_excel (xls, sheet_name=xls_sheet_names[figure_num])
        x = df[["alpha"]]
        y = df[["LOCALIZATION"]]
        z = df[["DETERMINANT"]]
        x_list = x.values.tolist()
        new_x_list = np.log(x_list)
        y_list = y.values.tolist()
        new_y_list = np.log(y_list)
        z_list = z.values.tolist()
        color = 'tab:red'
        ax.plot(new_x_list, y_list, color=color, marker='.', label='Localization')
        ax.tick_params(axis='y', labelcolor=color)
        ax2 = ax.twinx()
        color = 'tab:blue'
        ax2.plot(new_x_list, z_list, color=color, marker='.', label='Determinant')
        ax2.tick_params(axis='y', labelcolor=color)
        plt.ylim(0.0, 1.1)
        plt.yticks(np.arange(0.0, 1.1, 0.2))
        axes = plt.gca()
        axes.invert_xaxis()
        ax.set_title(xls_sheet_names[figure_num], fontsize=20)
        figure_num += 1
        
fig.text(0.5, 0.001, 'log(α)', ha='center', va='center', fontsize=12)
fig.text(0.001, 0.5, 'LOCALIZATION FUNCTIONAL', ha='center', va='center',
         rotation='vertical', color='tab:red', fontsize=12)
fig.text(0.999, 0.5, 'DETERMINANT det(σ)', ha='center', va='center',
         rotation='vertical', color='tab:blue', fontsize=12)
#axes.set_xlabel('LOCALIZATION FUNCTIONAL')
#axes.set_ylabel('DETERMINANT det(σ')
plt.tight_layout()
plt.show()

fig.savefig('1.pdf', dpi=300, bbox_inches = "tight")