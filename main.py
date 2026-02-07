import os
from datetime import datetime
from scripts.fetch_news import fetch_top_headlines
from scripts.make_script import make_news_song_script
from scripts.make_voice import make_voice
from scripts.make_subtitles import make_srt
from scripts.make_thumbnail import make_thumbnail
from scripts.render_video import render_video

def main():
    os.makedirs("output", exist_ok=True)

    headlines = fetch_top_headlines(limit=4)
    script_text = make_news_song_script(headlines)

    today = datetime.now().strftime("%b %d, %Y")

    title = f"Breaking News Song ({today}) 🎶🔥 | YoYo Beka News #shorts"

    description = (
        "Yo yo yo! Welcome to YoYo Beka News!\n"
        "Today’s trending world news, delivered in music 🎤🔥\n\n"
        "Today's headlines:\n"
        + "\n".join([f"• {h}" for h in headlines]) +
        "\n\nSubscribe today, don’t delay — tomorrow we sing the news again!\n\n"
        "#shorts #news #worldnews #trending #music #rap #yoyobekanews"
    )

    tags = "shorts,news,worldnews,trending,rap,music,breakingnews,youtube,yoyobekanews"

    with open("output/title.txt", "w", encoding="utf-8") as f:
        f.write(title)

    with open("output/description.txt", "w", encoding="utf-8") as f:
        f.write(description)

    with open("output/tags.txt", "w", encoding="utf-8") as f:
        f.write(tags)

    with open("output/script.txt", "w", encoding="utf-8") as f:
        f.write(script_text)

    make_voice(script_text, "output/voice.mp3")
    make_srt(script_text, "output/subtitles.srt")
    make_thumbnail(headlines[0], "output/thumbnail.jpg")

    render_video()

    print("DONE: YoYo Beka News package created!")

if __name__ == "__main__":
    main()
