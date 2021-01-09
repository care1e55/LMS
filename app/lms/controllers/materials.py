from flask import Blueprint, request
from lms.model.materials import Materials
import logging

from . import Session

material_api = Blueprint('material_api', __name__)

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO)
logger = logging.getLogger(__name__)

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
