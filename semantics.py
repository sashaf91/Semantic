import spacy
nlp = spacy.load('en_core_web_md')

word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")

print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))

#What is interesting about the result:
# Cat and monkey have a high similarity at 60% (both mammels, can be pets)
# Monkey and banana is less at 40% (monkeys eat bananas)
# However cat and banana are very far from similar at 20% 

#tokens = nlp('p apple monkey banana ')
tokens = nlp('python docker microsoft django ')

for token1 in tokens:
    for token2 in tokens:
            print (token1.text, token2.text, token1.similarity(token2))


sentance_to_compare = "why is my cat on the car"

sentances = [
      "Where did my dog go",
      "Hello, there is my car",
      "I\'ve lost my car in my car",
      "I\'d like my boat back",
      "I will name my dog Diana"
]

model_sentance = nlp(sentance_to_compare)
for sentance in sentances:
    similarity = nlp(sentance).similarity(model_sentance)
    print(sentance + " - ", similarity)