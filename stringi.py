def createWordUnderscore(list):
    finalstring = ""
    for i in list:
        if i == None:
            finalstring+="  "
        else:
            finalstring+=i+" "
    return finalstring
def findLetters(word,letter):
    sl = 0
    pl = []
    for i in word.lower():
        if i.lower() == letter.lower():
            pl.append(sl)
        sl=sl+1
    return pl
def formatInco(l):
    finalstring = "Niepoprawne litery: "
    for i in l:
        finalstring+=i+", "
    return finalstring