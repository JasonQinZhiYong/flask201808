from flask import Flask

# static_folder: 用来设置静态资源路径，默认是“static”
# static_url_path: 用来修改访问路径，修改之后访问路径必须是“/st”
# 一般不会修改，使用默认即可
# app = Flask(__name__,static_folder="static", static_url_path="/st")
# app = Flask(__name__,static_folder="static")
app = Flask(__name__)


@app.route('/')
def index():
    return "index pages"


@app.route('/center')
def center():
    return "center pages"


def main():
    print(app.url_map)
    app.run(debug=True)


if __name__ == '__main__':
    main()
