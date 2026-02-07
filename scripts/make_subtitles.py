def format_time(seconds):
    h = int(seconds // 3600)
    m = int((seconds % 3600) // 60)
    s = int(seconds % 60)
    return f"{h:02}:{m:02}:{s:02},000"

def make_srt(text, output_file="output/subtitles.srt"):
    lines = text.split("\n")
    lines = [l.strip() for l in lines if l.strip()]

    start_time = 0
    subtitle_index = 1

    with open(output_file, "w", encoding="utf-8") as f:
        for line in lines:
            duration = max(2, min(4, len(line) // 10))
            end_time = start_time + duration

            f.write(f"{subtitle_index}\n")
            f.write(f"{format_time(start_time)} --> {format_time(end_time)}\n")
            f.write(line + "\n\n")

            subtitle_index += 1
            start_time = end_time
