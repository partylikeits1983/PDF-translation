from transformers import T5ForConditionalGeneration, T5Tokenizer

# initialize the model architecture and weights
model = T5ForConditionalGeneration.from_pretrained("t5-large")
# initialize the model tokenizer
tokenizer = T5Tokenizer.from_pretrained("t5-large")

text = open('0.txt', 'r').read()

#text = '''text'''

# encode the text into tensor of integers using the appropriate tokenizer
inputs = tokenizer.encode("summarize: " + article, return_tensors="pt", max_length=512, truncation=True)

# generate the summarization output
outputs = model.generate(
    inputs, 
    max_length=250, 
    min_length=110, 
    length_penalty=4.0, 
    num_beams=4, 
    early_stopping=True)
# just for debugging
print(outputs)
print(tokenizer.decode(outputs[0]))
