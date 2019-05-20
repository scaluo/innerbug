from datetime import datetime
from functools import wraps
from flask import Blueprint,request,make_response,jsonify,current_app,g
from flask_httpauth import HTTPBasicAuth
from innerbug.extensions import db
from innerbug.models import User,Project,Bug
from flask_cors import CORS
from innerbug.blueprints.errors import api_abort,token_missing,invalid_token
api_bp = Blueprint('api',__name__)
CORS(api_bp)
auth = HTTPBasicAuth()

@auth.verify_password
def verify_password(username_or_token, password=None):
    # first try to authenticate by token
    user = User.verify_auth_token(username_or_token)
    if not user:
        # try to authenticate with username/password
        user = User.query.filter_by(loginname = username_or_token).first()
        if not user or not user.check_password(password):
            return False
    g.user = user
    return True

def get_token():
    # Flask/Werkzeug do not recognize any authentication types
    # other than Basic or Digest, so here we parse the header by hand.
    if 'Authorization' in request.headers:
        try:
            token = request.headers['Authorization']
        except ValueError:
            # The Authorization header is either empty or has no token
            token = None
    else:
        token = None
    return token

def auth_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = get_token()
        print(token)
        # Flask normally handles OPTIONS requests on its own, but in the
        # case it is configured to forward those to the application, we
        # need to ignore authentication headers and let the request through
        # to avoid unwanted interactions with CORS.
        if request.method != 'OPTIONS':
            if token is None:
                return token_missing()
            if not verify_password(token):
                return invalid_token()
        return f(*args, **kwargs)
    return decorated

@api_bp.route('/',methods=['GET'])
def index():
    return jsonify({"version":"1.0"})

@api_bp.route('/login',methods=['POST'])
def login():
    username = request.form.get('loginname')
    password = request.form.get('password')


    user = User.query.filter_by(loginname=username).first()
    if user is None or not user.check_password(password):
        return api_abort(code=400, message='Either the username or password was invalid.')
    else:
        token = user.generate_auth_token()
        response = jsonify({
             "access_token": token,
             "user_name": user.username,
             "isadmin":user.isadmin
         })
        return response;

@api_bp.route('/changepass',methods=['POST'])
@auth_required
def changepass():
    oldpass = request.form.get('oldpassword')
    newpass = request.form.get('newpassword')
    user = g.user
    if not user.check_password(oldpass):
        return api_abort(code=400, message='password is wrong.')
    else:
        user.set_password(newpass)
        db.session.commit()
        return jsonify({"info":"修改密码成功！"})

@api_bp.route('/addproject',methods=['POST'])
@auth_required
def addproject():
    projectname = request.form.get('projectname')
    project = Project(projectname=projectname)
    db.session.add(project)
    db.session.commit()
    return jsonify({"info":"新增项目完成"})

@api_bp.route('/addbug',methods=['POST'])
@auth_required
def addbug():
    title = request.form.get('title')
    level = request.form.get('level')
    prjid = request.form.get('prj')
    content = request.form.get('content')
    bug = Bug(title=title,project_id=prjid,level=level,content=content,user_id=g.user.id)
    db.session.add(bug)
    db.session.commit()
    return jsonify({"info":"新增BUG完成"})


@api_bp.route('/projects')
@auth_required
def getprojects():
    projects = Project.query.all()
    result = []
    for project in projects:
        result.append(project.to_json())
    return jsonify(result)

@api_bp.route('/bugs/<int:prj_id>')
@auth_required
def getbugs(prj_id):
    print(prj_id)
    bugs = Bug.query.filter_by(project_id=prj_id).all()
    result = []
    for bug in bugs:
        result.append(bug.to_json())
    return jsonify(result)

@api_bp.route('/bug/<int:id>')
@auth_required
def getbug(id):
    bug = Bug.query.get(id)
    return jsonify(bug.to_json())

@api_bp.route('/setbugstatus',methods=['POST'])
@auth_required
def setbugstatus():
    id= request.form.get('id')
    status = request.form.get('status')
    bug = Bug.query.get(id)
    bug.status=status
    
    db.session.commit()
    return jsonify({"info":"修改成功"})

@api_bp.route('/updatebug',methods=['POST'])
@auth_required
def updatebug():
    id = request.form.get('id')
    bug = Bug.query.get(id)
    bug.title = request.form.get('title')
    bug.project_id = request.form.get('prj')
    bug.level = request.form.get('level')
    bug.content = request.form.get('content')
    db.session.commit()
    return jsonify({"info":"修改成功"})

@api_bp.route('/delbug',methods=['POST'])
@auth_required
def delbug():
    id = request.form.get('id')
    bug =  Bug.query.get(id)
    db.session.delete(bug)
    db.session.commit()
    return jsonify({'info':'已删除'})

@api_bp.route('/delprj',methods=['POST'])
@auth_required
def delprj():
    id = request.form.get('id')
    bug =  Project.query.get(id)
    db.session.delete(bug)
    db.session.commit()
    return jsonify({'info':'已删除'})

@api_bp.route('/users')
@auth_required
def getusers():
    users = User.query.all()
    result = []
    for user in users:
        result.append(user.to_json())
    return jsonify(result)

@api_bp.route('/deluser',methods=['POST'])
@auth_required
def deluser():
    id = request.form.get('id')
    user =  User.query.get(id)
    db.session.delete(user)
    db.session.commit()
    return jsonify({'info':'已删除'})

@api_bp.route('/adduser',methods=['POST'])
@auth_required
def adduser():
    username = request.form.get('username')
    loginname = request.form.get('loginname')
    password = request.form.get('password')
    isadmin=False
    if request.form.get('isadmin')=='true':
        isadmin=True
    user = User(username=username,loginname=loginname,isadmin=isadmin)
    user.set_password(password)
    db.session.add(user)
    db.session.commit()
    return jsonify({"info":"新增用户完成"})
