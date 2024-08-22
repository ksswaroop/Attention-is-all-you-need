import torch
from torch import nn

class InputEmbedding(nn.Module):

    def __init__(self,d_model:int,vocab_size:int):
        super().__init__()
        self.d_model=d_model
        self.vocab_size=vocab_size
        self.embedding = nn.Embedding(vocab_size,d_model)
    def forward(self,x):
        return xpom