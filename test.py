import speech_recognition as sr

# List all available microphone devices
mic_list = sr.Microphone.list_microphone_names()

for i, microphone_name in enumerate(mic_list):
    print(f"Microphone with index {i}: {microphone_name}")
 