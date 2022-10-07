import numpy as np
from scipy.io import loadmat
import matplotlib.pyplot as plt


input_folder_path = "E:/0.MasterStudent/ADDetection/NetwrokConstruction/3.Results_Network_BD/Binaryzation_results/"
file_name_AD = "Binaryzation_AD_BinomialDistributionNetwork.mat"
file_name_CN = "Binaryzation_CN_BinomialDistributionNetwork.mat"

NetworkMatrix_AD = loadmat(input_folder_path + file_name_AD)["BDBinaryzationNetworkMatrix"]
NetworkMatrix_CN = loadmat(input_folder_path + file_name_CN)["BDBinaryzationNetworkMatrix"]


def sum(row_data):
    ans = 0
    for i in range(0, len(row_data)):
        if row_data[i]:
            ans += 1
    return ans


# x = np.arange(0, 400)
# print(x)
hist_AD = []
hist_CN = []
for row in NetworkMatrix_AD:
    ans = sum(row)
    hist_AD.append(ans)
for row in NetworkMatrix_CN:
    ans = sum(row)
    hist_CN.append(ans)

hist_AD = np.array(hist_AD)
hist_CN = np.array(hist_CN)
diff = abs(hist_AD - hist_CN)
ans = np.argsort(-diff)  # 排序，返回从大到小的下标
with open('HistogramSubtractDegreeTop20ROIs.csv', 'w') as f:
    f.write("begin_0_index,origin_index,diff\n")
    for i in range(20):
        f.write(str(ans[i]) + ",")
        if ans[i] < 200:  # 前200个起始下标为181
            f.write(str(ans[i] + 181) + "," + str(diff[ans[i]]) + "\n")
        else:  # 后200个起始下标为581
            f.write(str(ans[i] + 361) + "," + str(diff[ans[i]]) + "\n")
