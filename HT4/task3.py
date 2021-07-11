import re

text = "     name=Amanda=sssss&age=32&&salary=1500&currency=quro                             "
text = text.replace(" ", "")
array = re.split('&', text)
dict = {}
for element in array:
    array2 = element.split("=")
    if(len(array2) >= 2):
        dict[array2[0]] = array2[1]
print(dict)