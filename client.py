
import quandl

#quandl.ApiConfig.api_version = '2015-04-09'


quandl.ApiConfig.api_key = 'WMmx9zov_EVpG4L91ySF'
#print (quandl.get('TC1/SUNPHARMA', start_date='2018-08-20', end_date='2018-08-27'))

print(quandl.get('TC1/SUNPHARMA', start_date='2018-08-28', end_date='2018-08-28'))
