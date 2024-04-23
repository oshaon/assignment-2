import csv
import searchconsole
import os,dotenv
dotenv.load_dotenv()
MY_SITE = os.getenv('MY_SITE')

account = searchconsole.authenticate(client_config='client_secrets.json')
webproperty = account[MY_SITE]
report = webproperty.query.range('today', days=-7).dimension('query').get()
print(report.rows)

list = report.rows

file = open("data list.csv", "a+", newline='',encoding="utf-8")
write = csv.writer(file)
write.writerows(list)
file.close()