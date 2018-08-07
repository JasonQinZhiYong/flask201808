from flask import Flask
from flask import make_response
from flask import redirect
from flask import render_template
from flask import request
from flask import url_for

app = Flask(__name__)


class Config(object):
    DEBUG = True


app.config.from_object(Config)


@app.route("/", methods=["POST", "GET"])
def index():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        if not all([username, password]):
            print("用户名密码不能为空")
        else:
            print(username, password)
            if username == 'jason' and password == '123':
                # 状态保持,设置用户名到cookie中,表示登陆成功
                print("用户名密码正确")
                response = redirect(url_for("transfer"))
                response.set_cookie('username', username)
                return response
            else:
                print('密码错误')

    return render_template("temp_login.html")


@app.route("/transfer", methods=["POST", "GET"])
def transfer():
    # 从cookie中取到用户名
    username = request.cookies.get('username', None)
    # 如果没有取到代表没有登陆
    print(username)
    if not username:
        return redirect(url_for('index'))

    if request.method == 'POST':
        to_acount = request.form.get('to_acount')
        money = request.form.get('money')
        print('假装执行转账操作,将当前登陆用户的钱转账到指定账户中')
        return '转账%s 元到%s成功' % (money, to_acount)

    response = make_response(render_template('temp_transfer.html'))
    return response


def main():
    app.run(port=9000)


if __name__ == '__main__':
    main()
