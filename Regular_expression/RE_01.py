# import re

# string = "quick is a fox"
# pattern = r"quick"

# match = re.match(pattern,string)
# if match:
#     print("Match found:" , match.group())
# else:
#     print("no match")

import re

string = "this is a quick fox"
pattern = r"quick"

match = re.match(pattern,string)
if match:
    print("Match found:" , match.group())
else:
    print("no match")
