# This is my views.py file
from django.shortcuts import render

def home(request):
	import json
	import requests


	if request.method == "POST":
		zipcode = request.POST['zipcode']

		api_requests = requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=" + zipcode + "&distance=0&API_KEY=24A17575-242A-4FF8-88C7-3F81596D8B7F")

		try:
			api = json.loads(api_requests.content)
		except Exception as e:
			api = "Error..."

		if api[1]['Category']['Name'] == "Good":
			category_description = "(0-50): Air quality is satisfactory, and air pollution poses little or no risk."
			category_color = "good"
		elif api[1]['Category']['Name'] == "Moderate":
			category_description = "(51-100): Air quality is acceptable. However, there may be a risk for some people, particularly those who are unusually sensitive to air pollution."
			category_color = "moderate"
		elif api[1]['Category']['Name'] == "Unhealthy for Sensitive Groups":
			category_description = "(101-150): Members of sensitive groups may experience health effects. The general public is less likely to be affected."
			category_color = "usg"
		elif api[1]['Category']['Name'] == "Unhealthy":
			category_description = "(151-200): Some members of the general public may experience health effects; members of sensitive groups may experience more serious health effects."
			category_color = "unhealthy"
		elif api[1]['Category']['Name'] == "Very Unhealthy":
			category_description = "(201-300): Health alert: The risk of health effects is increased for everyone."
			category_color = "veryunhealthy"
		elif api[1]['Category']['Name'] == "Hazardous":
			category_description = "(301-500): Health warning of emergency conditions: everyone is more likely to be affected."
			category_color = "hazardous"
		return render(request, 'home.html', {'api': api,
			'category_description': category_description,
			'category_color': category_color})

	else:
		api_requests = requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=89129&distance=0&API_KEY=24A17575-242A-4FF8-88C7-3F81596D8B7F")

		try:
			api = json.loads(api_requests.content)
		except Exception as e:
			api = "Error..."

		if api[1]['Category']['Name'] == "Good":
			category_description = "(0-50): Air quality is satisfactory, and air pollution poses little or no risk."
			category_color = "good"
		elif api[1]['Category']['Name'] == "Moderate":
			category_description = "(51-100): Air quality is acceptable. However, there may be a risk for some people, particularly those who are unusually sensitive to air pollution."
			category_color = "moderate"
		elif api[1]['Category']['Name'] == "Unhealthy for Sensitive Groups":
			category_description = "(101-150): Members of sensitive groups may experience health effects. The general public is less likely to be affected."
			category_color = "usg"
		elif api[1]['Category']['Name'] == "Unhealthy":
			category_description = "(151-200): Some members of the general public may experience health effects; members of sensitive groups may experience more serious health effects."
			category_color = "unhealthy"
		elif api[1]['Category']['Name'] == "Very Unhealthy":
			category_description = "(201-300): Health alert: The risk of health effects is increased for everyone."
			category_color = "veryunhealthy"
		elif api[1]['Category']['Name'] == "Hazardous":
			category_description = "(301-500): Health warning of emergency conditions: everyone is more likely to be affected."
			category_color = "hazardous"
		return render(request, 'home.html', {'api': api,
			'category_description': category_description,
			'category_color': category_color})


def about(request):
	return render(request, 'about.html', {})



