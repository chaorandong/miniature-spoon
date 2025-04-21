import torch.nn as nn

class SimpleNet(nn.Module):
    def __init__(self, input_dim=10, output_dim=2):
        super().__init__()
        self.layer_1 = nn.Linear(input_dim, 5)
        self.layer_2 = nn.Linear(5, output_dim)

        # self.layer_dictionary = {}
        # for i in range(num_layers):
        #     self.layer_dictionary[i] = whatever

    def forward(self, x):
        x= self.layer_1(x)
        x = nn.Sigmoid(x)
        x = self.layer_2(x)
        x = nn.Sigmoid(x)
        return x
        
        # return nn.sigmoid(
        # self.layer_2(
        #     nn.sigmoid(
        #         self.layer_1(x)
        #     )))M