from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list, hall_number: int, cleaner: str, movie: str):
    peoples = [Customer(customer["name"], customer["food"])
               for customer in customers]
    bar = CinemaBar()
    hall = CinemaHall(hall_number)
    cleaner = Cleaner(cleaner)
    for human in peoples:
        bar.sell_product(human, human.food)
    hall.movie_session(movie, peoples, cleaner)
