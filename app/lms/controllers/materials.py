from . import *

# add material
@app.route('/material', methods = ['POST'])
def post_material():
    session = Session()
    session.add(Materials(
        **request.form))
    session.commit()
    return 'OK', 200
    session.close()

# modify material
@app.route('/material/<material_id>', methods = ['PUT', 'DELETE'])
def modify_material(material_id):
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
    return 'OK', 200
    session.close()
