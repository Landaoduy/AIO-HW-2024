import torch
import torch.nn as nn


class softmax_function(nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x):
        x_exp = torch.exp(x)

        partition = x_exp.sum(0, keepdim=True)  # dimension = 0

        return x_exp / partition


data = torch.Tensor([1, 2, 3])

my_softmax = softmax_function()

output = my_softmax(data)

print(output)
