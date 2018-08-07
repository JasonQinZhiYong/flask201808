from flask import Flask

app = Flask(__name__)
print(app)
print(app.__module__)
print(dir(app))

@app.route('/')
def index():
    return "index pages"

def main():
    app.run(debug=True)

if __name__ == '__main__':
    main()
