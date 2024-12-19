# FILE: main.py

from flask import Flask, redirect, request
import requests

app = Flask(__name__)

client_id = "uhvGoDscmT5lj26D5R"
client_secret = "F^2dL!N1Gl&#1YiD%w*sc^!fd69B4c4i"
redirect_uri = "http://127.0.0.1:8080/callback"

token = ""

@app.route("/auth")
def authorize():
    print("执行1")
    auth_url = f"https://dida365.com/oauth/authorize?scope=tasks:write tasks:read&client_id={client_id}&redirect_uri={redirect_uri}&response_type=code&state=state"
    return redirect(auth_url)

@app.route("/callback")
def callback():
    print("执行2")
    code = request.args.get('code')
    state = request.args.get('state')
    # 在这里处理获取到的 code 和 state
    return f"Code: {code}, State: {state}"

if __name__ == "__main__":
    app.run(debug=True, port=8080)