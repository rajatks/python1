from flask import Flask,jsonify,request;

app=Flask(__name__);

@app.route("/", methods=['GET'])
def hello():
    return jsonify({"Greeeting":"hello world"});

@app.route("/", methods=['POST'])
def abc():
    return jsonify({"Finish":"Good world"});

@app.route("/abc/", methods=['GET','POST'])
def xyz():
    if(request.method=='GET'):
        return jsonify({"hello Using ":"Good Morning"});
    if(request.method=='POST'):
        return jsonify({"Post Using ":"Good BYE"});

@app.route("/cube/abc/xyz/<int:num>",methods=['GET'])       
def cube(num):
    return jsonify({'result':num*num*num});

if __name__=='__main__':
    app.run(debug=True);


