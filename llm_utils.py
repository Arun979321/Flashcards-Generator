import os
import openai



from dotenv import load_dotenv
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_flashcards(text, subject="General", difficulty="Mixed", language="English"):
    # Emphasize language constraint
    difficulty_instruction = ""
    if difficulty.lower() != "mixed":
        difficulty_instruction = f"Only generate flashcards labeled as {difficulty} difficulty."

    prompt = f"""
You are an intelligent AI that generates educational flashcards for {subject} students.

Your task is to:
1. Read the content below.
2. Generate 10–15 flashcards with labeled difficulty (Easy, Medium, or Hard).
3. Group flashcards by topic/section (e.g., "Cell Structure", "Photosynthesis").
4. ✨ Translate all flashcards into **{language}**. This is mandatory.
5. Use clear and student-friendly language.
6. Format strictly as shown below.

⚠️ Do NOT answer in English if the selected language is not English.

Format:
[Difficulty: Easy/Medium/Hard]
Section: <Topic or Section>
Q: <Translated Question>
A: <Translated Answer>

Example:
[Difficulty: Easy]
Section: Introduction to Biology
Q: What is biology the study of?
A: Biology is the study of life.

Content:
{text[:3000]}
"""

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
    )

    return response.choices[0].message.content.strip()
