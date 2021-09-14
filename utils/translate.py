from google_trans_new import google_translator
translator = google_translator() 

with open('/path/to/text.txt', 'r') as file:
    data = file.read().replace('\n', '')
    
translate_text = translator.translate(data,lang_src='ru', lang_tgt='en')  
print(translate_text)

f = open("/path/to/translated.txt", "a")
f.write(translate_text)
f.close()
