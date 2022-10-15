"""
author: mhd
create time: 2022.9.9
description: use the result of GammaMixtureEM.m to binarize the network

* --- how to use it ---
please pip install numpy, scipy
[*important*] modify file_name and Gamma_Result !!!
* ---------------------
"""

import os
import csv
import numpy as np
from scipy.io import loadmat, savemat


file_path = "E:/0.MasterStudent/ADDetection/NetwrokConstruction/3.Results_Network_BD/"
file_name = "LMCI_BinomialDistributionNetwork.mat"
lkjdclksdjf

Gamma_Result = 0.2794  # AD: 0.2984  CN: 0.2930  EMCI: 0.2693  LMCI: 0.2794
NetworkMatrix = loadmat(file_path + file_name)["BD_NetworkMatrix"]


size = np.shape(NetworkMatrix)
for row in range(0, size[0]):
    for col in range(0, size[1]):
        if NetworkMatrix[row][col] > Gamma_Result:
            NetworkMatrix[row][col] = 1
            # print(row, col)
        else:
            NetworkMatrix[row][col] = 0

# print(NetworkMatrix)
# savemat(file_path + "Binaryzation_results/Binaryzation_" + file_name, {'BDBinaryzationNetworkMatrix': NetworkMatrix})
with open(file_path + "Binaryzation_results/Binaryzation_" + file_name.split('.')[0] + ".csv", "w", newline='') as f:
    writer = csv.writer(f)  # 这一步是创建一个csv的写入器
    writer.writerows(NetworkMatrix)  # 写入样本数据
