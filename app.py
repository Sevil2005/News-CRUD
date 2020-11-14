from flask import Flask, render_template, request, redirect, url_for
from db import News, all_news
app = Flask(__name__)

@app.route('/')
@app.route('/news')
def news():
    return render_template('all_news.html', data = all_news)

@app.route('/news/<int:id>')
def one_news(id):
    return render_template('one_news.html', data = all_news, news_id = id)

news_id = 5
@app.route('/new', methods=["GET", "POST"])
def add():
    if request.method == "POST":
        global news_id
        news_id += 1
        title = request.form['title']
        detail = request.form['detail']
        add_news = News(news_id, title, detail)
        all_news.append(add_news)
        return redirect(url_for('news'))
    else:
        return render_template("new_news.html")

@app.route('/news/<int:id>/update', methods=["GET", "POST"])
def update_news(id):
    if request.method == "POST" and id <= news_id:
        ftitle = request.form['title']
        fdetail = request.form['detail']

        for item in all_news:
            if item.id == id:
                item.title = ftitle
                item.details = fdetail
        return redirect(url_for('news'))

    elif request.method == 'GET' and id <= news_id:
        for updating_news in all_news:
            if updating_news.id == id:
                return render_template('update_news.html', updating_news = updating_news)

@app.route('/news/<int:id>/delete', methods=["GET", "POST"])
def delete(id):
    for deleting_news in all_news:
        if deleting_news.id == id:
            all_news.pop(all_news.index(deleting_news))

    return redirect(url_for('news'))


if __name__ == '__main__':
    app.run(debug=True)