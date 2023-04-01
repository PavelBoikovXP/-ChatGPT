import pyttsx3
import openai
import speech_recognition as sr



def voice(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()




while True :
    r = sr.Recognizer()
    with sr.Microphone(device_index=1) as source:
          print("скажи что нибудь : ")
          audio = r.listen(source)
          command = r.recognize_google(audio , language="ru-RU")
          print("Вы сказали: " +command)
    openai.api_key = "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"

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=command,
        temperature=0.9,
        max_tokens=4000,
        top_p=1,
        frequency_penalty=0.0,
        presence_penalty=0.6,

    )
    print("ИИ:"+response['choices'][0]['text'])
    voice(response['choices'][0]['text'])







