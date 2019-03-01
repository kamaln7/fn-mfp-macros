from datetime import datetime
import myfitnesspal
import os

with open("/var/openfaas/secrets/password","r") as password:
    client = myfitnesspal.Client(os.environ['USERNAME'], password.read())

def handle(req):
    try:
        day = client.get_date(datetime.now())
        totals = day.totals

        netcarbs = totals['carbohydrates'] - totals['fiber']

        return "{}g net carbs today. {}g total carbs, {}g fiber".format(netcarbs, totals['carbohydrates'], totals['fiber'])
    except Exception as e:
        return "error: {}".format(e.message)
