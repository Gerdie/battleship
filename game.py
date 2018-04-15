from flask import Flask, request

app = Flask(__name__)

width = 5
length = 5

GAMEBOARD = [['?'] * width for l in xrange(length)]


def _render_gameboard():
    board_str = map(lambda x: ' '.join(x), GAMEBOARD)
    return '<br/>'.join(board_str)


@app.route('/')
def homepage():
    return _render_gameboard()


if __name__ == '__main__':
    app.run()
