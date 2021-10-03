import jsonpickle


class PersistenciaEstado:
    @classmethod
    def save_json(cls, estado):
        text_open = open("files/" + 'estado' + '.json', mode='w')
        json_gui = jsonpickle.encode(estado)
        text_open.write(json_gui)
        text_open.close()

    @classmethod
    def load_json(cls, file_name):
        text_open = open("files/" + file_name, mode='r')
        json_gui = text_open.readline()
        estado = jsonpickle.decode(json_gui)
        text_open.close()
        return estado
