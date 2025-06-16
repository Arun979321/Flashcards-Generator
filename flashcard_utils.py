import re
import pandas as pd
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO
import zipfile

def parse_flashcards(raw_text):
    pattern = r"\[Difficulty:\s*(.*?)\]\s*Section:\s*(.*?)\s*Q:\s*(.*?)\nA:\s*(.*?)(?=\n\[Difficulty:|\Z)"
    cards = re.findall(pattern, raw_text, re.DOTALL)
    return [
        {
            "difficulty": diff.strip(),
            "section": section.strip(),
            "question": q.strip(),
            "answer": a.strip()
        }
        for diff, section, q, a in cards
    ]
