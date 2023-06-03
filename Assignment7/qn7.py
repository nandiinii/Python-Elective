# from PIL import Image,ImageFilter
# img = Image.open('cat.gif')
# img=img.convert("RGB")
# img=img.filter(ImageFilter.GaussianBlur(radius=5))
# img.save('blurred.gif')


from PIL import Image,ImageFilter
img=Image.open("cat.gif")
img=img.convert("RGB")
img=img.filter(ImageFilter.GaussianBlur(radius=5))
img.save("blurred.gif")
