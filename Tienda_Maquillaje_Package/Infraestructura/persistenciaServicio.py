import pickle
import jsonpickle


class PersistenciaServicio():
    @classmethod
    def save(cls, servicio):
        binary_open = open("files/" + str(servicio.id) + '.gui', mode='wb')
        pickle.dump(servicio, binary_open)
        binary_open.close()

    @classmethod
    def load(cls, file_name):
        binary_open = open("files/" + file_name, mode='rb')
        servicio = pickle.load(binary_open)
        binary_open.close()
        return servicio

    @classmethod
    def save_json(cls, servicio):
        text_open = open("files/" + str(servicio.id) + '.json', mode='w')
        json_gui = jsonpickle.encode(servicio)
        text_open.write(json_gui)
        text_open.close()

    @classmethod
    def load_json(cls, file_name):
        text_open = open("files/" + file_name, mode='r')
        json_gui = text_open.readline()
        servicio = jsonpickle.decode(json_gui)
        text_open.close()
        return servicio
