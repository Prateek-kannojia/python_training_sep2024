class Flight:
    def __init__(self, id, airline)->None:
                #  , source, destination, duration, fare) -> None:
        self.id = id
        self.airline = airline
        # self.source = source
        # self.destination = destination
        # self.duration = duration
        # self.fare = fare

    def __str__(self) -> str:
        return f'{self.id}, {self.airline}'
        # {self.source}, {self.destination}, {self.duration}, {self.fare}'

    def __repr__(self) -> str:
        return self.__str__()