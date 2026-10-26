import csv

depIdx = 1
withIdx = 2
totalIdx = 3

#Edit contents to what is needed!
grocery = ["tesco", "sainsburys", "asda"]
transport = ["uber", "trainline", "shell"]
entertainment = ["netflix", "spotify", "steam", "cineworld"]
uncategorised = ["job"]

def analyzeExpenses(fileName):
	# Initialize dictionary to hold totals for each sector:
	sectorTotals = [
		["Grocery", 0.0, 0.0, 0.0],
		["Transport", 0.0, 0.0, 0.0],
		["Entertainment", 0.0, 0.0, 0.0],
		["Uncategorized", 0.0, 0.0, 0.0],
	]

	totalDeposits = 0.0
	totalWithdraw = 0.0

	try:
		with open(fileName,'r') as file:
			csvReader = csv.DictReader(file)

			for row in csvReader:
				# Convert string values to floats for calculation:
				withdraw = float(row['Withdrawal'])
				deposit = float(row['Deposit'])
				description = row['Description'].lower()

				# Track overall cash flow:
				totalWithdraw += withdraw
				totalDeposits += deposit

				# Categorize spending based on keywords in description:
				if any(item in description for item in grocery):
					sectorTotals[0][depIdx] += deposit
					sectorTotals[0][withIdx] += withdraw
					sectorTotals[0][totalIdx] += deposit - withdraw

				elif any(item in description for item in transport):
					sectorTotals[1][depIdx] += deposit
					sectorTotals[1][withIdx] += withdraw
					sectorTotals[1][totalIdx] += deposit - withdraw

				elif any(item in description for item in entertainment):
					sectorTotals[2][depIdx] += deposit
					sectorTotals[2][withIdx] += withdraw
					sectorTotals[2][totalIdx] += deposit - withdraw

				elif any(item in description for item in uncategorised):
					sectorTotals[3][depIdx] += deposit
					sectorTotals[3][withIdx] += withdraw
					sectorTotals[3][totalIdx] += deposit - withdraw


		# Calculate final net savings:
		netSavings = totalDeposits - totalWithdraw

		print("=== NET SAVINGS BY SECTOR ===")
		for sector, dep, wit, total in sectorTotals:
			print(f"{sector}: \n    · Deposit: £{dep:.2f} \n    · Withdraw: £{wit:.2f}\n    · Total: £{total:.2f}\n")

		print("---\n")

		# Print the financial summary report:
		print("=== FINANCIAL SUMMARY REPORT ===")
		print(f"Total Deposits:    £{totalDeposits:.2f}")
		print(f"Total Withdrawals: £{totalWithdraw:.2f}")
		print(f"Net Savings:       £{netSavings:.2f}\n")

	except FileNotFoundError:
		print(f"Error: The file '{fileName}' was not found. Please ensure it is in the same directory.")

# Run the analysis on your data file:
inputFileName = input("Enter the exact name of the csv file (e.g: Data.csv):\n")

#temporary script:
if inputFileName == "":
	inputFileName = 'Data.csv'

print()
analyzeExpenses(inputFileName)
