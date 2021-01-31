
class CalculationRequest:
    def __init__(self, initialInvestment, discountRate, maxdiscountRate, cashinFlowFixed, numberofYears, *args):
        self._initialInvestment = initialInvestment
        self._discountRate = discountRate
        self._maxdiscountrate = maxdiscountRate
        self._cashinFlow = cashinFlowFixed
        self._numberofYears = numberofYears
        self._cashInFlows = []
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
