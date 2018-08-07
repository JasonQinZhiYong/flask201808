from flask import Flask, jsonify
from flask import abort
from flask import json
from flask import redirect
from flask import request
from flask import url_for

app = Flask(__name__)


class Config(object):
    DEBUG = True


app.config.from_object(Config)


@app.route('/')
def index():
    return "默认页面"

# 带参数的路由


@app.route('/demo1/<int:page_num>')
def demo1(page_num):
    if page_num == 1:
        return "第一页"
    else:
        return "other"

# 发送ppost请求


@app.route("/demo2", methods=["POST", "GET"])
def demo2():
    if request.method == "POST":
        return "post  request"
    elif request.method == "GET":
        return "get request"
    else:
        return "other method"

# 传递json对象


@app.route('/demo3')
def demo3():
    #     定义一个字典类型的数据
    my_dict = {
        "id": 1,
        "name": "jason",
        "age": 12,
        "gender": "gay"
    }
#     使用json.dumps方法，将python对象转换为json字符串
#     return json.dumps(my_dict)
#     下面这个方式需要会去复习一下视频
#     return json.dumps(my_dict), 200, {"Content-Type": "application/json"}
#     下面这种方法推荐使用
    return jsonify(my_dict)

# 请求路径转移


@app.route('/demo4')
def demo4():
    #     使用 redirect
    #     return redirect("/demo3")
    #   使用url_for + redirect()
    re_url = url_for('demo3')   # 传递进要跳转的函数名称，返回一个跳转函数的对应的url路径
    return redirect(re_url)

# 抛出异常


@app.route('/demo5/<int:page_num>')
def demo5(page_num):
    if page_num == 1:
        return 'first page'
    elif page_num > 3:
        return abort(404)   # 抛出异常
    else:
        return 'other'


@app.route('/demo6')
def demo6():
    return "%s" % (100 / 0)

# 创建一个404错误页面


@app.errorhandler(404)
def internal_server_error(e):
    print(request.url)
    print(e)
    return "not found"


@app.errorhandler(ZeroDivisionError)
def internal_server_error(e):
    print(e)
    return "除数不能为0"


def main():
    app.run()


if __name__ == '__main__':
    main()
