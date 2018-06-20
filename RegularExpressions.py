
#__For search particular paragraph or line

quote_text="Let us always meet each other with smile, " \
           "for the smile is the beginning of love"
import re
print(re.search("meet .*smile",quote_text))


#__For search particular word

match=re.search("found",quote_text)
print(type(match))


#__Method 2

a=list(re.finditer("Let .*smile",quote_text))
print(a)


#__For get_number_of_occurrences

def get_number_of_occurrences(string,substring):
    findings=list(re.finditer(substring,string))
    return len(findings)
print(get_number_of_occurrences("Let us always meet each other with smile,for the smile is the beginning of love","smile"))

