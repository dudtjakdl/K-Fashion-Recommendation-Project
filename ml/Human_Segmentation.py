import numpy as np
import cv2
import torch
import albumentations as albu
from iglovikov_helper_functions.utils.image_utils import load_rgb, pad, unpad
from iglovikov_helper_functions.dl.pytorch.utils import tensor_from_rgb_image
from people_segmentation.pre_trained_models import create_model
import matplotlib.pyplot as plt
import skimage.io
import time

model = create_model("Unet_2020-07-20")
model.eval();

def segmentation_model(input_image):


  image = load_rgb(input_image)
  
  transform = albu.Compose([albu.Normalize(p=1)], p=1)
  padded_image, pads = pad(image, factor=32, border=cv2.BORDER_CONSTANT)
  x = transform(image=padded_image)["image"]
  x = torch.unsqueeze(tensor_from_rgb_image(x), 0)
  with torch.no_grad():
    prediction = model(x)[0][0]
  mask = (prediction > 0).cpu().numpy().astype(np.uint8)
  mask = unpad(mask, pads)

  mask=mask.reshape(mask.shape[0],mask.shape[1],1)

  mask=mask.reshape(mask.shape[0],mask.shape[1],1)

  for i in range(mask.shape[2]):
    temp = skimage.io.imread(input_image)
    for j in range(temp.shape[2]):
        temp[:,:,j] = temp[:,:,j] * mask[:,:,i]
    plt.figure(figsize=(8,8))

   
  global timestr
  timestr= time.strftime("%Y%m%d-%H%M%S")
  skimage.io.imsave('static/segmentation_img/'+str(timestr)+'.png',temp)