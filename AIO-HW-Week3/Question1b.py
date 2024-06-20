import torch
import torch.nn as nn


class softmax_stable(nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x):
        x_max = torch.max(x, dim=0, keepdim=True)

        x_exp = torch.exp(x - x_max.values)

        partition = x_exp.sum(0, keepdim=True)

        return x_exp / partition


data2 = torch.Tensor([5, 2, 4])

my_softmax_stable = softmax_stable()

output = my_softmax_stable(data2)

print(output)
