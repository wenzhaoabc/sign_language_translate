import torch.nn as nn
import torch.nn.functional as F

class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()

        self.conv1 = nn.Conv2d(1, 80, kernel_size = 5).cuda()
        self.conv2 = nn.Conv2d(80, 80, kernel_size = 5).cuda()

        self.pool1 = nn.MaxPool2d(kernel_size = 2, stride = 2, padding = 0).cuda()
        self.pool2 = nn.MaxPool2d(kernel_size = 2, stride = 2, padding = 0).cuda()

        self.batch_norm1 = nn.BatchNorm2d(80).cuda()
        self.batch_norm2 = nn.BatchNorm2d(80).cuda()

        self.fc1 = nn.Linear(1280, 250).cuda()
        self.fc2 = nn.Linear(250, 25).cuda()

    def forward(self, x):

        x = self.conv1(x).cuda()
        x = self.batch_norm1(x).cuda()
        x = F.relu(x).cuda()
        x = self.pool1(x).cuda()

        x = self.conv2(x).cuda()
        x = self.batch_norm2(x).cuda()
        x = F.relu(x).cuda()
        x = self.pool2(x).cuda()

        x = x.view(x.size(0), -1).cuda()

        x = F.relu(self.fc1(x)).cuda()
        x = self.fc2(x).cuda()
        x = F.log_softmax(x, dim=1).cuda()

        return x