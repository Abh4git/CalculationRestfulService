from NPVCalculation import NPVCalculation
from IRRCalculation import IRRCalculation

from Calculation_Core.ICalculationFactory import CalculationTypeEnum
from CalculationFactory import CalculationFactory
from Calculation_Core.ICalculationFactory import ROIInputs
print("Hello Calculation World")
print("-----------------------")
# Instantiating the NPVCalculation class with
# values for initialInvestment, Discount Rate, CashInFlow
# and Number of Years. Then the Execute method call
# initiates execution and result is found in ,result.
cashFlows=[]
npvcalc = NPVCalculation(10000,.1,3000,5,cashFlows)
npvcalc.Execute()
print ("Printing calculation value ", npvcalc.result)

irrcalc = IRRCalculation(10000,.1,.9,3000,5,cashFlows)
irrcalc.Execute()
print ("Printing calculation value ", irrcalc.result)

roiInputs= ROIInputs(10000,.1,.9,3000,5)
Factory = CalculationFactory.getInstance()
npvCalcFact=Factory.GetCalculation(CalculationTypeEnum.NPV,roiInputs)
npvCalcFact.Execute()
print ("Printing npv calculation value ", npvCalcFact.result)

