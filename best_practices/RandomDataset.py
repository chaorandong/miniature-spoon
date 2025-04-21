import torch
from torch.utils.data import Dataset, DataLoader

class RandomDataset(Dataset):
    def __init__(self, num_samples=100, input_dim=10):
        super.__init__()

        # Save our input configuration
        self.num_samples = num_samples
        self.input_dim = input_dim

        # "Load" the data
        self.data = torch.randn(num_samples, input_dim)
        self.labels = torch.randint(0, 2, (num_samples,))

        # In practice, if dataset is large...
        # self.location_pf_dataset = ....

        # If dataset is small...
        # self.data = torch.load_csv(my_csv.csv)

    def __len__(self):
        return self.num_samples

    def __getitem__(self, idx):
        # Large datasets
        # data_sample = pd.read_csv('my_csv.csv', index = idx)

        # Small datasets
        # return self.my_data[idx]

        # For our random data
        return self.data[idx], self.labels[idx]


        
    
       