from PIL import Image, ImageDraw, ImageFont
import pandas as pd
import os
df = pd.read_csv('list.csv')
font = ImageFont.truetype(r"C:\Users\Asus\Desktop\card\OpenSans-Italic-VariableFont_wdth,wght.ttf",60)
for index,j in df.iterrows():
    img = Image.open('blank-card.jpg')
    draw = ImageDraw.Draw(img)
    draw.text(xy=(845,845),text='{}'.format(j['message']),fill=(15,20,180),font=font)
    img.save('cards/{}.jpg'.format(j['message']))