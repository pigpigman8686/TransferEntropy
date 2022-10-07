"""
author: mhd
create time: 2022.9.9
description: use binomial distribution build a brain network (642 400*400 --> 4 400*400)

* --- how to use it ---
please pip install numpy, scipy
[*important*] modify input_folder_path and group !!!
* ---------------------
"""
import os
import numpy as np
from scipy.io import loadmat, savemat


input_folder_path = "E:/0.MasterStudent/ADDetection/NetwrokConstruction/1.Ridgep_AD_Network_Schaefer/"
output_folder_path = "E:/0.MasterStudent/ADDetection/NetwrokConstruction/3.Results_Ridgep_Network_BD/"


group_data = np.zeros((400, 400))
files = os.listdir(input_folder_path)

group = "AD"

i = 1
for file in files:
    print("NO: ", i, end='  ')

    print(file, "processing....")

    # 读取文件并截取
    mat_data = loadmat(os.path.join(input_folder_path, file))

    # if True in np.isnan(mat_data["NetworkMatrix"][i-1]):
    #     print("就是这个B：", file)
    size = np.shape(mat_data["NetworkMatrix"])
    for row in range(0, size[0]):
        for col in range(0, size[1]):
            if mat_data["NetworkMatrix"][row][col] < 0:
                mat_data["NetworkMatrix"][row][col] = 0
    # if i == 1:
    #     print(mat_data["NetworkMatrix"])
    group_data += mat_data["NetworkMatrix"]

    # print(mat_data["NetworkMatrix"][i-1])

    print(file, "process done!")
    print()
    i += 1

BinomialDistributionNetwork = group_data / len(files) * 100
# 四组分别保存为二项分布网络
savemat(output_folder_path + group + "_BinomialDistributionNetwork.mat",
        {'BD_NetworkMatrix': BinomialDistributionNetwork})
