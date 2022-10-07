import numpy as np
from pyinform.transferentropy import *
from scipy.io import loadmat, savemat

file_path = \
    "E:/0.MasterStudent/ADDetection/NetwrokConstruction/AD_Origin_Schaefer_Sub/AD_BinomialDistributionNetwork.mat"

mat_data = loadmat(file_path)["Data"]
row0 = mat_data[:, 0][:10]
row1 = mat_data[:, 1][:10]
# print(row0)
row0 = [0, 1, 1, 1, 1, 0, 0, 0, 0]
row1 = [0, 0, 1, 1, 1, 1, 0, 0, 0]
print(transfer_entropy(row0, row1, k=2))
