from flask import Flask, render_template, jsonify, request
from pymongo import MongoClient
from datetime import datetime

client = MongoClient('mongodb+srv://test:sparta@cluster0.ex5d4.mongodb.net/?retryWrites=true&w=majority')
db = client.dbsparta

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/diary', methods=['GET'])
def show_diary():
    articles = list(db.diary.find({},{'_id':False}))
    return jsonify({'articles': articles})

@app.route('/diary', methods=['POST'])
def save_diary():
    title_receive = request.form["title_give"]
    content_receive = request.form["content_give"]

    today = datetime.now()
    mytime = today.strftime('%d-%m-%Y %H-%M-%S')

    file = request.files["file_give"]
    extension = file.filename.split('.')[-1]
    filename = f'static/post-{mytime}.{extension}'
    file.save(filename)

    profile = request.files["profile_give"]
    extension = profile.filename.split('.')[-1]
    profilename = f'static/profile-{mytime}.{extension}'
    profile.save(profilename)

    post_time = 

    doc = {
        'file':filename,
        'profile':profilename,
        'title':title_receive,
        'content':content_receive
    }
    db.diary.insert_one(doc)
    

    return jsonify({'msg':'Upload selesai'})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
