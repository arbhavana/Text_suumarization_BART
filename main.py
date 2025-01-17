from flask import Flask, render_template, request
from transformers import BartForConditionalGeneration, BartTokenizer

app = Flask(__name__)

# Loading pre-trained BART model and tokenizer
model = BartForConditionalGeneration.from_pretrained("facebook/bart-large-cnn")
tokenizer = BartTokenizer.from_pretrained("facebook/bart-large-cnn")

def summarize_text(text):
    inputs = tokenizer(text, return_tensors="pt", max_length=1024, truncation=True)
    summary_ids = model.generate(inputs["input_ids"], max_length=150, length_penalty=2.0, num_beams=4, early_stopping=True)
    return tokenizer.decode(summary_ids[0], skip_special_tokens=True)

@app.route('/', methods=['GET', 'POST'])
def home():
    summary = ""
    if request.method == 'POST':
        input_text = request.form['text']
        summary = summarize_text(input_text)
    return render_template('index.html', summary=summary)

if __name__ == "__main__":
    app.run(debug=True)
