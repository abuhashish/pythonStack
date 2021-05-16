from flask import Flask,render_template,request  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"
@app.route('/')          # The "@" decorator associates this route with the function immediately following
def one():
    return render_template("index.html")  # Return the string 'Hello World!' as a response
@app.route('/show',methods=['POST'])          # The "@" decorator associates this route with the function immediately following
def two():
    name=request.form['name']
    location=request.form['location']
    language=request.form['language']
    text=request.form['text']
    return render_template("show.html",name=name,location=location,language=language,text=text)  # Return the string 'Hello World!' as a response

    
if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.