import pandas as pd
import argparse

plants = pd.DataFrame({'Name': ['Calathea', 'Palm'], 
	                   'Price': [28.95, 34.95],
	                   'Height': [70., 85.] })

def main():

	parser = argparse.ArgumentParser()

	parser.add_argument('--show-prices', '-p', dest='prices', 
		                 action='store_true', default=False,
		                 help='Show the plants prices')

	parser.add_argument('--show-height', '-e', action='store_true', 
		                 dest='height', default=False,
		                 help='Show the plants heigths.')    
	
	args = parser.parse_args()

	cols = ['Name']

	if args.prices:
		cols += ['Price']

	if args.height:
		cols += ['Height']


	print('Here are your plants: ')
	print(plants[cols])



