with open('text.txt') as f:
    contents = f.read()


word_list=contents


for char in '-.,\n':
    word_list=word_list.replace(char,' ')
word_list = word_list.lower()


word_list = word_list.split()
saved_list = word_list


from collections import Counter
print(Counter(word_list).most_common())
