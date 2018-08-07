from flask import Flask
from flask import request

app = Flask(__name__)

class Config(object):
    DEBUG=True

app.config.from_object(Config)

@app.route('/')
def index():
    return '默认页面'

# 通过url的方式请求参数
# /demoargs?name=jaosn&age=19
@app.route('/demoargs')
def demoargs():
    print(request.args.get('name'))
    print(request.args.get('age'))
    return 'args'

# 使用request
@app.route('/demo1', methods=['POST', 'GET'])
def demo1():
    print(request.url)
    print(request.method)
    print(request.headers)
    return 'demo1'

# 接收post信息，form表单数据
@app.route('/demo2', methods=['POST'])
def demo2():
    print(request.form.get('name'))
    print(request.form.get("age"))
    return 'post get name'

# 传递图片
@app.route('/demo3', methods=['POST'])
def demo3():
    file = request.files.get('pic')
    print(file)
    file.save('./1.jpg')
    return "传递参数"


def main():
    app.run()


if __name__ == '__main__':
    main()