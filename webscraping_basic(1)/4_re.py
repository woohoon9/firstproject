import re

p = re.compile("ca.e") 
#. (ca.e): meaing a character- care, cafe, case (0) | caffe (X)
# #^(^de): the start of characters - desk, destination(0) | fade(X)
#$(se$) : the end of characters - case, base (0) | face(X)
m = p.match("caffe")
# print(m.group()) #if not matched, error occur

def print_match(m):
    if m:
        print("m.group():", m.group()) #return the matched characters
        print("m.string:", m.string) # return input characters 
        print("m.start:", m.start()) # start index of matched characters
        print("m.end():", m.end()) # end index of matched characters
        print("m.span():", m.span()) # start and end index of matched characters
    else:
        print("not matched")

# m=p.match("careless") # verifying the characters are matched from the head of sentence.
# print_match(m)

# m= p.search("good care") # search: verifying the match parts in the given character lines. 
# print_match(m)

lst=p.findall("good care cafe") # findall : return all matched in the form of list
print(lst)

#1. re.compile("compile the form wanted")
#2. m=p.match("characters  to be compared")
#3. m=p.search("characters to be compared")
#4. lst=p.findall("characters to be compared")

# the form wanted
#. (ca.e): meaing a character- care, cafe, case (0) | caffe (X)
# #^(^de): the start of characters - desk, destination(0) | fade(X)
#$(se$) : the end of characters - case, base (0) | face(X)