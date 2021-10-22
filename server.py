import model # Import the python file containing the ML model
import os
from flask import Flask, request, render_template,jsonify # Import flask libraries
import pickle
model1=pickle.load(open("model.pkl",'rb'))

# Initialize the flask class and specify the templates directory
app = Flask(__name__)

# Default route set as 'home'
@app.route('/')
def home():
    return render_template('home.html') # Render home.html

@app.route('/classify',methods=['GET'])
def classify_type():
    try:
        sepal_len = request.args.get('slen') # Get parameters for sepal length
        sepal_wid = request.args.get('swid') # Get parameters for sepal width
        petal_len = request.args.get('plen') # Get parameters for petal length
        petal_wid = request.args.get('pwid') # Get parameters for petal width

        # Get the output from the classification model
        variety = model.classify(sepal_len, sepal_wid, petal_len, petal_wid,model1)

        # Render the output in new HTML page
        return render_template('output.html', variety=variety)
    except:
        return 'Error'

# Run the Flask server
if(__name__=='__main__'):
    app.run(debug=True)
    
