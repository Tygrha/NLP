from textblob import TextBlob

with open('text.txt') as f:
    contents = f.read()

txt = contents
blob = TextBlob(txt)
nouns = blob.noun_phrases
print(nouns)

