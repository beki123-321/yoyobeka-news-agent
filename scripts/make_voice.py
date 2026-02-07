import asyncio
import edge_tts

VOICE = "en-US-GuyNeural"

async def generate_voice(text, output_file):
    communicate = edge_tts.Communicate(text, VOICE)
    await communicate.save(output_file)

def make_voice(text, output_file="output/voice.mp3"):
    asyncio.run(generate_voice(text, output_file))
