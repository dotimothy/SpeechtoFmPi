#Author Timothy Do

import os 

print("****Installing Libraries/Dependencies****\n")
os.system("sudo pip install gtts")
os.system("sudo make")
print("****Finish Installing Dependencies****\n")

from gtts import gTTS
import wave


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
