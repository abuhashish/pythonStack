from flask import Flask,render_template,request,session,redirect
import random
app = Flask(__name__)    # Create a new instance of the Flask class called "app"
app.secret_key = 'keep it secret, keep it safe' # set a secret key for security purposes

@app.route('/')          # The "@" decorator associates this route with the function immediately following
def one():
    session['attempts']=0
    session['num']=random.randint(1, 10) 
    print(session['num'])
    return render_template("index.html",count=session['num'])  # Return the string 'Hello World!' as a response
@app.route('/check',methods=['POST'])          # The "@" decorator associates this route with the function immediately following
def two():
    session['attempts']+=1
    num=int(request.form['num'])
    if num>session['num']:
        session['red']=1
    elif num<session['num']:
        session['red']=1
    else:
        session['green']=1
    return render_template("index.html")  # Return the string 'Hello World!' as a response
@app.route('/again')          # The "@" decorator associates this route with the function immediately following
def three():
    session.clear()
    return redirect("/")  # Return the string 'Hello World!' as a response
list=[]
@app.route('/leaderboard',methods=['post'])          # The "@" decorator associates this route with the function immediately following
def four():
    name=request.form['name']
    attempt=session['attempts']
    list.append(
        {'name':name,
        'attempt':attempt}
    )
    return render_template("leaderboard.html",list=list)

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.