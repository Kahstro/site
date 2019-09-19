from flask import Flask
app= Flask(__name__)

@pp.rout('/')
def index():
    return 'Pagina inicial'

if __name__=='__main__':
    app.run(debug=True)