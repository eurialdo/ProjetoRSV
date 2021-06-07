import pyttsx3
import speech_recognition as sr
import webbrowser
import os

en = pyttsx3.init()

en.say('olá, o que você deseja fazer nesse momento')
en.setProperty('voice', b'brazil')
en.setProperty('rate', 180)
en.setProperty('volume', 1)
en.runAndWait()

recon =sr.Recognizer()
with sr.Microphone() as source:
    while True:
        audio = recon.listen(source)
        resposta = recon.recognize_google(audio,language='pt')
        print(resposta)
        if resposta == "desejo acessar o Google":
            en.say('Ok, abrindo seu navegador na página do google')
            en.setProperty('voice', b'brazil')
            en.setProperty('rate', 180)
            en.setProperty('volume', 1)
            en.runAndWait()

            webbrowser.open("www.google.com")

        elif resposta == "desejo acessar o YouTube":
            en.say('ok, abrindo o youtube')
            en.setProperty('voice', b'brazil')
            en.setProperty('rate', 180)
            en.setProperty('volume', 1)
            en.runAndWait()
            webbrowser.open("www.youtube.com.br")

        elif resposta == "desejo acessar notícia":
            en.say('OK, acessando as noticias...')
            en.setProperty('voice', b'brazil')
            en.setProperty('rate', 180)
            en.setProperty('volume', 1)
            en.runAndWait()
            webbrowser.open('www.terra.com.br')

        elif resposta=="desejo ouvir música":
            en.say('Ok, executando a música')
            en.setProperty('voice',b'brazil')
            en.setProperty('rate', 180)
            en.setProperty('volume', 1)
            en.runAndWait()
            os.system('musica.mp3')

        elif resposta == "obrigado":
            en.say('OK, até mais...')
            en.setProperty('voice', b'brazil')
            en.setProperty('rate', 180)
            en.setProperty('volume', 1)
            en.runAndWait()
            break

        else:
            en.say('Desculpe comando não reconhecido, por favor repita')
            en.setProperty('voz', b'brazil')
            en.setProperty('rate', 180)
            en.setProperty('volume', 1)
            en.runAndWait()
            print('Desculpe comando não reconhecido...')