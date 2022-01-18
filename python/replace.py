import re
s = input()
strInput = re.sub(r'(?=sin|cos|tan|exp)', 'math.', s).sub(r'\^', '**', s)
print(strInput)