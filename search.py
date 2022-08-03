# import re
# txt = "use of python in machine learning"
# x=re.search("^use"
#             ".*machine",txt)
# if ( x):
#     print("yes!we have a match!")
# else:
#     print("no match")



#**find all random**

# import re
# txt="use of python in machine learning"
# x=re.findall("e",txt)
# print(x)



                   #  search program

import re
txt ="python is on of the most popular languages"
searchonj=re.search("\s",txt)
print("the first white space character is located",searchonj)
