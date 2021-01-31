import abc
from enum import  Enum
# The Abstract class defined in python for
# handling Calculations. All Calculations need to
# have an Execute method
# Author : Abhilash
# Note: abc is pythons Abstract Base class
class CaculationFactoryInterface(metaclass=abc.ABCMeta):
    @classmethod
    def __init__(self):
        print("Initialized")
        self._result=0


    @abc.abstractmethod
    def GetCalculation(self, calcType, roiInputs):
        """Load in the data set"""
        raise NotImplementedError

class CalculationTypeEnum(Enum):
    NPV=1
    IRR=2
    Other =3

class ROIInputs():
    def __init__(self, initialInvestment,discountRate,maxdiscountRate,cashinFlowFixed,numberofYears,*args):
        self._initialInvestment=initialInvestment
        self._discountRate = discountRate
        self._maxdiscountrate=maxdiscountRate
        self._cashinFlow=cashinFlowFixed
        self._numberofYears=numberofYears
        self._cashInFlows=[]
        for arg in args:
            self._cashInFlows.append(arg)
 # getting the values
    @property
    def InitialInvestment(self):
        print('Getting value')
        return self._initialInvestment

    @property
    def DiscountRate(self):
        print('Getting value')
        return self._discountRate

    @property
    def MaxDiscountRate(self):
        print('Getting value')
        return self._maxdiscountrate

    @property
    def CashinFlowFixed(self):
        print('Getting value')
        return self._cashinFlow

    @property
    def NumberOfYears(self):
        print('Getting value')
        return self._numberofYears

    @property
    def CashInFlows(self):
        print('Getting value')
        return self._cashInFlows




