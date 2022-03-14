from flask import Flask, render_template, session, redirect

app = Flask(__name__)
app.secret_key = "Keep it secret"

@app.route('/')          
def index():
    if 'count' not in session: # if 'key' of count is not in dictionary 'session'.  If it's been cleared and/or first visit to the page.
        session['count'] = 0
    session['count'] += 1 


    return render_template("index.html")

@app.route('/clear')
def clear_info():
    session.clear()
    return 	redirect('/')	 


if __name__=="__main__":  
    app.run(debug=True)   