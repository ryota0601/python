import roboter.views.console
from roboter.models import ranking
from collections import defaultdict

DEFAULT_ROBOT_NAME = 'ROBOKO'


class Robot(object):
    def __init__(self, name=DEFAULT_ROBOT_NAME, user_name=''):
        self.name = name
        self.user_name = user_name

    def introduction(self):
        while True:
            url = roboter.views.console.get_template('introduction.txt')
            contents = url.substitute()
            print(contents)
            user_name = input('name : ')
            if user_name:
                self.user_name = user_name.title()
                break


class RestaurantRobot(Robot):
    def __init__(self, name=DEFAULT_ROBOT_NAME, user_name='', restaurant=''):
        super().__init__(name)
        self.user_name = user_name
        self.restaurant = restaurant
        self.csvmodels = ranking.CsvModel()

    def recommended(self):
        must_popular = self.csvmodels.popular()
        will_must_popular = [must_popular]
        if not must_popular:
            return None

        while True:
            url = roboter.views.console.get_template('recommended.txt')
            contents = url.substitute(restaurant=must_popular)
            print(contents)
            judge = input('Yes/No : ')

            if judge == 'Yes':
                self.csvmodels.increment(must_popular)
                break

            elif judge == 'No':
                must_popular = self.csvmodels.popular(not_list=will_must_popular)
                if not must_popular:
                    break
                will_must_popular.append(must_popular)

    def favorite_restaurant(self):
        while True:
            url = roboter.views.console.get_template('restaurant.txt')
            contents = url.substitute(name=self.user_name)
            print(contents)
            restaurant = input('Restaurant : ')

            if restaurant:
                self.restaurant = restaurant.title()
                self.csvmodels.increment(self.restaurant)
                break

    def thanks(self):
        url = roboter.views.console.get_template('thanks.txt')
        contents = url.substitute(name=self.user_name)
        print(contents)

