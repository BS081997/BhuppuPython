
#__For search particular paragraph or line

quote_text="Let us always meet each other with smile, " \
           "for the smile is the beginning of love"
import re
print(re.search("meet .*smile",quote_text))


#__Method 2

a=list(re.finditer("Let .*smile",quote_text))
print(a)


#__For search particular word

match=re.search("found",quote_text)
print(type(match))


#__For get_number_of_occurrences

def get_number_of_occurrences(string,substring):
    findings=list(re.finditer(substring,string))
    return len(findings)
print(get_number_of_occurrences("Let us always meet each other with smile,for the smile is the beginning of love","smile"))


a=re.search(r'..d','food baar')
print(a)



def is_valid_Python_variable_name(string):
    found = re.match("[_A-Za-z][_a-zA-Z0-9]*",string)
    return  bool(found)
print(is_valid_Python_variable_name("the"))


