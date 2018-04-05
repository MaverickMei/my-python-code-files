#!/usr/bin/env python 
# -*- coding: utf-8 -*-

import pytesseract
from PIL import Image #除了pytesseract和Image，还需要安装Tesseract-OCR！！！

image = Image.open(r"a.png")
code = pytesseract.image_to_string(image)#识别英文字母,中文无法识别
print(code)



