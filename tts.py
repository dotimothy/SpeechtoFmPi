from gtts import gTTS
import wave
import os 

def main():
	txt = input("Type what the text, it will be speech: ")
	gt = gTTS(text=txt, lang='en', slow=False)
	gt.save("output.wav")
	print("Output has been compiled to output.wav.")

main()
