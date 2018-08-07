from flask import Flask, jsonify
from flask import json
from flask import redirect
from flask import request
from flask import url_for

app =Flask(__name__)

class Config(object):
    DEBUG = True

app.config.from_object(Config)

@app.route('/')
def index():
    return "默认页面"

# 传递参数给路由
@app.route('/demo/<str_arg>')
def demo(str_arg):
    if str_arg == "center":
        return "center pages"
    else:
        return "other pages"

@app.route('/demo2/<int:pag_num>')
def demo2(pag_num):
    # 如果不设置类型，则传递的参数默认是字符串类型
    if pag_num == 1:
        return "第一页 ，路由传递参数，使用int:关键字指定参数必须为数字"
    elif pag_num == 2:
        return "路由传参，第二页"
    else:
        return "路由传参 其他页"

# post访问
# 服务器处理post请求
@app.route("/demo3", methods=['POST', 'GET'])
def demo3():
    if request.method == "POST":
        return "post request"
    else:
        return "get request"
    # elif request.method == 'GET':
    #     return "get requ est"
    # else:
    #     return "other"

# 返回json
# @app.route('/demo5')
@app.route('/demo5asdfasdl;fhkkjdhafkljhfadkljishfakdhjs')
def d5():
    my_dict = {
        "name":"zhuan",
        "age": 21
    }
#    传递json
    json_o = json.dumps(my_dict)
    print(type(json_o))
    print(json_o)
    # return json.dumps(my_dict)  # 将python对象转换为json字符串
    # return json.dumps(my_dict), 200, {"Content-Type":"application/json"}
    print(type(jsonify(my_dict)))
    print(jsonify(my_dict))
    # 视图函数返回一个json格式的数据给客户端
    # Content-Type: application/json
    return jsonify(my_dict)


# 跳转路由 进入demo6跳转到demo5
@app.route('/demo6')
def demo6():
#     1.使用redirect 写跳转的路径
#     return redirect('/demo5')
#     2.使用url_for + redirect 的方式
    re_url = url_for('d5')  #传入函数引用，获得该函数对应的路由地址
    print(re_url)
    return redirect(re_url)



def main():
    # 当前文件模拟服务器接收请求
    app.run()


if __name__ == '__main__':
    main()