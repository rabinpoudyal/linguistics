import spacy

nlp = spacy.load('en_core_web_sm')

## Personal Pronoun -> (I, you, he, she, it, we, they)
## They are typically used as the nominal subject(nsub) of a verb.
sentence1 = "I am Rabin"
doc1 = nlp(sentence1)

for token in doc1:
    print(token.text, token.dep_)

## In accusative form, a personal pronoun can be assigned
## either 'dobj' or 'iobj', which stands for direct object and indirect
## object, respectively
sentence2 = "We should love them"
doc2 = nlp(sentence2)

for token in doc2:
    print(token.text, token.dep_)

##  Reflexive pronouns also usually act as
## either direct objects or indirect objects

sentence3 = "I love myself"
doc3 = nlp(sentence3)

for token in doc3:
    print(token.text, token.dep_)