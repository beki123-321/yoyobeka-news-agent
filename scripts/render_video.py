import os
import random
import subprocess

def render_video():
    beats_folder = "assets/beats"
    beats = [f for f in os.listdir(beats_folder) if f.endswith(".mp3")]
    beat_file = os.path.join(beats_folder, random.choice(beats))

    filter_complex = (
        "[0:v]scale=1080:1920,zoompan=z='min(1.15,1+0.0005*on)':d=1:s=1080x1920:fps=30[bg];"
        "[3:v]scale=750:-1[char];"
        "[bg][char]overlay=x=(W-w)/2:y=(H-h)/2+20*sin(2*PI*t*1.5):format=auto,"
        "subtitles=output/subtitles.srt:force_style='Fontsize=48,Outline=3,Shadow=1,Alignment=2'[v];"
        "[1:a]volume=1.4[voice];"
        "[2:a]volume=0.25[beat];"
        "[voice][beat]amix=inputs=2:duration=first:dropout_transition=2[a]"
    )

    cmd = [
        "ffmpeg", "-y",
        "-loop", "1", "-i", "assets/studio.jpg",
        "-i", "output/voice.mp3",
        "-i", beat_file,
        "-i", "assets/character.png",
        "-filter_complex", filter_complex,
        "-map", "[v]",
        "-map", "[a]",
        "-t", "90",
        "-r", "30",
        "-pix_fmt", "yuv420p",
        "output/final_video.mp4"
    ]

    subprocess.run(cmd, check=True)
