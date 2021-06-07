import pyttsx3
import speech_recognition as sr
import webbrowser
import os

en = pyttsx3.init()

def voz ():
    en.setProperty('voice', b'brazil')
    en.setProperty('rate', 180)
    en.setProperty('volume', 1)
    en.runAndWait()

en.say('olá, o que você deseja fazer nesse momento')
voz()

recon =sr.Recognizer()
with sr.Microphone() as source:
    while True:
        audio = recon.listen(source)
        resposta = recon.recognize_google(audio,language='pt')
        print(resposta)
        if resposta == "Abrir Google":
            en.say('Ok, abrindo seu navegador na página do google')
            voz()

            webbrowser.open("www.google.com")

        elif resposta == "abrir YouTube":
            en.say('ok, abrindo o youtube')
            voz()
            webbrowser.open("www.youtube.com.br")

        elif resposta =="quero fazer um cálculo":
            while True:
                en.say('informe os números que deseja multiplicar')
                voz()
                audio = recon.listen(source)
                soma = recon.recognize_google(audio, language='pt')
                if soma == 'obrigado pela ajuda': break
                print("sua multiplicação: " + str(soma))
                Resultado = str(int(soma[0]) * int(soma[4]))
                print("o resultado é"+ Resultado)
                en.say('O resultado é'+ str(Resultado))
                voz()

        elif resposta == "acessar notícia":
            en.say('OK, acessando as noticias...')
            voz()
            webbrowser.open('www.terra.com.br')

        elif resposta=="ouvir música":
            en.say('Ok, executando a música')
            voz()
            os.system('musica.mp3')

        elif resposta == "quero assistir Prime vídeo":
            en.say('OK, vamos assistir Prime vídeo...')
            voz
            webbrowser.open('www.primevideo.com')

        elif resposta == "Quero ver minhas notas de sistemas multimídias":
            voz()
            webbrowser.open('https://docs.google.com/spreadsheets/d/1-gDh2ois13yJ8lrLl_4-2BkQFd-qMo-XKcHGbvDUYQs/edit#gid=0')

        elif resposta == "Obrigado pela ajuda":
            en.say('OK, até mais...')
            voz()
            break

        else:
            en.say('Desculpe comando não reconhecido, por favor repita')
            voz()
            print('Desculpe comando não reconhecido...')