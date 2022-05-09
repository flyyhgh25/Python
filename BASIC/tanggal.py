from datetime import datetime

# from Challege.project_tugas import kembali
# date_format = "%m/%d/%Y"
# a = datetime.strptime('8/18/2008', date_format)
# b = datetime.strptime('9/26/2008', date_format)
# delta = b - a
# print (delta.days) # that's it
date = datetime.today()
date_pormat = "%d-%m-%Y"
strtr = date.strftime(date_pormat)

print(strtr)
kembali = "15-11-2021"

tdelta = datetime.strptime(kembali,date_pormat)- datetime.strptime(strtr,date_pormat)
print(tdelta)



