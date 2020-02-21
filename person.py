class Person:
	def __init__(self, name, addr, is_driver=False, mpg=None, passengers=None, seats=None):
		self.name = name
		self.addr = addr
		self.is_driver = is_driver
		self.mpg = mpg
		self.passengers = passengers
		self.seats = seats
		self.curr_pos = addr

	def __str__(self):
		return str(self.name) + ',' +\
		str(self.addr) + ',' +\
		str(self.is_driver) + ',' +\
		str(self.seats) + ',' +\
		str(self.mpg)
	def __repr__(self):
		return str({'name':self.name,\
		'addr':self.addr,\
		'is_driver':self.is_driver,\
		'seats':self.seats,\
		'mpg':self.mpg,\
		'passengers':self.passengers})
	
	# def is_driver():
	# 	return self.is_driver
	def open_seats():
		return seats - passengers

	def has_open_seats():
		return open_seats() > 0