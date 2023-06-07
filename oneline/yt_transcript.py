import re
from youtube_transcript_api import YouTubeTranscriptApi


def yt_transcript(link: str):
    index = link.find("=")
    vid_ids = link[index + 1 :]
    dicts = YouTubeTranscriptApi.get_transcript(vid_ids, languages=["vi"])
    texts = [i["text"] for i in dicts]
    text = " ".join(texts)

    # Regular expression pattern to match text enclosed in
    # parentheses or square brackets
    pattern = r"\([^)]*\)|\[[^\]]*\]"

    # Remove the matched patterns from the text
    cleaned_text = re.sub(pattern, "", text)

    # Remove excessive whitespace
    cleaned_text = re.sub(r"\s+", " ", cleaned_text)

    # Strip leading and trailing whitespace
    cleaned_text = cleaned_text.strip()

    return cleaned_text
