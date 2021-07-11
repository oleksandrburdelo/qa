import re

name = """["FirstItem", "FriendsList", "MyTuple"]"""
name = re.sub(r'(?<!^)(?=[A-EG-LN-Z])', '_', name).lower()
print(name)



