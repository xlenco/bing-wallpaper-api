from flask import Flask, redirect
import requests

app = Flask(__name__)

@app.route('/')
def index():
    try:
        # 发送请求获取壁纸数据
        response = requests.get("https://cn.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1&mkt=zh-CN")
        response.raise_for_status()  # 确保请求成功

        # 解析JSON数据
        data = response.json()

        # 获取壁纸URL的相对路径
        relative_image_url = data['images'][0]['url']

        # 构建完整的壁纸URL
        full_image_url = "https://cn.bing.com" + relative_image_url

        # 直接重定向到壁纸URL
        return redirect(full_image_url, code=302)

    except Exception as e:
        # 如果出现错误，返回错误页面或者处理错误
        # 这里简单地返回一个错误信息
        return "An error occurred. Please try again later.", 500

if __name__ == '__main__':
    # 在本地主机的上运行Flask应用
    app.run()
