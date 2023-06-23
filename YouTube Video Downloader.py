import tkinter as tk
from tkinter import messagebox, ttk
import youtube_dl

def download_video(audio_only=False):
    url = url_entry.get()
    quality = quality_var.get()
    try:
        ydl_opts = {
            'format': 'bestaudio/best' if audio_only else quality,
            'postprocessors': [{'key': 'FFmpegExtractAudio', 'preferredcodec': 'mp3',}] if audio_only else []
        }
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        messagebox.showinfo("Başarılı", "Video başarıyla indirildi")
    except Exception as e:
        messagebox.showerror("Hata", str(e))

root = tk.Tk()
root.title("YouTube Video İndirici")

style = ttk.Style()
style.configure("TButton",
                foreground="midnight blue",
                background="white",
                font=("Arial", 12, "bold"),
                padding=10)

style.configure("TEntry",
                foreground="midnight blue",
                background="white",
                font=("Arial", 12),
                padding=10)

frame = ttk.Frame(root, padding="10 20 10 20")
frame.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S))

url_label = ttk.Label(frame, text="YouTube Video URL:")
url_label.grid(column=0, row=0, sticky=tk.W)

url_entry = ttk.Entry(frame, width=50)
url_entry.grid(column=0, row=1, sticky=(tk.W, tk.E))

quality_label = ttk.Label(frame, text="Video Kalitesi:")
quality_label.grid(column=0, row=2, sticky=tk.W)

quality_var = tk.StringVar()
quality_combobox = ttk.Combobox(frame, textvariable=quality_var)
quality_combobox['values'] = ('720p', '480p', '360p', '240p', '144p')
quality_combobox.grid(column=0, row=3, sticky=(tk.W, tk.E))

download_video_button = ttk.Button(frame, text="Videoyu İndir", command=lambda: download_video(audio_only=False))
download_video_button.grid(column=0, row=4, sticky=tk.W)

download_audio_button = ttk.Button(frame, text="Sesini İndir", command=lambda: download_video(audio_only=True))
download_audio_button.grid(column=0, row=5, sticky=tk.W)

for child in frame.winfo_children():
    child.grid_configure(padx=5, pady=5)

root.mainloop()
