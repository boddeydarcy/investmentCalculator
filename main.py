class Investment:
	investments = []

	def __init__(self, name, amount, date):
		investment = [name, amount, date]
		self.investments.append(investment)

	def getIndexInvesments(self, indexName):
		tempInvestments = []
		n = len(self.investments)
		for i in range(n):
			if self.investments[i][0] == indexName:
				tempInvestments.append(self.investments[i])
		return tempInvestments

	def removeInvestments(self, name, amount, date):
		investment = [name, amount, date]
		self.investments.append(investment)

	def totalInvestedPer(self, indexName):
		investment = 0
		n = len(self.investments)
		for i in range(n):
			if self.investments[i][0] == indexName:
				investment += self.investments[i][1]
		print("Total invested into", indexName, "is", investment)

	def totalInvested(self):
		investment = 0
		n = len(self.investments)
		for i in range(n):
			investment += self.investments[i][1]
		print("Total Invested:", investment)

	def returnInvestments(self):
		return self.investments


Investment("S&P500", 75, "22/11/24")
Investment("S&P500", 50, "22/11/24")
Investment("Bitcoin", 100, "22/11/24")
Investment.removeInvestments(Investment,"S&P500", -50, "22/11/24")
print(Investment.returnInvestments(Investment))
print(Investment.getIndexInvesments(Investment, "S&P500"))
Investment.totalInvested(Investment)
Investment.totalInvestedPer(Investment, "S&P500")
