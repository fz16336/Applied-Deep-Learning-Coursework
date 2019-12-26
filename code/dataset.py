import torch
from torch.utils import data
import numpy as np
import pickle

class UrbanSound8KDataset(data.Dataset):
    def __init__(self, dataset_path, mode):
        self.dataset = pickle.load(open(dataset_path, 'rb'))
        self.mode = mode

    def __getitem__(self, index):

        dataset = np.array(self.dataset)

        LM = dataset[index]["features"]["logmelspec"]
        MFCC = dataset[index]["features"]["mfcc"]
        C = dataset[index]["features"]["chroma"]
        SC = dataset[index]["features"]["spectral_contrast"]
        T = dataset[index]["features"]["tonnetz"]

        print(MFCC)
        print(LM)
        print(C)
        print(SC)
        print(T)

        if self.mode == 'LMC':
            # Edit here to load and concatenate the neccessary features to
            # create the LMC feature
            LMC = np.concatenate((LM, C, SC, T), axis=0)
            feature = torch.from_numpy(LMC.astype(np.float32)).unsqueeze(0)
        elif self.mode == 'MC':
            # Edit here to load and concatenate the neccessary features to
            # create the MC feature
            MC = np.concatenate((MFCC, C, SC, T), axis=0)
            feature = torch.from_numpy(MC.astype(np.float32)).unsqueeze(0)
        elif self.mode == 'MLMC':
            # Edit here to load and concatenate the neccessary features to
            # create the MLMC feature
            MLMC = np.concatenate((MFCC, LM, C, SC, T), axis=0)
            feature = torch.from_numpy(MLMC.astype(np.float32)).unsqueeze(0)

        print(feature)
        label = self.dataset[index]['classID']
        fname = self.dataset[index]['filename']
        return feature, label, fname

    def __len__(self):
        return len(self.dataset)

dataset_train_LMC = UrbanSound8KDataset("./UrbanSound8K_train.pkl", "LMC")
print(dataset_train_LMC.__getitem__(0))
