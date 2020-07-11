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
# sentence2 = "We should love them"
# sentence2 = "Don't love me"
sentence2 = "It's her choice"
doc2 = nlp(sentence2)

for token in doc2:
    print(token.text, token.dep_)

##  Reflexive pronouns also usually act as
## either direct objects or indirect objects

sentence3 = "I love myself"
doc3 = nlp(sentence3)

for token in doc3:
    print(token.text, token.dep_)

## Modal auxullary verb 
## “may,” “might,” “can,” “could,”, “must,” “ought,” “shall,” “should,” “will,” and “would,”
## likelihood, permission, capability, necessity, willingness, or advice.

sentence4 = "I wish I could fly"
doc4 = nlp(sentence4)

for token in doc4:
    # Fine grained POS, coarse grained POS -> gives MD, aux
    print(token.tag_, token.dep_)

## Prepositional phrases
## A preposition connects noun phrases with other words in a sentence
## Spatial relation & Temporal relation: “in,” “above,” “under,” “after,” and “before”
## Semantic roles: to, of, for
## Object of preposition -> Noun, Pronoun, or Noun Phrase that follows preposition
## pobj
sentence5 = "I am sleeping in the bed"
doc5 = nlp(sentence5)

for token in doc5:
    print(token.tag_, token.dep_)

## Transitive verbs and direct verbs
## A direct object is a noun (or a noun phrase) denoting something that is directly acted on by a verb.
## A transitive verb accepts a direct object
sentence6 ="I cried untill morning"

doc6 = nlp(sentence6)
for token in doc6:
    print(token.text, token.dep_, token.tag_)
