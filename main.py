from flask import Flask , jsonify, request

app = Flask(__name__)

languages=[{"name":"c++"}, {"name":"python"}, {"name":"js"}]

#get method
@app.route('/',methods=['GET'])
def test():
   return jsonify({"message":"it works"})


@app.route('/lang',methods=['GET'])
def all_lang():
    return jsonify({"languages":languages})


@app.route('/lang/<string:name>', methods=["GET"])
def return_one(name):
    langs=[language for language in languages if language['name']==name]
    return jsonify({"language":langs[0]})


#post method
@app.route('/lang', methods=['POST'])
def addone():
    language= {'name': request.json['name']}
    languages.append(language)
    return jsonify({'languages' : languages})


#put method
@app.route('/lang/<string:name>',methods=['PUT'])
def editone(name):
    langs=[language for language in languages if language['name']==name]
    langs[0]['name']=request.json['name']
    return jsonify({"languages":langs[0]})


#delete method
@app.route('/lang/<string:name>',methods=['DELETE'])
def deleteone(name):
    langs=[language for language in languages if language['name']==name]
    languages.remove(langs[0])
    return jsonify({"languages":languages})    


if __name__ == '__main__':
   app.debug=True 
   app.run()