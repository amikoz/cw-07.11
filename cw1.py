from flask import Flask, render_template, request
import cw


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('cw.html')

def finder(g):
    if request.args['word'] == a:
        return word + request.args['key']
    
def main():
    index()
    g = cw.main()
    finder(g)
    
if __name__ == '__main__':
    app.run(debug=True)
    main()
