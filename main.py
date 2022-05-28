# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}




def read_file_content(filename):
    # [assignment] Add your code here 
 with open(filename, 'r') as file:
        mainfile = file.read()
 return mainfile
       

    # return file


def count_words():
    text = read_file_content("./story.txt")
    # [assignment] Add your code here
    words_count = {}
 
    
    text_to_list = text.split() 
    # return {"as": 10, "would": 20}
    for word in text_to_list:
        words_count[word] = text_to_list.count(word)
 
    return words_count
 
words_count = count_words()
print(words_count)