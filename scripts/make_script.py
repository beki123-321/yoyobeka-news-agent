import random
from datetime import datetime

def make_news_song_script(headlines):
    hooks = [
        "STOP SCROLLING! Today’s news is wild!",
        "Yo yo yo! This one is crazy!",
        "Wait wait wait... you NEED to hear today’s news!",
        "Breaking news vibes, let’s go!"
    ]

    hook = random.choice(hooks)
    today = datetime.now().strftime("%B %d")

    intro = (
        f"{hook}\n"
        f"Yo yo yo! Welcome to YoYo Beka News!\n"
        f"It’s {today}, and I’m singing the headlines for you!"
    )

    chorus = (
        "Daily news, daily tune!\n"
        "Fast facts, no afternoon!\n"
        "If you like this crazy flow,\n"
        "Hit subscribe, let’s go!"
    )

    verses = []
    for i, h in enumerate(headlines, start=1):
        verses.append(
            f"Story {i}, listen up right now!\n"
            f"{h}!\n"
            f"People talking, trending strong,\n"
            f"YoYo Beka keeps it going with the song!"
        )

    outro = (
        "Yo yo yo! That’s the news in music!\n"
        "Subscribe today, don’t delay — tomorrow we sing again!"
    )

    full_text = (
        intro + "\n\n" +
        verses[0] + "\n\n" +
        verses[1] + "\n\n" +
        chorus + "\n\n" +
        verses[2] + "\n\n" +
        verses[3] + "\n\n" +
        outro
    )

    return full_text
