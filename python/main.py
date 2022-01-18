from PIL import Image, ImageDraw
import math
import re

INF = 1000000000

# function definition
def sqrt(x):
    if x >= 0:
        return math.sqrt(x)
    else:
        return INF
def pow(x, y):
    if x > 0:
        return math.pow(x, y)
    elif x == 0:
        return 0
    else:
        return INF
def log(x, a):
    if x > 0 and a > 0 and a != 1:
        return math.log(x, a)
    else:
        return INF
def ln(x):
    return log(x, math.e)
def gamma(x):
    if x.is_integer() and x <= 0:
        return INF
    else:
        return math.gamma(x)



# input data
print("Enter the x range of the graph")
displayXRange = float(input()) * 2
print("Enter the y range of the graph")
displayYRange = float(input()) * 2
print("Enter the resolution of the graph")
res = int(input())
print("f(x)= ?")
strInput = input()

# string conversion
strInput = re.sub(r'(?=sin|cos|tan|exp|floor)', 'math.', strInput)
strInput = re.sub(r'\^', '**', strInput)

# define f(x)
def f(x):
    return eval(strInput)

# initialize image
im = Image.new('RGB', (res,res), (255,255,255))
draw = ImageDraw.Draw(im)
lineWidth = math.ceil(res / 500)

fx = []

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

im.save('image.png')