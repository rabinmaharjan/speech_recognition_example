import speech_recognition as sr
import webbrowser as wb

r = sr.Recognizer()
mic = sr.Microphone()
chrome_path = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"


with mic as source:
    print("Say anything...")
    sound = r.listen(source)
    print("Done!")

 
try:
    web =r.recognize_google(sound)
    wb.get(chrome_path).open(web)

except sr.RequestError as e:
    print("error".format(e))

    
    
