from Calculation_Core.ICalculationFactory import CalculationTypeEnum
from NPVCalculation import NPVCalculation
from IRRCalculation import IRRCalculation
from Calculation_Core.ICalculationFactory import CaculationFactoryInterface

class CalculationFactory(CaculationFactoryInterface):
    __instance = None

    @staticmethod
    def getInstance():
        """ Static access method. """
        if CalculationFactory.__instance == None:
            CalculationFactory()
        return CalculationFactory.__instance

    def __init__(self):
        """ Virtually private constructor. """
        if CalculationFactory.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            CalculationFactory.__instance = self
        self._result = 0

    def GetCalculation(self,calcType,iroiInputs):
        if (calcType==CalculationTypeEnum.NPV):
            self._calculation=NPVCalculation(iroiInputs.InitialInvestment,iroiInputs.DiscountRate,
                                             iroiInputs.CashinFlowFixed, iroiInputs.NumberOfYears,iroiInputs.CashInFlows)
        elif(calcType==CalculationTypeEnum.IRR):
            self._calculation = IRRCalculation(iroiInputs.InitialInvestment,iroiInputs.DiscountRate,iroiInputs.MaxDiscountRate,
                                             iroiInputs.CashinFlowFixed, iroiInputs.NumberOfYears, iroiInputs.CashInFlows)
        else:
            raise NotImplementedError
        return self._calculation








#Registering factory interface
CaculationFactoryInterface.register(CalculationFactory)
