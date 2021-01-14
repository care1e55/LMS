from flask import Blueprint, request, redirect, url_for, g
from lms.model.auth import Auth
from lms.model.materials import Materials
import logging

from . import Session

material_api = Blueprint('material_api', __name__)

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO)
logger = logging.getLogger(__name__)

@material_api.before_request
def before_request():
    g.token = request.cookies.get('token')
    user_id = Auth.verify_auth_token(str(g.token))
    session = Session()
    g.user = session.query(Auth).filter_by(user_id=user_id).first()
    session.close()
    if g.user is None:
        redirect(url_for('/')) 

# add material
@material_api.route('/material', methods = ['POST'])
def post_material():
    logger.log(logging.INFO, request.form)
    session = Session()
    session.add(Materials(
        **request.form))
    session.commit()
    session.close()
    return 'OK', 200

# modify material
@material_api.route('/material/<material_id>', methods = ['PUT', 'DELETE'])
def modify_material(material_id):
    logger.log(logging.INFO, request.form)
    session = Session()
    if request.method == 'PUT':
        session.query(Materials) \
            .filter(Materials.material_id == material_id) \
            .update(
                **request.form,
                material_id = material_id)
        session.commit()
    elif request.method == 'DELETE':
        session.query(Materials).filter(Materials.material_id == material_id).delete()
        session.commit()
    session.close()
    return 'OK', 200
