from flask import Flask
from lms.controllers.groups import groups_api
from lms.controllers.profile import profile_api
from lms.controllers.materials import material_api
from lms.controllers.homeworks import homework_api
from lms.controllers.solutions import solution_api
from lms.controllers.auth import auth_api, auth_get
from lms.controllers.courses import courses_api

app = Flask(__name__)
app.register_blueprint(groups_api)
app.register_blueprint(profile_api)
app.register_blueprint(material_api)
app.register_blueprint(courses_api)
app.register_blueprint(auth_api)
app.register_blueprint(homework_api)
app.register_blueprint(solution_api)
app.register_blueprint(auth_get)