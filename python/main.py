from PIL import Image, ImageDraw
import math
import re

INF = 1000000000

# input data
print("Enter the x range of the graph")
displayXRange = float(input()) * 2
print("Enter the y range of the graph")
displayYRange = float(input()) * 2
print("Enter the resolution of the graph")
res = int(input())
print("f(x)= ?")
strInput1 = input()
print("g(x) = ?")
strInput2 = input()
print("h(x) = ?")
strInput3 = input()


# string conversion
strInput1 = re.sub(r'(?=pi|sin|cos|tan|exp|floor|sqrt|pow|log|gamma)', 'math.', strInput1)
strInput1 = re.sub(r'\^', '**', strInput1)
strInput2 = re.sub(r'(?=pi|sin|cos|tan|exp|floor|sqrt|pow|log|gamma)', 'math.', strInput2)
strInput2 = re.sub(r'\^', '**', strInput2)
strInput3 = re.sub(r'(?=pi|sin|cos|tan|exp|floor|sqrt|pow|log|gamma)', 'math.', strInput3)
strInput3 = re.sub(r'\^', '**', strInput3)


# define input function
def f(x):
    return eval(strInput1)
def g(x):
    return eval(strInput2)
def h(x):
    return eval(strInput3)


# initialize image
im = Image.new('RGB', (res,res), (255,255,255))
draw = ImageDraw.Draw(im)
lineWidth = math.ceil(res / 500)
fx,gx,hx = [],[],[]


# initialize graph
draw.line([(0,res / 2), (res,res / 2)], fill='black', width=lineWidth)
for i in range(int(displayYRange) + 1):
    num = res / 2 - res * (math.ceil(displayYRange / 2) - i) / displayYRange
    draw.line([(49 * res / 100, num),(51 * res / 100, num)], fill='black', width=lineWidth)
draw.line([(res / 2,0), (res / 2,res)], fill='black', width=lineWidth)
for i in range(int(displayXRange) + 1):
    num = res / 2 - res * (math.ceil(displayXRange / 2) - i) / displayXRange
    draw.line([(num, 49 * res / 100),(num, 51 * res / 100)], fill='black', width=lineWidth)


# draw graph
for i in range(res):
    x = (i * 2 - res) * displayXRange / (res * 2.0)
    try:
        y = round((displayYRange / 2.0 - f(x)) * res / (displayYRange))
    except:
        y = INF
    fx += [y]
    if i > 0:
        if fx[i-1] < 2 * res and fx[i-1] >= -res and fx[i] < 2 * res and fx[i] >= -res:
            draw.line([(i-1,fx[i-1]), (i,fx[i])], fill='blue', width=lineWidth)
            
for i in range(res):
    x = (i * 2 - res) * displayXRange / (res * 2.0)
    try:
        y = round((displayYRange / 2.0 - g(x)) * res / (displayYRange))
    except:
        y = INF
    gx += [y]
    if i > 0:
        if gx[i-1] < 2 * res and gx[i-1] >= -res and gx[i] < 2 * res and gx[i] >= -res:
            draw.line([(i-1,gx[i-1]), (i,gx[i])], fill='red', width=lineWidth)

for i in range(res):
    x = (i * 2 - res) * displayXRange / (res * 2.0)
    try:
        y = round((displayYRange / 2.0 - h(x)) * res / (displayYRange))
    except:
        y = INF
    hx += [y]
    if i > 0:
        if hx[i-1] < 2 * res and hx[i-1] >= -res and hx[i] < 2 * res and hx[i] >= -res:
            draw.line([(i-1,hx[i-1]), (i,hx[i])], fill='green', width=lineWidth)


# output image
im.save('image.png')