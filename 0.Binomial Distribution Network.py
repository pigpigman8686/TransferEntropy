"""
author: mhd
create time: 2022.9.9
description: use binomial distribution build a brain network (642 130*400 --> 4 130*400)

* --- how to use it ---
please pip install numpy, scipy
* ---------------------
"""
import os
import numpy as np
from scipy.io import loadmat, savemat

save_process_files_flag = True
input_folder_path = "E:/0.MasterStudent/ADDetection/NetwrokConstruction/origin_rs-fMRI_Surface_624/"
process_folder_path = "E:/0.MasterStudent/ADDetection/NetwrokConstruction/"
output_folder_path = "E:/0.MasterStudent/ADDetection/NetwrokConstruction/3.Results_BD_Network/"


group_data = {
    "AD": np.zeros((130, 400)),
    "CN": np.zeros((130, 400)),
    "EMCI": np.zeros((130, 400)),
    "LMCI": np.zeros((130, 400))
}
# print(group_data)
sub_folders = os.listdir(input_folder_path)
for folder in sub_folders:
    group = folder.split("_")[0]  # ex:AD CN
    group_files = os.listdir(os.path.join(input_folder_path, folder))
    # print(group_files)
    for file in group_files:
        print(file, "processing....")

        # 读取文件并截取
        mat_data = loadmat(os.path.join(input_folder_path, folder, file))
        origin_data = np.hstack((mat_data["Data"][:, 180:380], mat_data["Data"][:, 560:760]))  # 横向合并, Schaefer模板
        # 保存每个被试文件
        if save_process_files_flag:
            # 保存每个切片后的被试
            savemat(process_folder_path + "2.Sub_" + group + "_Origin_Schaefer/" + file, {'OriginData': origin_data})  #

        group_data[group] += origin_data

        print(file, "process done!")
        print()

    BinomialDistributionNetwork = group_data[group] / len(group_files)
    # 四组分别保存为二项分布网络
    savemat(output_folder_path + group + "_BinomialDistributionNetwork.mat",
            {'Data': BinomialDistributionNetwork})  # 将最后的结果输出
