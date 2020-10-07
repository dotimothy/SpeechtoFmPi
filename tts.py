#Author Timothy Do

import os
print("****Installing Libraries/Dependencies****\n")
os.system("sudo apt-get install libsox-fmt-mp3")
os.system("sudo pip install gtts")
print()
os.system("sudo make")
print("\n****Finish Installing Dependencies****\n")

from gtts import gTTS
import wave


def main():
	txt = raw_input("\nType what the text, it will be speech: ")
	gt = gTTS(txt)
	gt.save("output.mp3")
	os.system("sox output.mp3 -r 44100 -c 1 -b 16 -t wav output.wav")
	print("Output has been compiled to output.wav.")
	freq = float(input("Specify the frequency you would like to broadcast: "))
	print("Broadcasting your output at " + str(freq) + " mHZ!")
	os.system("sudo ./fm -f " + str(float(freq)) + " output.wav")
	print("Your output has been compiled and broadcasted.")
	os.system("sudo rm output.wav")
	os.system("sudo rm output.mp3")
	exit()

main()
