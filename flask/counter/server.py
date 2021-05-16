from flask import Flask,render_template,request,session,redirect

app = Flask(__name__)    # Create a new instance of the Flask class called "app"
app.secret_key = 'keep it secret, keep it safe' # set a secret key for security purposes

@app.route('/')          # The "@" decorator associates this route with the function immediately following
def one():
    if 'count' not in session:
        session['count']=0
    session['count']+=1
    return render_template("index.html",count=session['count'])  # Return the string 'Hello World!' as a response
@app.route('/addtwo')          # The "@" decorator associates this route with the function immediately following
def three():
    if 'count' not in session:
        session['count']=0
    session['count']+=2
    if 'sick' in session:
        session.pop('sick')
    return render_template("index.html",count=session['count'])  # Return the string 'Hello World!' as a response
@app.route('/destroy_session')          # The "@" decorator associates this route with the function immediately following
def two():
    session.clear()
    return redirect('/')

@app.route('/addx',methods=["POST"])          # The "@" decorator associates this route with the function immediately following
def four():
    print(request.form['num'])
    if 'count' not in session:
        session['count']=0
    session['count']+=int(request.form['num'])
    session['sick']=request.form['num']
    return redirect('/')
if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.