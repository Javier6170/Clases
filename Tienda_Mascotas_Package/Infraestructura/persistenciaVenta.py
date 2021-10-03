import jsonpickle


class PersistenciaVenta:
    @classmethod
    def save_json(cls, venta):
        text_open = open("files/" + str(venta.id) + '.json', mode='w')
        json_gui = jsonpickle.encode(venta)
        text_open.write(json_gui)
        text_open.close()

    @classmethod
    def load_json(cls, file_name):
        text_open = open("files/" + file_name, mode='r')
        json_gui = text_open.readline()
        venta = jsonpickle.decode(json_gui)
        text_open.close()
        return venta
