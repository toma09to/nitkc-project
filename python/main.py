from PIL import Image, ImageDraw
import math

INF = 10000000000

print("Enter the x range of the graph")
displayXRange = float(input())
print("Enter the y range of the graph")
displayYRange = float(input())
print("Enter the resolution of the graph")
res = int(input())
print("f(x)= ?")
strInput = input()

def f(x):
    return eval(strInput)

im = Image.new('RGB', (res+1,res+1), (255,255,255))
draw = ImageDraw.Draw(im)
lineWidth = math.ceil(res / 500)

fx = []

draw.line([(0,res / 2), (res,res / 2)], fill='black', width=lineWidth)
draw.line([(res / 2,0), (res / 2,res)], fill='black', width=lineWidth)

for i in range(res+1):
    x = (i * 2 - res) * displayXRange / res
    fx += [round((displayYRange - f(x)) * res / (displayYRange * 2.0))]
    if i > 0 :
        draw.line([(i-1,fx[i-1]), (i,fx[i])], fill='blue', width=lineWidth)

im.save('image.png')