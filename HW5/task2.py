import pickle

with open('./test/test1/text.txt', 'rb') as file:
    text1 = file.read()
    text2 = pickle.loads(text1)

for text3 in text2:
    print(text3)