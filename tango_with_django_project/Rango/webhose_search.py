import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','tango_with_django_project.settings')

import django
django.setup()

import json
import urllib.parse # Py3
import urllib.request # Py3

def read_webhose_key():
	webhose_api_key = None 
	try:
		with open('search.key','r') as f:
			webhose_api_key = f.readline().strip()

	except :
		raise IOError('search.key file not found')

	return webhose_api_key

def run_query(search_terms , size = 10):

	webhose_api_key = read_webhose_key()
	if not webhose_api_key :
		raise KeyError('Key not found')

	root_url = 'http://webhose.io/search'

	# Format the query string - escape special characters.
	query_string = urllib.parse.quote(search_terms) # Py3

	# Use string formatting to construct the complete API URL.
	# search_url is a string split over multiple lines.
	search_url = ('{root_url}?token={key}&format=json&q={query}'
					'&sort=relevancy&size={size}').format(
					root_url=root_url,
					key=webhose_api_key,
					query=query_string,
					size=size)
							

	results = []

	try :
		response = urllib.request.urlopen(search_url).read().decode('utf-8')
		json_response= json.loads(response)
		
		for post in json_response['posts']:
			results.append({
				'title' : post['title'],
				'link' : post['url'],
				'summary' : post['text'][:200],
				})

	except:
		print("error when querying the webhose api")
	
	return results
	
