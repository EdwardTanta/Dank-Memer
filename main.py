import random
import glob
from PIL import ImageFont
from PIL import ImageDraw
from PIL import Image  

white = (255,255,255)
black = (0,0,0)

data = open('data.txt','r')
datatable = data.readlines()
promptrand = int(random.randrange(0, len(datatable)))
path = "C:\\Users\\Edward\\Desktop\\Dank Memer\\images"
file_path_type = ["./images/*.png", "./images/*.jpeg"]
images = glob.glob(random.choice(file_path_type))
random_image = random.choice(images)

print(datatable[promptrand])

background = Image.open('background.PNG')
foreground = Image.open('pepe.PNG')

text1 = promptrand
text2 = "caption"

img_name = 'meme.png'

color = 'dark_blue'


imgover = Image.open(random_image)
width, height = imgover.size

blankspace = 50
offset = 0, blankspace

img  = Image.new( mode = "RGB", size = (width, height+blankspace), color=white)
img.convert("RGB")
img.paste(imgover, offset)

draw = ImageDraw.Draw(img)

font = ImageFont.truetype('Roboto-Regular.ttf', 12)

draw.text((10, (blankspace/2)-10),datatable[promptrand],(0,0,0),font=font)

img.show()