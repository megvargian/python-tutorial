class MyRouter(object):
	"This is a class that describes the characteristics of a router."

	def __init__(self, routername, model, serialno, ios):
		self.routername = routername
		self.model = model
		self.serialno = serialno
		self.ios = ios

	def print_router(self, manuf_date):
		print("The router name is: ", self.routername)
		print("The router model is: ", self.model)
		print("The serial number of: ", self.serialno)
		print("The ios version is: ", self.ios)
		print("The model and date combined: ", self.model + manuf_date)

router1 = MyRouter("R1", "2500", "1234", "12.4")
router1.print_router("today")
print(type(router1)) 