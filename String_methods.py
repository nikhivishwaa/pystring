# Methods of string in python

name = "Hello how are You"; b=5
print(len(name))
print(name.startswith("h"))
print(name.startswith("H"))
print(name.startswith("how",6,17))  # New string indexing
print(name.endswith("u"))
print(name.endswith("o"))
print(name.endswith("are",0,13))    # New string indexing
print(name.capitalize())
print(name.upper()) # upper case
print(name.lower()) # lower case
print(b)

clg = "SISTEC"; feels = "!oh  my god!!!!!!!!!!";c="*";u_name = "nikiVishwa1234"
A_name ="ABCdef"
print(clg.isupper())
print(clg.islower())
print(clg.find("VI"))   # false return -1
print(clg.find("SIS"))   # true return 1
print(feels.rstrip("!"))    # removes the trailing character
print(clg.count("S"))   # count "S" how many no. of times present in string 
print(clg.replace("S","T"))
print("12345678901234567890123456789012345678901234567890") #counting
print(clg.center(50))   # 22SISTEC22
print(clg.center(49)+c)   # 22SISTEC21
print(len(clg.center(0)))   # length of clg = 6
print(len(clg.center(50)))   # length = 50
print(feels.split("god")) # returns list of two strings & "god"-> parameter will be removed
print(feels.index("!!"))
print(feels.isalnum())  # feels is Alphanumeric (a-z,A-Z,0-9)
print(name.isalnum())
print(u_name.isalnum()) # "nikiVishwa1234" is Alphanumeric value
print(A_name.isalpha())   # A_name is Alphabetical (A-Z,a-z)
print(name.isalpha())

s = "hi, iam harry\n"
print(s.isprintable())  # is printable -> no escape sequences in string
print(name.isprintable())
print(name.swapcase())  # change lowercase to upper & upper to lower
title = s.title()   # Cpitalize 1st letter of each word
print(title)
print(title.istitle())    # check string is in tittle format or not
print(s.isspace())
space = "     " # using space bar
tab = "     "   # using tab
print(space.isspace())
print(tab.isspace())

# slicing of string

print(name[1])
print(name[1:8])
print(name[0:]) # print complate string [0:17]
print(name[:17])    # print complate string [0:17]
print(name[:])  # print complate string [0:17]
print(name[0::2])   #remove every 2nd character from [0:17:2]
print(name[-17:0])  # dont bo print
print(name[:-1])
print(name[-17:-1)
