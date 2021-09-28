from PIL import Image
import numpy as np

img = Image.open("coder.jpeg")
img_list = list(img.getdata())
img.show()

#here 'msg' is a String you want to encrypt
def steganography(msg):
    pixel = img_list
    img2 = Image.new("RGB", (img.size[0], img.size[1]))
    i = 0;s = ''
    for v in msg:
        s += bin(ord(v))[2:]

    for v in range(len(s)):
        pixel[v] = list(pixel[v])
        temp = bin(pixel[v][0])
        temp = list(temp[2:])

        temp[len(temp)-1] = s[v]
        red = listnum(temp)
        pixel[v][0] = red
        pixel[v] = tuple(pixel[v])
        
    """while(i < len(msg)):
        z = list(bin(ord(msg[i])))
        z = z[2:]
        for v in range(len(z)):
            pixel[v] = list(pixel[v])

            temp = list(bin(pixel[v][0]))
            temp[len(temp)-1] = z[v]            # use listnum function here
            temp = temp[2:]

            red = listnum(temp)
            pixel[v][0] = red
            pixel[v] = tuple(pixel[v])
        
        i += 1"""

    img2.putdata(pixel)
    #print(pixel)
    img2.show()
    return img2
        
#stego_img = ste("hi")

def resteganography(length, stego_img):
    msg = []
    pixel = list(stego_img.getdata())
    for i in range(length*7):
        word = list(bin(pixel[i][0]))
        msg.append(word[len(word)-1])
        if(i == 6):
            char = chr(listnum(msg))
            print(char, end='')
            msg = []
        if(i == length*7-1):
            char = chr(listnum(msg))
            print(char)

#reste(2, stego_img)
