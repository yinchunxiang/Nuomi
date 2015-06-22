#!flask/bin/python

from nuomi_dict import app

class CityDict(object):
    def __init__(self):
        self.__id_name_dict = {}
        with app.open_resource('data/nuomi.city') as f:
            lines = f.readlines()
            for line in lines:
                city_id, city_name = line.rstrip().split('\t')
                self.__id_name_dict[city_id] = city_name
                self.__id_name_dict[city_name] = city_id


    def get_value(self, city_key):
        try:
            name = self.__id_name_dict[city_key]
            return name
        except KeyError:
            return 'unknown'

