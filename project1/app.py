#django
#flask
#streamlit
#fast api
#rest api
#front end --> html/css
#backend --> python flask is a web framework 


from flask import Flask , render_template
app = Flask(__name__)


@app.route('/')                    # (/) --> home route 
def home():
    return render_template('index.html')

@app.route('/project')
def project():
    return render_template('project.html')




if __name__ == "__main__":
    app.run(debug=True)
   



