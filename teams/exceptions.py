class NegativeTitlesError(Exception):
    default_message = "titles cannot be negative"

    def __init__(self, message) -> None:
        self.message = message or self.default_message


class InvalidYearCupError(Exception):
    default_message = "there was no world cup this year"

    def __init__(self, message) -> None:
        self.message = message or self.default_message


class ImpossibleTitlesError(Exception):
    default_message = "impossible to have more titles than disputed cups"

    def __init__(self, message) -> None:
        self.message = message or self.default_message
