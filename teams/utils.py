from .exceptions import NegativeTitlesError, InvalidYearCupError, ImpossibleTitlesError
from datetime import datetime


def data_processing(data):
    if data["titles"] < 0:
        raise NegativeTitlesError("titles cannot be negative")

    current_year = int(datetime.now().year)

    cups = [year for year in range(1930, current_year, 4)]

    first_cup = int(datetime.strptime(data["first_cup"], "%Y-%m-%d").strftime("%Y"))

    if first_cup not in cups:
        raise InvalidYearCupError("there was no world cup this year")

    appearances = cups.index(cups[-1]) - cups.index(first_cup)

    if data["titles"] > appearances:
        raise ImpossibleTitlesError("impossible to have more titles than disputed cups")
