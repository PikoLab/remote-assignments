from flask import (Flask, request, render_template, jsonify, make_response,
                    redirect, url_for)
import json

app = Flask(__name__)

def get_saved_data():
    try:
        data = json.loads(request.cookies.get('secret'))
    except TypeError:
        data = {}
    return data


@app.route('/')
def hello_world():
    return "Hello world!"

@app.route('/sum.html')
def homepage():
    return render_template("sum.html")


@app.route('/data', methods=["GET"])
def data():
    number=request.args.get("number")
    if (number == "") or (number == None):
        return jsonify({"result":"Lack of Parameter"})

    elif number.isdigit() == True and int(number)>0 :
        result=str(int((1+int(number))*int(number)/2))  
        return jsonify({"result": "When number is {}, the sum is {} !!!".format(number,result)})   

    else:
         return jsonify({"result":"Wrong Parameter"})

@app.route('/myName')
def myName():
    return render_template("name.html", saves=get_saved_data())

@app.route('/trackName', methods=['POST'])
def trackName():
    # name=request.args.get("name")
    response= make_response(redirect(url_for('myName')))
    data = get_saved_data()
    data.update(dict(request.form.items()))
    response.set_cookie('secret',json.dumps(data))
    return response


if __name__ == "__main__":
    app.run(debug=True, port=3000, host='localhost')