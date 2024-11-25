from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_cloud():
  return 'Hello Cloud!This is Mohammed Umar Khan'

app.run(host='0.0.0.0')
