import multiprocessing
import time
import ui
import stringi
""
error = 0
def e():
    try:
        exec(open("server.py").read())
    except Exception as e:
        print("Fail detected")
        print("In server.py: "+e)
        print(e.with_traceback())
def runWordServer():
    multiprocessing.Process(target=e,daemon=True).start()
try:
    word = ui.getWord()
    cat = ui.getCategory()
    errs = []
    unders = []
    for i in word:
        if i ==" ":
            unders.append(None)
        else:
            unders.append("_")
    ui.init()
    runWordServer()
    ui.updateDisplay(stringi.createWordUnderscore(unders),0,cat,stringi.formatInco(errs))
    while True:
        start = time.time()
        w = ui.getLetter(errs)
        if time.time() - start < 0.5:
            ui.cheatDetect(word)
            raise SystemExit
        if stringi.findLetters(word,w) == []: 
            error=error+1
            errs.append(w)
        if error>12 or error==12:
            strd = []
            for i in word:
                if i == " ":
                    strd.append(None)
                else:
                    strd.append(i)
            ui.updateDisplay(stringi.createWordUnderscore(strd),error,cat,stringi.formatInco(errs))
            ui.lost(word)
            break
        
        for i in stringi.findLetters(word,w):
                unders[i] = word[i]
        ui.updateDisplay(stringi.createWordUnderscore(unders),error,cat,stringi.formatInco(errs))
        try:
            unders.index("_")
        
        except Exception as e:
            ui.win(word,error)
            break
except Exception as e:
    print("Fail detected")
    print(f"In main.py: {e}")
    print(e.with_traceback())
        
