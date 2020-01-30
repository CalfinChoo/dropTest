#Calvin Chu
#SoftDev pd9
#
#2020

from flask import Flask
import os
app = Flask(__name__) #create instance of class Flask

@app.route("/") #assign following fxn to run when root route requested
def root():
    print(__name__) #where will this go?        In the flask terminal
    return "No hablo queso!"


if __name__ == "__main__":
    app.debug = True
    app.run()
