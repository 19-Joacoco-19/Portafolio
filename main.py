from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():

    # Variables de proyectos
    button_python = None
    button_discord = None
    button_html = None
    button_db = None

    if request.method == 'POST':

        # Botones de habilidades
        button_python = request.form.get('button_python')
        button_discord = request.form.get('button_discord')
        button_html = request.form.get('button_html')
        button_db = request.form.get('button_db')

        # Formulario de feedback
        email = request.form.get('email')
        text = request.form.get('text')

        if email and text:
            connection = sqlite3.connect('feedback.db')
            cursor = connection.cursor()

            cursor.execute('''
                CREATE TABLE IF NOT EXISTS feedback (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    email TEXT,
                    comment TEXT
                )
            ''')

            cursor.execute(
                "INSERT INTO feedback (email, comment) VALUES (?, ?)",
                (email, text)
            )

            connection.commit()
            connection.close()

    return render_template(
        'index.html',
        button_python=button_python,
        button_discord=button_discord,
        button_html=button_html,
        button_db=button_db
    )

if __name__ == "__main__":
    app.run(debug=True)