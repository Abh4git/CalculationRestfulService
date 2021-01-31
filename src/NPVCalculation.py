from Calculation_Core.CalculationInterface import CaculationInterface

# Class Responsible for NPV Calculation
# Takes the parameters of InitialInvestment,
# DiscountRate, CashInFlow, Number of Years
class NPVCalculation(CaculationInterface):

    def __init__(self,initialInvestment,discountRate,cashInflow,numberofyears, cashFlowsList):
        self._initalInvestment=initialInvestment
        self._discountRate = discountRate
        self._cashInflow = cashInflow
        self._numberofyears = numberofyears
        self._cashFlowList = []
        # for arg in args:

        self._cashFlowList=cashFlowsList

        self._result=0

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
# Execute method. Calculation is done in this method
    def Execute(self):
        npv = 0
        nominator = self._cashInflow
        denominator = 1
        resultInital = 0
        for i in range  (1,self._numberofyears+1):
            denominator = pow((1 + self._discountRate), i)
            resultInital += nominator / denominator
#            print (resultInital)
        npv = resultInital - self._initalInvestment
        self.result=npv
        return True

#registering  this as attached to CalculationInterface
# abstract class.
CaculationInterface.register(NPVCalculation)
