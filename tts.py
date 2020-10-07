#Author Timothy Do

import os
print("****Installing Libraries/Dependencies****\n")
print()
try:
	from pydub import AudioSegment
except ModuleNotFoundError:
	os.system("sudo apt-get install ffmpeg")
	print("\nFinished installing ffmpeg\n")
	os.system("sudo pip install pydub")
	print("\nFinished installing pydub\n")
try:
	from gtts import gTTS
except ModuleNotFoundError:
	os.system("sudo pip install gtts")
	print("\nFinished installing gtts\n")
os.system("sudo make")
print("\nFinished making executable for fm_transmittewr\n")
print("\n****Finish Installing Dependencies****\n")

from pydub import AudioSegment


def main():
	txt = raw_input("\nType what the text, it will be speech: ")
	gt = gTTS(txt)
	src = "output.mp3"
	dst = "output.wav"
	gt.save(src)
	sound = AudioSegment.from_mp3(src)
	sound.export(dst,format="wav")
	print("Output has been compiled to output.wav.")
	freq = float(input("Specify the frequency you would like to broadcast: "))
	print("Broadcasting your output at " + str(freq) + " mHZ!")
	os.system("sudo ./fm -f " + str(float(freq)) + " output.wav")
	print("Your output has been compiled and broadcasted.")
	os.system("sudo rm output.wav")
	os.system("sudo rm output.mp3")
	exit()

main()
