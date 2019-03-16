from MySQL_Class import Mysqldata

obj = Mysqldata()

opt = int(input('1.City\n2.country\n3.Country Languages\nWhich table needed?'))

obj.fetch(opt)
