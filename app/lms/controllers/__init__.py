from flask import request, make_response, render_template, url_for, redirect
from sqlalchemy import create_engine
from sqlalchemy import func, and_, or_, not_
from sqlalchemy.orm import sessionmaker
from lms.model import *
import json

from .. import app

db_string = "postgresql://postgres:example@localhost:5432/postgres"
engine = create_engine(db_string)
Session = sessionmaker(bind=engine)
