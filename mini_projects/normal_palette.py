
from PIL import Image
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

base_angles = np.array([0, np.pi/12, np.pi/8, np.pi/6])

#base_angles = np.array([0, np.pi/6])

key_angles = np.array([
  base_angles + ii*np.pi/4
  for ii in range(8)
]).flatten()

def get_normal(theta, phi):
  #theta in xy plane,
  #-pi to pi
  #phi from 0 to pi/2
  zz = np.cos(phi)
  rr = np.sin(phi)
  xx = rr*np.cos(theta)
  yy = rr*np.sin(theta)
  return np.array([xx, yy, zz])

def normal2rgb(nn):
  return ((nn + 1)*(255/2)).round().astype(np.int)

rgb2hex = lambda r,g,b: '#%02x%02x%02x' %(r,g,b)

if __name__ == '__main__':
    for phi in key_angles[:len(key_angles)//4 + 1]: # angles 0 ... 90 deg
      print(f"phi: {(phi*180/np.pi).round()}")
      for theta in key_angles:
        print(rgb2hex(*normal2rgb(get_normal(theta, phi))))


    pallet = np.array(
        [
            [
                normal2rgb(get_normal(theta, phi))
                for phi in key_angles[:len(key_angles)//4 + 1]
            ]
            for theta in key_angles
        ]
    )

    plt.imsave("normal_pallet_from_python.png", pallet.astype(np.uint8))
