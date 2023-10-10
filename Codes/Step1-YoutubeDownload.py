import tkinter as tk
from tkinter import messagebox
from pytube import YouTube

# Function to download the YouTube video in MP4 format
def download_video():
    video_url = url_entry.get()
    try:
        yt = YouTube(video_url)
        stream = yt.streams.filter(file_extension='mp4').get_highest_resolution()
        stream.download()
        messagebox.showinfo("Download Complete", "Video downloaded successfully!")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Create the main window
root = tk.Tk()
root.title("YouTube Video Downloader")

# Create a label
label = tk.Label(root, text="Enter YouTube URL:")
label.pack(pady=10)

# Create an entry field to enter the URL
url_entry = tk.Entry(root, width=50)
url_entry.pack()

# Create a download button
download_button = tk.Button(root, text="Download MP4", command=download_video)
download_button.pack(pady=20)

# Run the Tkinter main loop
root.mainloop()
