from PIL import Image

def load_img(filename):
  im = Image.open(filename)
  return im

def show_img(im):
  im.show()

def save_img(im, filename):
  im.save(filename, "jpeg")
  show_img(im)

def obamicon(im):
    pixels = im.getdata()
    newPixels = []

    darkBlue = (0, 51, 76)
    red = (217, 26, 33)
    lightBlue = (112, 150, 158)
    yellow = (252, 227, 166)

    for p in pixels:
        intensity = p[0] + p[1] + p[2]

        if intensity < 182:
            newPixels.append(darkBlue)
        elif intensity >= 182 and intensity < 364:
            newPixels.append(red)
        elif intensity >= 364 and intensity < 546:
            newPixels.append(lightBlue)
        else:
            newPixels.append(yellow)

    newImage = Image.new("RGB", im.size)

    newImage.putdata(newPixels)
    return newImage
