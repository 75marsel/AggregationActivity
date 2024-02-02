from abc import ABCMeta, abstractmethod


class IProtoType(metaclass=ABCMeta):
    
    @staticmethod
    @abstractmethod
    def clone():
        """clone"""