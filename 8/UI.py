import get_data as prov
import write_data as dw


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


def request_view():
    word = prov.get_request()
    return word
