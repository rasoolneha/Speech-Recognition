r = sr.Recognizer() # initialise a recogniser    
# listen for audio and convert it to text:    
def record_audio(ask=False):    
    with sr.Microphone() as source: # microphone as source    
        if ask:    
            speak(ask)    
        audio = r.listen(source)  # listen for the audio via source    
        voice_data = ''    
        try:    
            voice_data = r.recognize_google(audio)  # convert audio to text    
        except sr.UnknownValueError: # error: recognizer does not understand    
            speak('I did not get that')    
        except sr.RequestError:    
            speak('Sorry, the service is down') # error: recognizer is not connected    
        print(f">> {voice_data.lower()}") # print what user said    
        return voice_data.lower()     
