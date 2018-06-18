lorem_text= "Lorem ipsum dolor sit amet, consectetur"
import re
found = re.search("dolor.*amet",lorem_text)
print(found)