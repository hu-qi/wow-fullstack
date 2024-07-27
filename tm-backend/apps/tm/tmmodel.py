from flask import Flask,json
from apps.login.beknowmodels import *

appguanguan = Flask(__name__)
appguanguan.config['SQLALCHEMY_DATABASE_URI'] = Config.SQLALCHEMY_DATABASE_URI
appguanguan.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(appguanguan)

def fetch_queses(req):
    testid = req.form.get("pid")
    with appguanguan.test_request_context():
        allquiz = []
        tp = Testpapers.query.filter_by(testpaperid=testid).first()
        rtn = {}
        rtn["testpaper_title"]=tp.testpaper_title
        rtn["testpaper_authorname"]=tp.testpaper_authorname
        rtn["ques_amount"]=tp.ques_amount
        rtn["answers"]=tp.answers
        return rtn
    

def fetchpapers(req):
    paperdata = [
        {'paperid':7,'papertitle':'暑假集训测验'},
        {'paperid':8,'papertitle':'prompt'},
        {'paperid':9,'papertitle':'langchain'},
    ]
    with appguanguan.test_request_context():
        for pp in paperdata:
            tp = Testpapers.query.filter_by(testpaperid=pp['paperid']).first()
            pp["papertitle"]=tp.testpaper_title
            pp["author"]="自塾"
            pp["num"]=tp.ques_amount
    return paperdata