from flask import Blueprint,jsonify,request
import json
mod= Blueprint('user',__name__,url_prefix='/user')
data=json.load(open('first_flask\\data.json','r'))
# with open('first_flask\\data.json','r')as abc:            #another way to open json file
#     data=json.load(abc)
#     print(data)

@mod.route('/',methods=['GET'])

def fetchall():
    # return "<h1>Hello world..!</h1>"
    return jsonify(data)                        #http://127.0.0.1:5000/user


@mod.route('/<user_id>',methods=['GET'])
def show(user_id):
    # print(user_id)
    response=[x for x in data if x['id']==int(user_id)]
    return jsonify((response))
    # response={
    #     "user_id":user_id
    # }
    # return jsonify((response))          #http://127.0.0.1:5000/user/1 or 2

@mod.route('/fetch_user',methods=['GET'])
def fetch_user():
    user_id=request.args.get('user_id')       #import request module
    user_details=[x for x in data if x['id']==int(user_id)]
    user_details=user_details[0] if user_details else{}
    return jsonify((user_details))     #http://127.0.0.1:5000/user/fetch_user?user_id=2


@mod.route('/create_user',methods=['POST'])
def create_user1():
    user_data=request.get_json()
    new_user_id=data[-1]['id']+1
    response=user_data
    response['id']=new_user_id
    data.append(response)
    json.dump(data,open('first_flask\\data.json','w'))
    return "data saved succesfully"

@mod.route('/create_user_form',methods=['POST'])
def create_user2():
    name=request.form.get('name')
    add=request.form.get('add')
    new_user_id=data[-1]['id']+1
    response={
        'id':new_user_id,
        'name':name,
        'add':add
    }
    data.append(response)
    json.dump(data,open('first_flask\\data.json','w'))
    return "data saved succesfully from form"


@mod.route('/update_user/<user_id>/',methods=['PUT'])
def update_user(user_id):
    user_data=request.get_json()
    for d in data:
        if d['id']==int(user_id):
            if 'name'in user_data:
                d['name']=user_data['name']
            if 'add' in user_data:
                d['add']=user_data['add']
    json.dump(data,open('first_flask\\data.json','w'))
    return "user details upload successfully"

@mod.route('/delete/<user_id>/',methods=['DELETE'])
def delete_user(user_id):
    for index,d in enumerate(data):
        if d['id']==int(user_id):
            del data[index]
    json.dump(data,open('first_flask\\data.json','w'))
    return "deleted succesfully"