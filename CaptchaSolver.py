#OCR de Captcha numérico

from PIL import Image
from pytesseract import image_to_string

def solver_captcha(image):
  #variável image é o path do captcha em formato .jpeg
  im = Image.open(image)
  return image_to_string(im, config='--psm 9 --oem 3 -c tessedit_char_whitelist=0123456789')   
