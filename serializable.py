from abc import ABC, abstractmethod


class Serializable(ABC):

    @abstractmethod
    def save_object(self):
        ...

    @abstractmethod
    def load_object(self):
        ...
