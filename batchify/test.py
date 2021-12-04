import torch
from torch.utils import data

from .batchify import Batch, Batchable, DataLoader


class SubTest(Batchable):
    arr: torch.Tensor

    def __init__(self, arr: torch.Tensor):
        self.arr = arr

class Test(Batchable):

    a: int
    b: float
    c: SubTest

    def __init__(self, a: int, b: int, c: SubTest):
        self.a = a
        self.b = b
        self.c = c

t1 = Test(1, 1.5, SubTest(torch.tensor([1, 1, 1])))
t2 = Test(2, 2.5, SubTest(torch.tensor([2, 2, 2])))
batch = Batch([t1, t2])
print(batch.c.arr.shape)
print(batch[1].b)

batch2 = Batch(Test,
               a=torch.tensor([3, 4]),
               b=torch.tensor([3.5, 4.5]),
               c=Batch(SubTest,
                       arr=torch.tensor([[3, 3, 3],
                                         [4, 4, 4]])))
print(batch2[1].b)

class TestDataset(data.Dataset):

    def __len__(self):
        return 16

    def __getitem__(self, index):
        return t1


dataset = TestDataset()
loader = DataLoader(dataset, batch_size=8)
for batch in loader:
    print(batch.a)
