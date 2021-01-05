from flask import Flask
app = Flask(__name__)

from lms.controllers import profile, materials, auth, groups, homeworks, solutions, courses
