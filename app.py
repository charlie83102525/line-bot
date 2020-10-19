from flask import Flask, request, abort #用flask架設伺服器


from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi('pd+ozecWVTmcbqNeKmPNFf5JtkkhmJo4ELm2NT7d+0kR0nHDLndzIhp0H6Xh2/19TZCNdEydWH0rNOstXXv6+nuqa1g8OByP6EmGVbLYGsD3GC1Sus36DRfh1agyjZy5reufPMown4Cqiv/YBU9PRQdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('72819c8cc7cd0b793af5431e5e632320')


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msg = event.message.text
    r = '我看不懂你說什麼'


    if msg == 'hi':
        r = 'hi'
    elif msg == '你吃飯了嗎':
        r = '還沒'

    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=r))


if __name__ == "__main__":
    app.run()