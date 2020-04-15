from roboter.models import robot


def conversation():
    robot_restaurant = robot.RestaurantRobot()
    robot_restaurant.introduction()
    robot_restaurant.recommended()
    robot_restaurant.favorite_restaurant()
    robot_restaurant.thanks()

