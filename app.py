from flask import Flask
# importing os module 
import shutil

path = '/tmp/f.txt'
shutil.chown(path, user=None, group=None)

app = Flask(__name__)



@app.route("/")
def hello():
	html = "<h3>Hello !</h3>"
	return html
	
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
