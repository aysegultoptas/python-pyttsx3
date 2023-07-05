import pyttsx3
engine = pyttsx3.init()
voices = engine.getProperty('voices')
index = 0
for voice in voices:  #bulunan sesler for döngüsü ile ekrana yazdırılır.
   print(f'index-> {index} -- {voice.name}')
   index +=1
engine.runAndWait()

engine.setProperty('voice', voices[0].id)  #0. ses çağırılır --> Microsoft Zira, kadın sesi.
engine.say("Hello world!")

engine.setProperty('voice', voices[1].id)  #1. ses çağırılır --> Microsoft David, erkek sesi.
engine.say("Hello world!")

engine.runAndWait()
