from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>My Travel Blog</title>
    </head>
    <body>
        <h1>Welcome to My Blog</h1>
        <p>Read more about my trip to Paris 
        <a href="https://example.com/paris" target="_blank">here</a>.</p>
    </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(debug=True)
