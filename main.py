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
		n = len(self.investments)
		for i in range(n):
			if self.investments[i][0] == name and self.investments[i][1] == amount and self.investments[i][2] == date:
				self.investments.remove(self.investments[i])

	def totalInvestedPer(self, indexName):
		investment = 0
		n = len(self.investments)
		for i in range(n):
			if self.investments[i][0] == indexName:
				investment += self.investments[i][1]
		return investment

	def printInvestment(self, indexName):
		investment = self.totalInvestedPer(Investment, indexName)
		print("Total invested into", indexName, "is", investment)

	def checkInvestmentPer(self, indexName, currentPrice):
		investment = self.totalInvestedPer(Investment, indexName)
		diff = currentPrice - investment
		if diff > 0:
			percentageDiff = diff / investment * 100
			print("Investment Is Positive, Has increased by", percentageDiff, "%")
		elif diff == 0:
			print("Investment hasnt changed")
		else:
			percentageDiff = (investment - currentPrice) / investment * 100
			print("Investment Is Negative, Has decreased by", percentageDiff, "%")


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
Investment.printInvestment(Investment, "S&P500")
Investment.checkInvestmentPer(Investment, "S&P500", 50)
