import tkinter as tk
from tkinter import filedialog, messagebox
from moviepy.editor import *

# Function to convert MP4 to MP3
def convert_to_mp3():
    mp4_file = filedialog.askopenfilename(filetypes=[("MP4 files", "*.mp4")])
    if mp4_file:
        try:
            video = VideoFileClip(mp4_file)
            mp3_file = mp4_file[:-4] + ".mp3"
            video.audio.write_audiofile(mp3_file)
            video.close()
            messagebox.showinfo("Conversion Complete", f"{mp4_file} converted to {mp3_file} successfully!")
        except Exception as e:
            messagebox.showerror("Error", str(e))

# Create the main window
root = tk.Tk()
root.title("MP4 to MP3 Converter")

# Create a label
label = tk.Label(root, text="Select an MP4 file:")
label.pack(pady=10)

# Create a convert button
convert_button = tk.Button(root, text="Convert to MP3", command=convert_to_mp3)
convert_button.pack(pady=20)

# Run the Tkinter main loop
root.mainloop()
