from PIL import Image
import numpy as np

img = Image.open("coder.jpeg")
img_list = list(img.getdata())
img.show()

"""pixels = list(map(lambda x: int((x[0] + x[1] + x[2])/3), img_list))
img2 = Image.new("L", (img.size[0], img.size[1]), 255)
img2.putdata(pixels)
#img2.show()

pixels = list(map(lambda x: int((x[0]*(299/1000) + x[1]*(587/1000) + x[2]*(114/1000))/3), img_list))
img3 = Image.new("L", (img.size[0], img.size[1]), 255)
img3.putdata(pixels)
#img3.show()
"""
"""pixels = list(map(lambda x: int((x[0]*(212/1000) + x[1]*(715/1000) + x[2]*(72/1000))/3), img_list))
img4 = Image.new("L", (img.size[0], img.size[1]), 255)  #'L' makes the image dimension
img4.putdata(pixels)                                    #from 3[r,g,b] to 1[black & white]
#img4.show()
"""
x = len(img_list)

'''for i in range(20):
    v = img.size[0] + img.size[1]*(i+1) + i*2#len(img_list)-img.size[0]-2#img.size[0]*img.size[1] - img.size[0]-2
    img_list[v] = 120'''
'''i = 0
for v in range(img.size[0]+1, len(img_list)-img.size[0]-1):
    if(v >= img.size[0]*(i+1)+1 and v <= img.size[0]*(i+1)-2+img.size[0]):
        img_list[v] = 120
    if(v == img.size[0]*(i+1)-2+img.size[0]):
        i+=1'''
'''for i in range(20):
    v = img.size[0]*(i+1) - 2 + img.size[0]
    #v = img.size[0]*(2+i) - 3
    img_list[v] = 120'''
# current pixel = v, left = v-1, right = v+1, topr = v-img.size[0]+1
# top = v-img.size[0], bott = v+img.size[0], topl = v-img.size[0]-1
# bottl = v+img.size[0]-1, bottr = v+img.size[0]+1
##img_list = tuple(img_list)
##img.putdata(img_list)
##img.show()

def createlist(x, lis, y):
    if(y == 1):
        for i in range(x):
            lis.append([0, 0, 0])
    elif(y == 0):
        for i in range(x):
            lis.append(0)

def xaxis(pixel, mode):
    i = 0
    if(mode == 'blur'):
        xfill = np.array([[1, 1, 1],
                          [1, 1, 1],
                          [1, 1, 1]])
        div = 9
    elif(mode == 'gauss_b'):
        xfill = np.array([[1, 2, 1],
                          [2, 4, 2],
                          [1, 2, 1]])
        div = 16
    elif(mode == 'x_edge'):
        xfill = np.array([[-1, 0, 1],
                          [-2, 0, 2],
                          [-1, 0, 1]])
        div = 1
    elif(mode == 'y_edge'):
        xfill = np.array([[-1, -2, -1],
                          [0, 0, 0],
                          [1, 2, 1]])
        div = 1
    elif(mode == 'slant'):
        xfill = np.array([[-1, -1, 0],
                          [-1, 0, 1],
                          [0, 1, 1]])
        div = 1

    img2 = Image.new("RGB", (img.size[0], img.size[1]))
    pix = []
    createlist(len(pixel), pix, 0)
    
    for v in range(img.size[0]+1, len(img_list)-img.size[0]-1):
        if(v >= (img.size[0]*(i+1) + 1) and v <= img.size[0]*(i+1) - 2 + img.size[0]):
            left = pixel[v-1]
            right = pixel[v+1]
            top = pixel[v-img.size[0]]
            bott = pixel[v+img.size[0]]
            topl = pixel[v-img.size[0]-1]
            topr = pixel[v-img.size[0]+1]
            bottl = pixel[v+img.size[0]-1]
            bottr = pixel[v+img.size[0]+1]
            curr = pixel[v]

            img_arr = np.array([[topl, top, topr],
                                [left, curr, right],
                                [bottl, bott, bottr]])

            filled = img_arr*xfill
        
            s = np.sum(filled)

            pix[v] = s/div
        if(v == img.size[0]*(i+1) - 2 + img.size[0]):
            i+=1

    pix = tuple(pix)
    img2.putdata(pix)
    img2.show()
    return img2

#y = xaxis(pixels, 'blur')

def white_it(img):
    img_list = list(img.getdata())
    img2 = Image.new("RGB", (img.size[0], img.size[1]))
    pixel = []
    createlist(len(img_list), pixel, 1)

    for i in range(len(img_list)):
        pixel[i] = list(pixel[i])
        color = img_list[i]
        
        if(color[0] >= 200 and color[1] >= 200 and color[2] >= 200):      #red channel
            pixel[i][0] = 255
            pixel[i][1] = 255
            pixel[i][2] = 255
        else:
            pixel[i] = color

        pixel[i] = tuple(pixel[i])

    img2.putdata(pixel)
    img2.show()
    img2.save("Viraj.jpg")

white_it(img)

def big_blur(pixel):
    img2 = Image.new("L", (img.size[0], img.size[1]))
    pix = []
    createlist(len(pixel), pix, 0)
    i = 0
    
    for v in range(img.size[0]+1, len(img_list)-img.size[0]-1):
        if(v >= (img.size[0]*(i+1) + 1) and v <= img.size[0]*(i+1) - 2 + img.size[0]):
            topl  = pixel[v-img.size[0]-1]
            top   = pixel[v-img.size[0]]
            topr  = pixel[v-img.size[0]+1]
            left  = pixel[v-1]
            right = pixel[v+1]
            bottl = pixel[v+img.size[0]-1]
            bott  = pixel[v+img.size[0]]
            bottr = pixel[v+img.size[0]+1]

            avg = topl + top + topr + left + right + bottl + bott + bottr + pixel[v]
            avg = avg/9;

            pix[v-img.size[0]-1]  = avg
            pix[v-img.size[0]]    = avg
            pix[v-img.size[0]+1]  = avg
            pix[v-1]              = avg
            pix[v+1]              = avg
            pix[v+img.size[0]-1]  = avg
            pix[v+img.size[0]]    = avg
            pix[v+img.size[0]+1]  = avg

            if(v == img.size[0]*(i+1) - 2 + img.size[0]):
                i+=1

    pix = tuple(pix)
    img2.putdata(pix)
    img2.show()
    return img2

#y = big_blur(pixels)

def edge_detect():
    x = xaxis(pixels, 'x_edge')
    y = xaxis(pixels, 'y_edge')
    x = list(x.getdata())
    y = list(y.getdata())
    z = []
    img_edge = Image.new("L", (img.size[0], img.size[1]))
    for i in range(len(x)):
        z.append(x[i] + y[i])
    z = tuple(z)
    img_edge.putdata(z)
    img_edge.show()

#edge_detect()

def listnum(lis):
    s = 0
    for i in range(len(lis)):
        s += (2**i)*int((lis[len(lis)-i-1]))
    return s


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
        

def gray(img):
    img_list = list(img.getdata())
    img2 = Image.new("RGB", (img.size[0], img.size[1]))
    pixel = []
    createlist(len(img_list), pixel, 1)
        
    for i in range(len(img_list)):
        pixel[i] = list(pixel[i])
        pixel[i][0] = img_list[i][0]    #eqauting the red values of all pixels in
        pixel[i][1] = img_list[i][0]    #original to all rgb values in updated
        pixel[i][2] = img_list[i][0]    #can do same with green & blue also
        pixel[i] = tuple(pixel[i])
        
    img2.putdata(pixel)
    img2.show()    
    
def sepRGB(img, thres):
    img_list = list(img.getdata())
    img2 = Image.new("RGB", (img.size[0], img.size[1]))
    pixel = []
    createlist(len(img_list), pixel, 1)
    #pixel = [[0, 0, 0]]*len(img_list)  #if did this, all get same id so if one
                                        #changes other also changes
    for i in range(len(img_list)):
        #print(type(pixel[i]))
        pixel[i] = list(pixel[i])       #if pixel=[[0,0,0]]* then also we need
                                        #to do this (why?) as pixel[i] is already
                                        #a list then why again typecaste it?
        if(img_list[i][0] >= thres):
            pixel[i][0] = img_list[i][0]
        pixel[i] = tuple(pixel[i])

    img2.putdata(pixel)
    img2.show()
