from flask import Flask
# importing os module 
import os

app = Flask(__name__)

# Change the owner id and 
# the group id of the file
# using os.chown() method
uid = 2000
gid = 2000
os.chown(path, uid, gid)

@app.route("/")
def hello():
	html = "<h3>Hello !</h3>"
	return html
	
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
