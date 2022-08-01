import random
import glob
from PIL import ImageFont, ImageDraw, Image

# you can import multiple classes of a module at once
from pathlib import Path
#additional library sry


#white = (255,255,255)
#black = (0,0,0)
#bad code, might regret defining colours like this

def main():
  def text1_factory():
    data = open('data.txt','r')
    datatable = data.readlines()
    promptrand = random.randrange(0, len(datatable)) 
    return datatable[promptrand]
  
  def img_factory():
    file_path_type = ["./images/*.png", "./images/*.jpg"]
    images = glob.glob(random.choice(file_path_type))
    random_image = random.choice(images)
    return random_image
  
    
  #path = "C:\\Users\\Edward\\Desktop\\Dank Memer\\images"
  
  
  class meme_maker:
    def __init__(self, name, caption, img):
      self.name = name
      self.caption=caption
      self.img = img
  
    def make_img(self):
      
      imgover = Image.open(Path(self.img))
      width, height = imgover.size
  
      blankspace = 50
      offset = 0, blankspace
  
      img  = Image.new(mode = "RGB", size = (width, height+blankspace), color=(255,255,255))
      img.convert("RGB")
      img.paste(imgover, offset)
  
  
  
  
      draw = ImageDraw.Draw(img)
  
      font = ImageFont.truetype('Roboto-Regular.ttf', 12)
  
      draw.text((10, (blankspace/2)-10),self.caption,(0,0,0),font=font)
      return img
  
    def save_img(self,img):
      img.save(self.name)
      return None
  
  
  
  img_name = 'meme.png'
  
  image = meme_maker(img_name, text1_factory(), img_factory())
  
  image.save_img(image.make_img())
  
  
  
  
  
  #background = Image.open('background.png')
  #foreground = Image.open('pepe.png')
  #unused????
  #file extensions are always lowercase
  
  
  
  #text2 = "caption"
  #unused?
  
  
  
  #color = 'dark_blue'
  #also unused?
  
  
  
  
if __name__ == '__main__':
  main()