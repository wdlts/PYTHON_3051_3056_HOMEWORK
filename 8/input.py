from UI import description_view
from UI import first_name_view
from UI import last_name_view
from UI import telephone_view


def confirm():
    return ' '.join([first_name_view(), last_name_view(), telephone_view(), description_view()])+'\n'