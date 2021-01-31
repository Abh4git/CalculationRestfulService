import unittest
import sys
import os
file_dir = os.path.dirname(__file__)
sys.path.append(file_dir)
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import os, sys; sys.path.append(os.path.dirname(os.path.realpath(__file__)))
#print('\n'.join(sys.path))
#sys.path.append("../src/Calculation_Core")

from Calculation_Core.ICalculationFactory import CalculationTypeEnum
from CalculationFactory import CalculationFactory
from Calculation_Core.ICalculationFactory import ROIInputs


sys.path.append("./src")



class CalculationTests(unittest.TestCase):
    def test_NPVCalculation(self):

        roiInputs = ROIInputs(10000, .1, .9, 3000, 5)
        Factory = CalculationFactory.getInstance()
        npvCalcFact = Factory.GetCalculation(CalculationTypeEnum.NPV, roiInputs)
        npvCalcFact.Execute()
        self.assertEqual(1372.36,round(npvCalcFact.result,2))

    def test_IRRCalculation(self):
        initialInvst = 500000
        discountRate = 0.1
        maxdiscountRate = .9
        yearlyCashFlows =[]
        yearlyCashFlows.append(160000)
        yearlyCashFlows.append(160000)
        yearlyCashFlows.append(160000)
        yearlyCashFlows.append(160000)
        yearlyCashFlows.append(50000)

        roiInputs = ROIInputs(10000, .1, .9, 3000, 5)
        Factory = CalculationFactory.getInstance()
        irrCalc = Factory.GetCalculation(CalculationTypeEnum.IRR, roiInputs)
        irrCalc.Execute()
        self.assertEqual(.2,irrCalc.result)


if __name__ == '__main__':
    unittest.main()
