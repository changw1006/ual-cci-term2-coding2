# Week5 - Convolution Neural Networks

Chang Wang 20036997
<br />

Convolutional neural networks are now widely used in image recognition, and I will make a convolutional neural network to analyse handwritten digits.
<br />

Let's look at the final visualisation first.

![](https://static.wixstatic.com/media/27541e_c975cf4d343446dd8746e46d4721f85a~mv2.gif)

I will be using Mnist handwritten data to classify the numbers so that the computer can recognise the handwritten numbers.

<br />
First import the various modules.

````python
import torch
import torch.nn as nn
import torch.utils.data as Data
import torchvision   #Database module
import matplotlib.pyplot as plt
````
<br />

## **MNIST handwritten data**

````python
torch.manual_seed(1)    # reproducible

# Hyper Parameters
EPOCH = 1  # train the training data n times, to save time, we just train 1 epoch
BATCH_SIZE = 50
LR = 0.001  # learning rate
DOWNLOAD_MNIST = False


# Mnist digits dataset
if not(os.path.exists('./mnist/')) or not os.listdir('./mnist/'):
    # not mnist dir or mnist is empyt dir
    DOWNLOAD_MNIST = True
 
    
# Mnist digits dataset
train_data = torchvision.datasets.MNIST(
    root='./mnist/',
    train=True,  # this is training data
    transform=torchvision.transforms.ToTensor(),  # Converts a PIL.Image or numpy.ndarray to  # torch.FloatTensor of shape (C x H x W) and normalize in the range [0.0, 1.0]
    download=DOWNLOAD_MNIST,
)
````
<br />

To present the training data, use the drawing function to present the first image of the training data.

````python
# plot one example
print(train_data.train_data.size())  # (60000, 28, 28)
print(train_data.train_labels.size())  # (60000)
plt.imshow(train_data.train_data[0].numpy(), cmap='gray')
plt.title('%i' % train_data.train_labels[0])
plt.show()
````

Run to get the first image of the training data in the database, which is a two-dimensional data form.

![](https://static.wixstatic.com/media/27541e_fb636003198d4171ba8f96b3f1b8f829~mv2.png/v1/fill/w_800,h_600,al_c,q_90/27541e_fb636003198d4171ba8f96b3f1b8f829~mv2.webp)

(Values in black are all 0, values in white are greater than 0.)

<br />

Once you have the training data, use the Dataloader.

````python
# Data Loader for easy mini-batch return in training, the image batch shape will be (50, 1, 28, 28)
train_loader = Data.DataLoader(dataset=train_data, batch_size=BATCH_SIZE, shuffle=True)
````
<br />

Again, in addition to the training data, I used some test data to see if it was trained properly.

````python
# pick 2000 samples to speed up testing
test_data = torchvision.datasets.MNIST(root='./mnist/', train=False)
test_x = torch.unsqueeze(test_data.test_data, dim=1).type(torch.FloatTensor)[:2000]/255.   # shape from (2000, 28, 28) to (2000, 1, 28, 28), value in range(0,1)
test_y = test_data.test_labels[:2000]
````

## **Convolution Neural Networks modules**

A ````class```` is used to build a CNN model. The overall flow of this CNN is Convolution ````Conv2d```` -> Excitation ````ReLU```` -> Pooling, down-sampling ````MaxPooling```` -> Again -> Flattening of the multi-dimensional convolutional feature map -> Integration into a fully connected layer ````Linear```` -> Output.

````python
class CNN(nn.Module):
 def __init__(self):
     super(CNN, self).__init__()
     self.conv1 = nn.Sequential(         # input shape (1, 28, 28)
         nn.Conv2d(
             in_channels=1,              # input height
             out_channels=16,            # n_filters
             kernel_size=5,              # filter size
             stride=1,                   # filter movement/step
             padding=2,                  # if want same width and length of this image after Conv2d, padding=(kernel_size-1)/2 if stride=1
         ),                              # output shape (16, 28, 28)
         nn.ReLU(),                      # activation
         nn.MaxPool2d(kernel_size=2),    # choose max value in 2x2 area, output shape (16, 14, 14)
     )
     self.conv2 = nn.Sequential(         # input shape (16, 14, 14)
         nn.Conv2d(16, 32, 5, 1, 2),     # output shape (32, 14, 14)
         nn.ReLU(),                      # activation
         nn.MaxPool2d(2),                # output shape (32, 7, 7)
        )
     self.out = nn.Linear(32 * 7 * 7, 10)   # fully connected layer, output 10 classes

 def forward(self, x):
     x = self.conv1(x)
     x = self.conv2(x)
     x = x.view(x.size(0), -1)           # flatten the output of conv2 to (batch_size, 32 * 7 * 7)
     output = self.out(x)
     return output, x    # return x for visualization

cnn = CNN()
print(cnn)   # net architecture


"""
CNN (
  (conv1): Sequential (
    (0): Conv2d(1, 16, kernel_size=(5, 5), stride=(1, 1), padding=(2, 2))
    (1): ReLU ()
    (2): MaxPool2d (size=(2, 2), stride=(2, 2), dilation=(1, 1))
  )
  (conv2): Sequential (
    (0): Conv2d(16, 32, kernel_size=(5, 5), stride=(1, 1), padding=(2, 2))
    (1): ReLU ()
    (2): MaxPool2d (size=(2, 2), stride=(2, 2), dilation=(1, 1))
  )
  (out): Linear (1568 -> 10)
)
"""
````

<br />

## **Training** 

Wrap ````x```` ````y```` in a ````Variable````, put it into ````cnn```` to calculate the ````output````, and then calculate the error. The code below omits the part that calculates the ````accuracy````.

````python
# training and testing
for epoch in range(EPOCH):
    for step, (b_x, b_y) in enumerate(train_loader):   # gives batch data, normalize x when iterate train_loader

        output = cnn(b_x)[0]               # cnn output
        loss = loss_func(output, b_y)   # cross entropy loss
        optimizer.zero_grad()           # clear gradients for this training step
        loss.backward()                 # backpropagation, compute gradients
        optimizer.step()                # apply gradients

"""
...
Epoch:  0 | train loss: 0.0306 | test accuracy: 0.97
Epoch:  0 | train loss: 0.0147 | test accuracy: 0.98
Epoch:  0 | train loss: 0.0427 | test accuracy: 0.98
Epoch:  0 | train loss: 0.0078 | test accuracy: 0.98
"""
````

<br />

Check the results of your training every 50 steps

````python
if step % 50 == 0:
    test_output, last_layer = cnn(test_x)
    pred_y = torch.max(test_output, 1)[1].data.numpy()
    accuracy = float((pred_y == test_y.data.numpy()).astype(int).sum()) / float(test_y.size(0))
    print('Epoch: ', epoch, '| train loss: %.4f' % loss.data.numpy(), '| test accuracy: %.2f' % accuracy)
````

<br />

Finally, take 10 datas to see if the predicted values are correct or not:

````python
# print 10 predictions from test data
test_output = cnn(test_x[:10])
pred_y = torch.max(test_output, 1)[1].data.numpy().squeeze()
print(pred_y, 'prediction number')
print(test_y[:10].numpy(), 'real number')
````

<br />

Next, start running the CNN network
![](https://static.wixstatic.com/media/27541e_6d801da1d8a14d2081464ce40936bcd2~mv2.jpg/v1/fill/w_818,h_457,al_c,lg_1,q_90/27541e_6d801da1d8a14d2081464ce40936bcd2~mv2.webp)

At the end of the training, a 97% - 98% correct rate can be achieved.


<br />

## **Visualization training** 

The visualisation code is mainly done with ````matplotlib```` and ````sklearn````. This is because we use the ````T-SNE```` dimensionality reduction technique to visualize the output of the last layer of the high-dimensional CNN, and this is the result of the CNN forward code ````x = x.view(x.size(0), -1)````.

````python
# following function (plot_with_labels) is for visualization, can be ignored if not interested
from matplotlib import cm
try: from sklearn.manifold import TSNE; HAS_SK = True
except: HAS_SK = False; print('Please install sklearn for layer visualization')
def plot_with_labels(lowDWeights, labels):
    plt.cla()
    X, Y = lowDWeights[:, 0], lowDWeights[:, 1]
    for x, y, s in zip(X, Y, labels):
        c = cm.rainbow(int(255 * s / 9)); plt.text(x, y, s, backgroundcolor=c, fontsize=9)
    plt.xlim(X.min(), X.max()); plt.ylim(Y.min(), Y.max()); plt.title('Visualize last layer'); plt.show(); plt.pause(0.01)

plt.ion()
````

![](https://static.wixstatic.com/media/27541e_c975cf4d343446dd8746e46d4721f85a~mv2.gif)
