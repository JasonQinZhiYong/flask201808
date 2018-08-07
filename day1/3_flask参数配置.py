from flask import Flask
app = Flask(__name__)

# 测试app.run配置， 公司里面app.config.from_boject
# 写在配置对象中
class Config(object):
    DEBUG = True

    SERVER_NAME

# 1.以配置对象的方式    公司中一般使用这种方式，可以灵活修改配置参数
# app.config.from_object(Config)

# 2.以配置文件的方式
app.config.from_pyfile('config.ini')


@app.route('/')
def index():
    # return "index"
    return "%d" %(11/10)


def main():
    # 进入debug模式
    # 1.可以进入到调试模式
    # 2.不用在重新启动项目
    # app.run(debug=True)

    # 3.port 修改端口

    app.run()


if __name__ == '__main__':
    main()