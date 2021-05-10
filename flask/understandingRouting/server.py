from flask import Flask ,render_template # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"
@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    return 'Hello World!'  # Return the string 'Hello World!' as a response
@app.route('/dojo')          # The "@" decorator associates this route with the function immediately following
def dojo():
    return 'Dojo!'  # Return the string 'Hello World!' as a response
@app.route('/say/<name>')          # The "@" decorator associates this route with the function immediately following
def say(name):
    return render_template("index.html",some_name=name)  # Return the string 'Hello World!' as a response
@app.route('/repeat/<num>/<world>')          # The "@" decorator associates this route with the function immediately following
def repeat(num,world):
    return render_template("index2.html",num=int(num),world=world)  # Return the string 'Hello World!' as a response
if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.