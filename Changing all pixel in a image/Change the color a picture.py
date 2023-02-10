from PIL import Image
img = Image.open("image.png")
largeur_image=500
hauteur_image=500
for y in range(hauteur_image):
    for x in range(largeur_image):
        rgb = img.getpixel((x,y))[:3]
        r, v, b = rgb
        n_r=v
        n_v=b
        n_b=r
        img.putpixel((x,y),(n_r,n_v,n_b))
img.show()
img.save("image_modifiee.png")


