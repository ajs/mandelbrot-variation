#!/usr/bin/env python3
import numpy as np
from PIL import Image # Pillow fork of PIL
x,y=np.ogrid[-5.4:0.8:950j,-1.6:1.6:500j]
c = x + 1j*y
ones = np.ones_like(x*y)
its = np.zeros_like(ones)
z = c * 0
for n in range(200):
  itsmax = abs(z) < 200.0
  np.putmask(its, itsmax, n*ones)
  np.putmask(z, itsmax,  z**2 + 0.19 * z ** 3 + c)
smooth = its - np.log(np.log(np.maximum(2.0, abs(z))))/np.log(2.6)
v = np.where(itsmax, 0, np.log(smooth * 1.1 + 1.0) * 0.3)
greys = np.array((v,v,v)).T
blues = np.array((v**4, v**2.5, v)).T
w = np.maximum(0, 2-v)
sepias = np.array((w, w**1.5, w**3)).T
color = np.where(greys<1.0, blues, sepias)
rgb = np.uint8(np.minimum(1.0, color) * 255)
img = Image.fromarray(rgb, mode="RGB")
img.save("mand.png")
