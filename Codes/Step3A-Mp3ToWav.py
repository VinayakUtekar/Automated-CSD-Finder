from pydub import AudioSegment
sound = AudioSegment.from_mp3("Song.mp3")
sound.export("Song.wav", format="wav")

# NOTE:
# Above code will work only if the mp3 file is in the directory of python file
# If the song file is in another location folder then add the address along with the Name.
# Eg: "C:\admin\song.mp3" OR "C:\admin\song.wav" 

