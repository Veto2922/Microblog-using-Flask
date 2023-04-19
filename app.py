import datetime
from flask import Flask , render_template ,request
from pymongo import MongoClient



app = Flask(__name__)
client = MongoClient('') #but your mongo atlas link here
app.db = client.microblog

# entries = []

@app.route('/', methods = ['GET' , 'POST'])
def home():
    # print(app.db.entries.find({}))
    if request.method == 'POST':
        entry_content = request.form.get('content')
        date = datetime.datetime.today().strftime('%Y-%m-%d')
        # entries.append((entry_content , date))
        app.db.entries.insert_one({'content': entry_content , 'date':date})
    entry_date = [
        
            (
                entry['content'],
                entry['date'],
                datetime.datetime.strptime( entry['date'] ,'%Y-%m-%d').strftime('%b %d')
                
            )
            for entry in app.db.entries.find({})
    ]




    return render_template('home.html' , entries = entry_date)

if __name__ == "__main__":
    app.run(debug=True)
