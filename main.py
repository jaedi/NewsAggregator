from threading import Lock
from flask import Flask, render_template
from flask_socketio import SocketIO, emit
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen

async_mode = None
app = Flask(__name__)
socketio = SocketIO(app, async_mode=async_mode)

site = "https://www.inquirer.net/"
hdr = {'User-Agent': 'Mozilla/5.0'}
req = Request(site, headers=hdr)
page = urlopen(req)
soup = BeautifulSoup(page, 'html.parser')


@app.route('/')
def index():
    return render_template('index.html', async_mode=socketio.async_mode)

@socketio.event
def my_ping():
    emit('my_pong')


# @socketio.on('latest_news')
# def latest_news():
#     socketio.emit('latest_news', {'title': 'zxc huhuhu', 'source': 'www.zxc.com', 'date': '123123'}, broadcast=True)

@socketio.on('latest_news', namespace='/news')
def latest_news(message):
    news = []
    for a in soup.select('#tr_boxs3'):
        data = {
            'title': a.find('h2').text,
            'source': a.find('a')['href'],
            'date': a.find('span').text
        }
        if(data in news):
            continue
        news.append(data)
    emit('my_response', news)


if __name__ == '__main__':
    socketio.run(app)