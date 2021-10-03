import pickle
import jsonpickle


class PersistenciaProducto():
    @classmethod
    def save(cls, producto):
        binary_open = open("files/" + str(producto.id) + '.gui', mode='wb')
        pickle.dump(producto, binary_open)
        binary_open.close()

    @classmethod
    def load(cls, file_name):
        binary_open = open("files/" + file_name, mode='rb')
        producto = pickle.load(binary_open)
        binary_open.close()
        return producto

    @classmethod
    def save_json(cls, producto):
        text_open = open("files/" + str(producto.id) + '.json', mode='w')
        json_gui = jsonpickle.encode(producto)
        text_open.write(json_gui)
        text_open.close()

    @classmethod
    def load_json(cls, file_name):
        text_open = open("files/" + file_name, mode='r')
        json_gui = text_open.readline()
        producto = jsonpickle.decode(json_gui)
        text_open.close()
        return producto