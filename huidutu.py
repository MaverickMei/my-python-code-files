#!/usr/bin/env python
# -*- coding: utf-8 -*-
from PIL import Image  #或直接import Image

im1 = Image.open(r'C:\Users\mcc\Desktop\chengp.jpg').convert('L')  #注意 反斜杠后面：\U和\1都是转义字符
im1.save(r'C:\Users\mcc\Desktop\danghui2.jpg')