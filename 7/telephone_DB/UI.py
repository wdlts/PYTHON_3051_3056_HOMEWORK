import data_provider as prov
import data_writer as dw


def first_name_view():
    data = prov.get_first_name()
    dw.first_name_writer(data)
    return data


def last_name_view():
    data = prov.get_last_name()
    dw.last_name_writer(data)
    return data


def telephone_view():
    data = prov.telephone()
    dw.telephone_writer(data)
    return data


def description_view():
    data = prov.description()
    dw.description_writer(data)
    return data
