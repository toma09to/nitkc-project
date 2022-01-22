import re
strInput1 = input()
strInput1 = re.sub(r'(?=pi|sin|cos|tan|exp|floor)', 'math.', strInput1)
print(strInput1)