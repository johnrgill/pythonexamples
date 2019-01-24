#!/usr/local/bin/python3
from datetime import datetime
varDate = input("please enter a date with format YYYY-MM-DD")
varDate = datetime.strptime(varDate, '%Y-%m-%d')
dateToCheck = "2018-06-30"
dateToCheck = datetime.strptime(dateToCheck, "%Y-%m-%d")
diff = dateToCheck - varDate
print(diff)
