import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty("rate",150) #konuşma hızı belirlenir.
engine.setProperty("volume", 0.5) #ses yüksekliği belirlenir.

engine.say("Hello world!") #seslendirmek istenilen cümle buraya girilir.
engine.runAndWait()
