# from flask import Flask,render_template  # Import Flask to allow us to create our app
# app = Flask(__name__)    # Create a new instance of the Flask class called "app"
# @app.route('/play')          # The "@" decorator associates this route with the function immediately following
# def play():
#     return  render_template("index.html")
# if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
#     app.run(debug=True)    # Run the app in debug mode.

# from flask import Flask,render_template  # Import Flask to allow us to create our app
# app = Flask(__name__)    # Create a new instance of the Flask class called "app"
# @app.route('/play/<num>')          # The "@" decorator associates this route with the function immediately following
# def play2(num):
#     return  render_template("index2.html",num=int(num))
# if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
#     app.run(debug=True)    # Run the app in debug mode.

from flask import Flask,render_template  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"
@app.route('/play/<num>/<color>')          # The "@" decorator associates this route with the function immediately following
def play2(num,color):
    return  render_template("index3.html",num=int(num),color=color)
if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.