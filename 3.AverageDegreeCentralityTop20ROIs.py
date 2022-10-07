"""
author: mhd
create time: 2022.9.15
description: use BInaryzation.py results to get top 20 ROIs which have most degree

* --- how to use it ---
[*important*] modify input_folder_path
* ---------------------
"""
import numpy as np
from scipy.io import loadmat

input_folder_path = "E:/0.MasterStudent/ADDetection/NetwrokConstruction/3.Results_Network_BD/Binaryzation_results/"

file_name_AD = "Binaryzation_LMCI_BinomialDistributionNetwork.mat"
file_name_CN = "Binaryzation_CN_BinomialDistributionNetwork.mat"
file_name_EMCI = "Binaryzation_EMCI_BinomialDistributionNetwork.mat"
file_name_LMCI = "Binaryzation_LMCI_BinomialDistributionNetwork.mat"

NetworkMatrix = [loadmat(input_folder_path + file_name_AD)["BDBinaryzationNetworkMatrix"],
                 loadmat(input_folder_path + file_name_CN)["BDBinaryzationNetworkMatrix"],
                 loadmat(input_folder_path + file_name_EMCI)["BDBinaryzationNetworkMatrix"],
                 loadmat(input_folder_path + file_name_LMCI)["BDBinaryzationNetworkMatrix"]]  # 0:AD 1:CN 2:EMCI 3:LMCI

size = np.shape(NetworkMatrix[0])
degree_list = np.array([np.zeros(size[0]), np.zeros(size[0]), np.zeros(size[0]), np.zeros(size[0])])
for i in range(0, 4):  # 统计四类人每个脑区的度
    for row in range(0, size[0]):
        for col in range(0, size[1]):
            if NetworkMatrix[i][row][col] != 0:
                degree_list[i][row] += 1
# print(degree_list[0])

# Average Degree Centrality
average_degree = (degree_list[0] + degree_list[1] + degree_list[2] + degree_list[3]) / (4 * size[0])
ans = np.argsort(-average_degree)  # 排序，返回从大到小的下标
with open('AverageDegreeCentralityTop20ROIs.csv', 'w') as f:
    f.write("begin_0_index,origin_index,centrality\n")
    for i in range(0, 20):
        f.write(str(ans[i]) + ",")
        if ans[i] < 200:  # 前200个起始下标为181
            f.write(str(ans[i] + 181) + "," + "%.3f" % average_degree[ans[i]] + "\n")
        else:  # 后200个起始下标为561
            f.write(str(ans[i] + 361) + "," + "%.3f" % average_degree[ans[i]] + "\n")
