import os
import pathlib
import textwrap
from PIL import Image
from dotenv import load_dotenv
import google.generativeai as genai
from IPython.display import display
from IPython.display import Markdown


load_dotenv()
GOOGLE_API_KEY = os.environ.get('GEMINI_API_KEY')
genai.configure(api_key=GOOGLE_API_KEY)


def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))


# for m in genai.list_models():
#   if 'generateContent' in m.supported_generation_methods:
#     print(m.name)


# for text-only prompts

def single_response():
    model = genai.GenerativeModel('gemini-pro')
    try:
        prompt = input("User: ")
        print() # for new line sake
        response = model.generate_content(prompt, stream=True)

        for chunk in response:
            print(chunk.text)
    except Exception as e:
        print(f"{type(e).__name__}: {e}")


def text_from_img():
    model = genai.GenerativeModel('gemini-pro-vision')
    img = Image.open("Lionel-Messi-Argentina-2022-FIFA-World-Cup_(cropped).jpg")

    response = model.generate_content(["Write a short story about this image", img], stream=True)
    response.resolve()

    print(response.text)

text_from_img_text()
