from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
import os


# TODO: 封装flask构造方法
class Application(Flask):

    def __init__(self, import_name, template_folder=None, static_folder=None, root_path=None):
        super(Application, self).__init__(import_name, template_folder=template_folder, static_folder=static_folder,
                                          root_path=root_path)
        self.config.from_pyfile('config/base_setting.py')
        if 'ops_config' in os.environ:
            self.config.from_pyfile('config/%s_setting.py' % os.environ['ops_config'])

        db.init_app(self)


db = SQLAlchemy()
app = Application(__name__, template_folder=os.getcwd()+'/web/templates', root_path=os.getcwd())
manager = Manager(app)


from common.libs.UrlManager import UrlManager
app.add_template_global(UrlManager.buildStaticUrl, 'buildStaticUrl')
app.add_template_global(UrlManager.buildUrl, 'buildUrl')

