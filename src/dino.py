import torch
from torchvision.models.efficientnet import efficientnet_v2_s
import keyboard
from PIL import Image, ImageGrab
import numpy as np
from torchvision.transforms import Compose, Resize, CenterCrop, ToTensor, Normalize
from tqdm import tqdm
import os
import sys

model = efficientnet_v2_s()
model.classifier = torch.nn.Linear(in_features = 1280, out_features = 2)

# Check if the model file exists
model_path = "efficientnet_s.pth"
if not os.path.isfile(model_path):
    print(f"Model file {model_path} not found. Please ensure the file exists.")
    sys.exit(1)

model.load_state_dict(torch.load(model_path, map_location='cpu'))

# Check if CUDA is available
device = "cuda" if torch.cuda.is_available() else "cpu"
print(f"Running on device: {device}")

model.to(device)
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
  try:
    image = ImageGrab.grab(bbox = (620,220,1280,360)) 
    image = ToTensor()(image)
    image = image.to(device)
    image = transformer(image)
    outputs = model(image[None , ...])
    _,preds = torch.max(outputs.data, 1)
    if preds.item() == 1:
        keyboard.press_and_release("space")
  except Exception as e:
    print(f"An error occurred: {e}")
