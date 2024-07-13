from translate import Translator #package imported
line = input("Enter line to translate:") #read
lang = languages = [
    "Hindi", #hi
    "Marathi", #mr

]

for languages in lang:
    to = Translator(to_lang = "language") #created translator
    line_translated = to.translate(line) #translate
    print("Language is:", languages, "\tLine is translated as:", line_translated)