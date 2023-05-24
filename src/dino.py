import torch
from torchvision.models.efficientnet import efficientnet_v2_s                                                                                          
import keyboard
from PIL import Image, ImageGrab
import numpy as np
from torchvision.transforms import Compose, Resize, CenterCrop, ToTensor, Normalize
from tqdm import tqdm

model = efficientnet_v2_s()
model.classifier = torch.nn.Linear(in_features = 1280, out_features = 2)
model.load_state_dict(torch.load("efficientnet_s.pth"))
model.to("cuda")
model.eval()


transformer = Compose([
    Resize([480,480]),
    CenterCrop(480),
    Normalize(mean =[0.485, 0.456, 0.406], std =[0.229, 0.224, 0.225])
])


def generator():
    while(not keyboard.is_pressed("esc")):
      yield

for _ in tqdm(generator()):
    image = ImageGrab.grab(bbox = (620,220,1280,360)) 
    image = ToTensor()(image)                    
    image = image.to("cuda")
    image = transformer(image)
    outputs = model(image[None , ...])
    _,preds = torch.max(outputs.data, 1)
    if preds.item() == 1:
        keyboard.press_and_release("space")