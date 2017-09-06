"""A madlib game that compliments its users."""

from random import choice, sample

from flask import Flask, render_template, request

# "__name__" is a special Python variable for the name of the current module.
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful',
    'smashing', 'lovely',
]

TEMPLATES = ["madlib.html", "madlib1.html", "madlib2.html"]


@app.route('/')
def start_here():
    """Display homepage."""

    return "Hi! This is the home page."


@app.route('/hello')
def say_hello():
    """Say hello to user."""

    return render_template("hello.html")


@app.route('/greet', methods=["POST"])
def greet_person():
    """Greet user with compliment."""

    player = request.form.get("person")

    compliments = sample(AWESOMENESS, 3)

    return render_template("compliment.html",
                           person=player, compliments=compliments)

@app.route('/game', methods=["POST"])
def show_madlib_form():

    answer = request.form.get("answer")

    if answer == 'yes':
        return render_template("game.html")
    else:
        return render_template("goodbye.html")

@app.route('/madlib', methods=["POST"])
def show_madlib():

    person = request.form.get("person")
    color = request.form.get("color")
    noun = request.form.get("noun")
    adj = request.form.get("adj")
    animal = request.form.get("animal")
    foods = request.form.getlist("foods")

    return render_template(choice(TEMPLATES),
                           person=person, color=color, noun=noun, adj=adj, animal=animal, foods=foods)


if __name__ == '__main__':
    # Setting debug=True gives us error messages in the browser and also
    # "reloads" our web app if we change the code.

    app.run(debug=True)
