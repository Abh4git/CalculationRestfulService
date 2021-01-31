import numpy
from Calculation_Core.CalculationInterface import CaculationInterface

# Class Responsible for NPV Calculation
# Takes the parameters of InitialInvestment,
# DiscountRate, CashInFlow, Number of Years
class IRRCalculation(CaculationInterface):


    def __init__(self, initialInvestment,discountRate,maxdiscountRate,cashInflow,numberofyears, cashFlowsList):
        self._initalInvestment = initialInvestment
        self._discountRate = discountRate
        self._cashInflow = cashInflow
        self._numberofyears = numberofyears
        self._maxdiscountRate = maxdiscountRate
        self._cashFlowList=[]
        #for arg in args:
        self._cashFlowList=cashFlowsList
        self._result = 0

    #def __init__(self,initialInvestment,discountRate,cashInflow,numberofyears):
    #    self._initalInvestment=initialInvestment
    #   self._discountRate = discountRate
    #    self._cashInflow = cashInflow
    #   self._numberofyears = numberofyears
    #   self._result=0

# Properties to get result
    @property
    def result(self):
        print('Getting value')
        return self._result

#Property setter for result
    @result.setter
    def result(self, value):
        print('Setting value to ' ,value)
        self._result = value

        # floating point range


    # Execute method. Calculation is done in this method
    def Execute(self):
        npv = 1;
        discountRate = 0;
        for i in numpy.arange(self._discountRate, self._maxdiscountRate,.1) :
            npv = self.CalculateNPV(i)
            if (npv <= 0):
                discountRate = i
                break;
        self.result=discountRate
        return True

    def CalculateNPV(self, discountRate):
        npv = 0
        nominator = self._cashInflow
        denominator = 1
        resultInital = 0
        for i in range(1, self._numberofyears + 1):
            if (len(self._cashFlowList) > 0):
                nominator = self._cashFlowList[i]
            denominator = pow((1 + discountRate), i)
            resultInital += nominator / denominator
            #print(resultInital)
        npv = resultInital - self._initalInvestment
        return npv


#registering  this as attached to CalculationInterface
# abstract class.
CaculationInterface.register(IRRCalculation)
