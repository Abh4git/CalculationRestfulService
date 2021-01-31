import abc

# The Abstract class defined in python for
# handling Calculations. All Calculations need to
# have an Execute method
# Author : Abhilash
# Note: abc is pythons Abstract Base class
class CaculationInterface(metaclass=abc.ABCMeta):
    @classmethod
    def __init__(self):
        print("Initialized")
        self._result=0

    # getting the values
    @property
    def result(self):
        print('Getting value')
        return self._result

    # setting the values
    @result.setter
    def result(self, value):
        print('Setting value to ' + value)
        self._result = value

    @abc.abstractmethod
    def Execute(self, path: str, file_name: str):
        """Load in the data set"""
        raise NotImplementedError


