# This line prints a message on the screen
print("to coding journey kaisi chal rhi hai ")

# This line adds 56 and 65 and then prints the result
print(56 + 65)

# This part checks if the Flask module can be imported
try:
    import flask  # Try to import the Flask module
    print("Flask import ho gaya hai!")  # If it works, print this message
except ImportError:
    print("Flask import nahi hua hai.")  # If it doesn't work, print this message

# Import Flask from the flask library
from flask import Flask

# Create an instance of the Flask application
app = Flask(__name__)

# Define what happens when the user visits the homepage ('/')
@app.route('/')
def hello_world():
    return 'i am trying to making a web page '  # Send this message to the user

# Make sure the server runs only if this script is run directly
if __name__ == "__main__":
    # Start the Flask web server
    app.run(host='0.0.0.0', debug=True)
