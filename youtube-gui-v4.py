import os
import tkinter as tk
from pytube import YouTube
from moviepy.editor import VideoFileClip

def download_video():
    # Get the YouTube video URL entered by the user
    url = url_entry.get()

    try:
        # Create a YouTube object
        yt = YouTube(url)

        # Get the video stream with the highest resolution
        stream = yt.streams.get_highest_resolution()

        # Create a new directory for downloaded videos if it doesn't exist
        download_dir = os.path.join(os.path.dirname(__file__), "Downloads")
        if not os.path.exists(download_dir):
            os.mkdir(download_dir)

        # Download the video to the downloads directory
        video_filename = stream.download(output_path=download_dir)

        # Enable the convert button
        convert_button.config(state="normal")

        # Display a success message
        status_label.config(text="Download complete!", fg="green")

        # Return the stream object for converting the video
        return stream
    except:
        # Display an error message if the download fails
        status_label.config(text="Download failed!", fg="red")

def convert_video(stream):
    # Get the path of the downloaded video
    video_filename = stream.default_filename

    try:
        # Convert the video to MP3 format
        video = VideoFileClip(video_filename)
        audio_filename = os.path.join(os.path.dirname(__file__), "downloads", video_filename.replace(".mp4", ".mp3"))
        audio = video.audio
        audio.write_audiofile(audio_filename)
        video.close()
        audio.close()

        # Display a success message
        status_label.config(text="Conversion complete!", fg="green")
    except:
        # Display an error message if the conversion fails
        status_label.config(text="Conversion failed!", fg="red")

def clear_url():
    # Clear the text field
    url_entry.delete(0, tk.END)

# Create the GUI window
window = tk.Tk()
window.title("YouTube Video Downloader")

# Set the window size and position
window.geometry("500x300")
window.resizable(False, False)
window.configure(bg="#F0F0F0")

# Create the input field for the YouTube video URL
url_label = tk.Label(window, text="Enter YouTube URL:", font=("Arial", 14), bg="#F0F0F0")
url_label.pack(pady=10)
url_entry = tk.Entry(window, font=("Arial", 12), width=35)  # Set the width to 50
url_entry.pack(pady=5, padx=10)

# Create the download button
download_button = tk.Button(window, text="Download", command=download_video, font=("Arial", 12), bg="#008CBA", fg="white")
download_button.pack(pady=10)

# Create a label for displaying the download status
status_label = tk.Label(window, text="", font=("Arial", 12), bg="#F0F0F0")
status_label.pack()

# Create the convert button (disabled by default)
convert_button = tk.Button(window, text="Convert to MP3", command=lambda: convert_video(download_video()), font=("Arial", 12), bg="#008CBA", fg="white", state="disabled")
convert_button.pack(pady=10)

# Create the clear button
clear_button = tk.Button(window, text="Clear", command=clear_url, font=("Arial", 12), bg="#008CBA", fg="white")
clear_button.pack(pady=10)

# Start the GUI loop
window.mainloop()