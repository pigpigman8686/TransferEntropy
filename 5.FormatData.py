"""
author: mhd
create time: 2022.9.29
description: format centrality and subtract TOP 40 ROIs data
"""
import os
import numpy as np
from scipy.io import loadmat, savemat

# 原始时间序列
# AD_inputdir = 'E:/0.MasterStudent/ADDetection/NetwrokConstruction/origin_rs-fMRI_Surface_624/AD_105'
# CN_inputdir = 'E:/0.MasterStudent/ADDetection/NetwrokConstruction/origin_rs-fMRI_Surface_624/CN_172'
# EMCI_inputdir = 'E:/0.MasterStudent/ADDetection/NetwrokConstruction/origin_rs-fMRI_Surface_624/EMCI_212'
# LMCI_inputdir = 'E:/0.MasterStudent/ADDetection/NetwrokConstruction/origin_rs-fMRI_Surface_624/LMCI_135'
# 构造脑网络后
AD_inputdir = 'E:/0.MasterStudent/ADDetection/NetwrokConstruction/1.Corr_AD_Network_Schaefer'
CN_inputdir = 'E:/0.MasterStudent/ADDetection/NetwrokConstruction/1.Corr_CN_Network_Schaefer'
EMCI_inputdir = 'E:/0.MasterStudent/ADDetection/NetwrokConstruction/1.Corr_EMCI_Network_Schaefer'
LMCI_inputdir = 'E:/0.MasterStudent/ADDetection/NetwrokConstruction/1.Corr_LMCI_Network_Schaefer'

AD_files = os.listdir(AD_inputdir)
CN_files = os.listdir(CN_inputdir)
EMCI_files = os.listdir(EMCI_inputdir)
LMCI_files = os.listdir(LMCI_inputdir)

# 选择的40个ROI下标(原始时间序列)
# index = [647, 289, 291, 292, 579, 252, 588, 266, 201, 213, 675, 584, 671, 650, 290, 673, 206, 210, 230, 633,  # centrality
#          738, 327, 273, 369, 352, 751, 718, 700, 712, 703, 365, 721, 374, 660, 249, 317, 710, 281, 336, 705]  # diff
# index = [647, 289, 291, 292, 579, 252, 588, 266, 201, 213, 675, 584, 671, 650, 290, 673, 206, 210, 230, 633]  # centrality
# index = [738, 327, 273, 369, 352, 751, 718, 700, 712, 703, 365, 721, 374, 660, 249, 317, 710, 281, 336, 705]  # diff

# 选择的40个ROI下标(原始时间序列)
index = [286, 108, 110, 111, 218, 71, 227, 85, 20, 32, 314, 223, 310, 289, 109, 312, 25, 29, 49, 272,  # centrality
         377, 146, 92, 188, 171, 390, 357, 339, 351, 342, 184, 360, 193, 299, 68, 136, 349, 100, 155, 344]  # diff
# index = [286, 108, 110, 111, 218, 71, 227, 85, 20, 32, 314, 223, 310, 289, 109, 312, 25, 29, 49, 272]  # centrality
# index = [377, 146, 92, 188, 171, 390, 357, 339, 351, 342, 184, 360, 193, 299, 68, 136, 349, 100, 155, 344]  # diff

X = []  # 最终特征数据
label = []  # 数据标签： 1:AD 2:CN 3:EMCI 4:LMCI

Number = 0
for class_files in [AD_files, CN_files, EMCI_files, LMCI_files]:
    Number += 1
    for file in class_files:
        print(file, "processing.....")

        # 读取文件并截取
        path = AD_inputdir
        if Number == 1:
            path = AD_inputdir
        elif Number == 2:
            path = CN_inputdir
        elif Number == 3:
            path = EMCI_inputdir
        elif Number == 4:
            path = LMCI_inputdir
        # mat_data = loadmat(os.path.join(path, file))["Data"]
        mat_data = loadmat(os.path.join(path, file))["NetworkMatrix"]

        mat_data_line = []
        for i in index:
            # mat_data_line += list(mat_data[:, i])  # 根据index，将功能连接图像矩阵中的指定ROI取出
            mat_data_line += list(mat_data[i, 0:i]) + list(mat_data[i, (i+1):])  # 根据index，将功能连接图像矩阵中的指定ROI取出
        X.append(mat_data_line)  # 一个被试的所有特征，加入到最终特征数据中

        label.append([float(Number)])
print(len(X), len(X[0]))
print(len(label))

savemat('E:/0.MasterStudent/ADDetection/NetwrokConstruction/4.FormatData.mat', {'FeatureData': X})
savemat('E:/0.MasterStudent/ADDetection/NetwrokConstruction/4.LabelData.mat', {'LabelData': label})
