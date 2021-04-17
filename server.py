from flask import Flask, render_template
app = Flask(__name__)

@app.route('/play')
def play_3():
    return render_template("index.html", times=3)

@app.route('/play/<int:number>')
def play_number(number):
    return render_template("index.html", times=number)

@app.route('/play/<int:number>/<color>')
def play_color(number, color):
    return render_template("index.html", times=number, color=color)

if __name__=="__main__":
    app.run(debug=True)