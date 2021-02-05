from NPVCalculation import NPVCalculation
from IRRCalculation import IRRCalculation

from Calculation_Core.ICalculationFactory import CalculationTypeEnum
from CalculationFactory import CalculationFactory
from Calculation_Core.ICalculationFactory import ROIInputs
from flask import jsonify, request
from CalculationResponse import  CalculationResponse

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

from app import create_app

app = create_app()
@app.route('/')
def home():
   return "Hello Calculation World!"

# Based on Calculation Request
@app.route('/calculation/<calculation_type_id>', methods=['GET','PUT'])
def execute_calculation(calculation_type_id):


    if request.method == 'GET':
        factoryinst = CalculationFactory.getInstance()
        roiInputsUpdated = ROIInputs(10000, .1, .9, 3000, 5)
        npvCalcuator = factoryinst.GetCalculation(CalculationTypeEnum.NPV, roiInputsUpdated)
        npvCalcuator.Execute()
        calculation_response = CalculationResponse(roiInputsUpdated.InitialInvestment,roiInputsUpdated.DiscountRate,
                                                  roiInputsUpdated.MaxDiscountRate,roiInputsUpdated.CashinFlowFixed,
                                                  roiInputsUpdated.NumberOfYears,npvCalcuator.result)
        print("Printing npv calculation value ", npvCalcuator.result)
    else:
        if request.method =='PUT':
            calculation_request = request.get_json()
            factoryinst = CalculationFactory.getInstance()
            roiInputsUpdated = ROIInputs(calculation_request.InitialInvestment
                                         ,calculation_request.DiscountRate ,
                                         calculation_request.MaxDiscountRate,
                                         calculation_request.CashinFlowFixed,
                                         calculation_request.NumberOfYears)
            npvCalcuator = factoryinst.GetCalculation(calculation_type_id, roiInputsUpdated)
            npvCalcuator.Execute()
            print("Printing npv calculation value ", npvCalcuator.result)
            calculation_response = CalculationResponse(roiInputsUpdated.InitialInvestment, roiInputsUpdated.DiscountRate,
                                                   roiInputsUpdated.MaxDiscountRate, roiInputsUpdated.CashinFlowFixed,
                                                   roiInputsUpdated.NumberOfYears, npvCalcuator.result)
    return calculation_response.toJSON()

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')