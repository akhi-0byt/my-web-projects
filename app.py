print("to coding journay kaisi chal rhi hai ")
print(56+65)
try:
  import flask
  print("Flask import ho gaya hai!")
except ImportError:
  print("Flask import nahi hua hai.")
from flask import Flask, app
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'i am trying to macking a web page '
if __name__== "__main__":
   app.run(host='0.0.0.0',debug=True)