from flask import Flask, render_template, request
import random

app = Flask(__name__)

# Quotes list
quotes = [
     """It’s only after we’ve lost everything that we’re free to do 
    anything.” — Tyler Durden""", 
    
     """The next time you’re told to behave, consider this: obedience
    might be polite, but mischief — that’s where the magic lives.""",
    
    """And those who were seen dancing were thought to be insane by those
    who could not hear the music. — Friedrich Nietzsche""",
    
     """The trickster’s charm lies in their ability to turn the tables
    and leave you questioning everything. – Unknown""",
    
     """A trickster’s greatest weapon is their ability to make you believe
    what you want to believe. – Unknown""",
    
     """Do I really look like a guy with a plan? You know what I am? I’m a
    dog chasing cars. I wouldn’t know what to do with one if I caught it! – The Joker""",
    
     """There is no Yoda — there’s no one who points you in the right
    direction. You’ve got to figure that out by yourself. – The Joker""",
    
     """I know the voices in my head aren’t real, but sometimes their ideas
    are absolutely awesome. – The Joker""",
    
     """It’s like anything in life, visualizing the old man you’re going to become:
    as long as you have a clear picture of that – the life you want to lead – eventually
    you’ll probably get there. – The Joker"""
    
]

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        raw_options = request.form.get('options')
        if raw_options:
            choices = [opt.strip() for opt in raw_options.split(',') if opt.strip()]
            if not choices:
                return render_template('index.html', 
                error="You’ve got to give me something to work with.")
            else:
                final_choice = random.choice(choices) if choices else "Nothing chosen"
            quote = random.choice(quotes)
            return render_template('index.html', decision=final_choice, quote=quote, original=raw_options)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
