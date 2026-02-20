class FilterModule(object):
	def filters(self):
		return { 'to_uppercase' : self.to_uppercase }

	def to_uppercase(self, value):
		return value.upper()

