from spellchecker import SpellChecker
print(dir(SpellChecker))
spell=SpellChecker()
def greet(e):
    for word in e:
        print("AutoCorrect by itself with probability")
        print(word,":",spell.correction(word),":","probability",spell.word_usage_frequency(word))
        print("Autocorrection by showing similar words")
        print(spell.candidates(word))
        print("--------------X---------------")
docx=["calandar","ligtening","locotion","misspel","neccessary","recieve","adress"]
c=greet(docx)
print(c)
sent=list(map(str,input("Enter your sentence or word:").split()))
b=greet(sent)
print(b)
