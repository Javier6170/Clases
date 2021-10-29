import falcon
from falcon import API
import waitress
from Tienda_Mascotas_Package.Infraestructura.persistenciaMascota import PersistenciaMascota
import json


class HolaMundo():

    def on_get(self, req, resp, uuid):
        db = PersistenciaMascota()
        gui = db.load_json(uuid + '.json')
        mensajes = ['Hola Mindo', 'Hola Que hace', 'Adio', 'Ciao', '2+2=4']
        resp.body = json.dumps(gui.__dict__)
        resp.status = falcon.HTTP_OK


def iniciar() -> API:
    # run:app -b 0.0.0.0:2020 --workers 1 -t 240
    api = API()
    api.add_route("/mascota/{uuid}", HolaMundo())

    return api


app = iniciar()

if __name__ == "__main__":
    waitress.serve(app, port=8080, url_scheme="http")
