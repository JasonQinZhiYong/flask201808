from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('temp_index.html')


def main():
    app.run(port=8000)


if __name__ == '__main__':
    main()
