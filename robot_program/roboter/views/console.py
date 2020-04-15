import string

DEFAULT_URL = '/Users/koseryouta/PycharmProjects/robot_program/roboter/templates/'


def get_template(url_name):
    url_name = url_name
    with open(DEFAULT_URL + '/' + url_name) as url:
        url_read = string.Template(url.read())

    return url_read


