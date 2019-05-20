import os
import click
from flask import Flask
from innerbug.extensions import db
from innerbug.settings import config
from innerbug.blueprints.api import api_bp
from innerbug.models import User

def create_app(config_name=None):
    app = Flask('innerbug')
    if config_name == None:
        config_name = os.getenv('FLASK_CONFIG','development')
    app.config.from_object(config[config_name])
    register_extensions(app)
    register_blueprints(app)
    register_commands(app)
    register_shell_context(app)
    return app

def register_extensions(app):
    db.init_app(app)
    

def register_blueprints(app):
    app.register_blueprint(api_bp,url_prefix='/api')
    
def register_shell_context(app):
    @app.shell_context_processor
    def make_shell_context():
        return dict(db=db)

def register_commands(app):
    @app.cli.command()
    def test():
        click.echo('This is a test')

    @app.cli.command()
    @click.option('--drop',is_flag=True,help='Create after drop')
    def initdb(drop):
        if drop:
            click.confirm('确认是否删掉原来的表',abort=True)
            db.drop_all()
            click.echo('成功删除表')
        db.create_all()
        click.echo('创建所有表')
        admin = User(
                    loginname='admin',
                    username='管理员',
                    isadmin=True
                    )
        admin.set_password('admin')
        db.session.add(admin)
        db.session.commit()
        click.echo('添加人员成功')