def speak(audio_string):    
tts = gTTS(text=audio_string, lang='en') # text to speech(voice)    
r = random.randint(1,20000000)    
audio_file = 'audio' + str(r) + '.mp3'    
tts.save(audio_file) # save as mp3    
playsound.playsound(audio_file) # play the audio file    
print(f"May Day: {audio_string}") # print what app said    
os.remove(audio_file) # remove audio file     
