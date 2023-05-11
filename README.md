# batchify: structured data in pytorch

### Note: all the batchify functionality has been incorperated into [Terrace](https://github.com/mixarcid/terrace). Please use Terrace instead; development on this repo has stopped. 

PyTorch can already batchify tensors (and tuples of tensors), but what about arbitrary classes? If your neural network is dealing with complex datatypes, structuring your data in classes is the solution. With batchify, you can seemlessly return classes in a pytorch dataset.

As an example, let's say you want your neural network do something with people. People, as we all know, are faces and names


```python
import torch
from batchify import Batch, Batchable

MAX_NAME_LEN = 128
IMG_SIZE = 256
class Person(Batchable):
    
    face: torch.Tensor
    name: torch.Tensor
    
    def __init__(self): # not a very interesting person
        self.face = torch.zeros((3, IMG_SIZE, IMG_SIZE))
        self.name = torch.zeros((MAX_NAME_LEN,))
    
```

Now here's the fun part: we can make a batch of people. This automatically batchifies both the face and the name


```python
dave = Person()
rhonda = Person()
batch = Batch([dave, rhonda])
print(len(batch))
print(dave.name.shape)
print(batch.name.shape) # notice the extra batch dimension
print(batch[0].name.shape) # un-batchification
```

    2
    torch.Size([128])
    torch.Size([2, 128])
    torch.Size([128])


But what about a custom person dataset? Pretty easy with the batchify dataloader


```python
from batchify import DataLoader

class PersonDataset(torch.utils.data.Dataset):
    
    def __len__(self):
        return 16
    
    def __getitem__(self, index):
        return Person()
    
batch_size = 8
dataset = PersonDataset()
loader = DataLoader(dataset, batch_size=batch_size)
for batch in loader:
    print(batch.face.shape)
```

    torch.Size([8, 3, 256, 256])
    torch.Size([8, 3, 256, 256])


This is all great if you want to input a Person into your network. But what if you want to _output_ a person?

(**warning**: this functionality only works if you have correct type annotations on your Batchable classes)


```python
out_batch = Batch(Person,
                  face=torch.zeros((batch_size, 3, IMG_SIZE, IMG_SIZE)),
                  name=torch.zeros((batch_size, MAX_NAME_LEN)))
print(len(out_batch))
print(out_batch[0].name.shape)
```

    8
    torch.Size([128])

