import googletrans
import time

print("Here are the available languages:")
time.sleep(1.5)
for k, v in googletrans.LANGUAGES.items():
	print(k, "->", v)

text = input("Enter text to translate > ")
to_lang = input("Enter language to translate to (e.g 'en' for english) ")

try:
	translator = googletrans.Translator()
	result = translator.translate(text, dest=to_lang)
	print(result.text)
except ValueError:
	print("Language not recognised.")
