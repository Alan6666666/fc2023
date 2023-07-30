from time import sleep
import torch
from utils import getWeightPath
from models.a_fake_number_recognizing_model import Net

if __name__ == "__main__":
    net = Net()
    print("i am training...")
    sleep(1)
    print("finish!") 
    torch.save(net, getWeightPath('a_fake_number_recognizer'))

