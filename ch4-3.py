import spacy
nlp = spacy.load('en_core_web_sm')

#doc = nlp("Berlin is the capital of Germany")
#doc.ents

#print(doc.ents[0],doc.ents[0].label_)
f = open(".\\filetext\\tim_cook.txt", "r")
article = f.read()
doc = nlp(article)
# Print all of the found entities and their labels
for ent in doc.ents:
    print(ent.label_, ent.text)