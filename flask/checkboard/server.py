from flask import Flask,render_template  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"
@app.route('/')          # The "@" decorator associates this route with the function immediately following
def one():
    return render_template("index2.html",x=8,y=8,width=8*60,c1="black",c2="red")  # Return the string 'Hello World!' as a response

@app.route('/<num>')          # The "@" decorator associates this route with the function immediately following
def two(num):
    width=int(num)*60
    return render_template("index2.html",x=8,y=int(num),width=width,c1="black",c2="red")  # Return the string 'Hello World!' as a response

@app.route('/<x>/<y>')          # The "@" decorator associates this route with the function immediately following
def three(x,y):
    width=int(y)*60
    return render_template("index2.html",x=int(x),y=int(y),width=width,c1="black",c2="red")  # Return the string 'Hello World!' as a response

@app.route('/<x>/<y>/<c1>/<c2>')          # The "@" decorator associates this route with the function immediately following
def four(x,y,c1,c2):
    width=int(y)*60
    return render_template("index2.html",x=int(x),y=int(y),width=width,c1=c1,c2=c2)  # Return the string 'Hello World!' as a response
if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.