from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/coding4kids')
def coding4kids():
    return render_template('coding4kids.html')

@app.route('/eleven_plus')
def eleven_plus():
    return render_template('eleven_plus.html')

@app.route('/keystages')
def keystages():
    return render_template('keystages.html')

if __name__ == '__main__':
    app.run(debug=True)
