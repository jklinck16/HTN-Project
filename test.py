import json
import requests

output = ('https://onesimpleapi.com/api/readability?'
          'token=3wEsSs9EGcHNyjHv2A5qEPnB6jcxbQdoVOsj3hDC&'
          'output=json&'
          'text=The first no-code API designed to save time, money and stress! A toolbox with all the things you need to get your no-code project to success: PDF generation, Currency Exchange, QR codes, Screenshots, and more.'
          )

response = requests.get(output)
print(response.json())
