import tkinter as tk
from pytube import YouTube

def download_video():
    # Get the YouTube video URL entered by the user
    url = url_entry.get()

    try:
        # Create a YouTube object
        yt = YouTube(url)

        # Get the video stream with the highest resolution
        stream = yt.streams.get_highest_resolution()

        # Download the video to the current working directory
        stream.download()

        # Display a success message
        status_label.config(text="Download complete!", fg="green")
    except:
        # Display an error message if the download fails
        status_label.config(text="Download failed!", fg="red")

# Create the GUI window
window = tk.Tk()
window.title("YouTube Video Downloader")

# Set the window size and position
window.geometry("500x250")
window.resizable(False, False)
window.configure(bg="#F0F0F0")

# Create the input field for the YouTube video URL
url_label = tk.Label(window, text="Enter YouTube URL:", font=("Arial", 14), bg="#F0F0F0")
url_label.pack(pady=10)

url_entry = tk.Entry(window, font=("Arial", 12))
url_entry.pack(pady=5, padx=10)

# Create the download button
download_button = tk.Button(window, text="Download", command=download_video, font=("Arial", 12), bg="#008CBA", fg="white")
download_button.pack(pady=10)

# Create a label for displaying the download status
status_label = tk.Label(window, text="", font=("Arial", 12), bg="#F0F0F0")
status_label.pack()

# Start the GUI loop
window.mainloop()
