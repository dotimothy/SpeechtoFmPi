#Author Timothy Do

print("****Installing Libraries/Dependencies****\n")
os.system("pip install gtts")

from gtts import gTTS
import wave
import os 

def main():
	txt = input("Type what the text, it will be speech: ")
	gt = gTTS(text=txt, lang='en', slow=False)
	gt.save("output.wav")
	print("Output has been compiled to output.wav.")
	freq = float(input("Specify the frequency you would like to broadcast: "))
	print("Broadcasting your output at " + str(freq) + " mHZ!")
	os.system("sudo echo placeholder")
	print("Your output has been compiled and broadcasted.")
	os.system("sudo rm output.wav")
	exit()

main()
