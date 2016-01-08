import json


fname = 'dummy_data2.json'



with open(fname, 'r') as f:
	
	for line in f:
		tweet = json.loads(line)
		
		
		
		if tweet['coordinates']:
			#newobj = tweet['coordinates']
			
			print(tweet['coordinates']['coordinates'])