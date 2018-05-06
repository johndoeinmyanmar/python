# OOP design for vector calcultion 
class Vector:
	"""Represent a vector in multidiemnsional space."""

	def __init__(self, d):
		"""Create d-dimensional vector of zeros."""
		self._coords = [0] * d

	def __len__(self):
		"""Return the dimension of the vector."""
		return len(self._coords)

	def __getitem__(self, j):
		"""Return the jth coordinate of the vector."""
		return self._coords[j]

	def __setitem__(self, j, val):
		"""Set jth coordinate of vector to given value."""
		self._coords[j] = val

	def __add__(self, other):
		"""Return the sum of two vectors."""
		if len(self) != len(other):
			raise ValueError('dimension must agree.')
		result = Vector(len(self))
		for j in range(len(self)):
			result[j] = self[j] + other[j]
		return result
	
	def __eq__(self, other):
		"""Return Ture if vector has same coordinate as other."""
		return self._coords == other._coords

	def __ne__(self, other):
		"""Return True if vector differ from other."""
		return not self == other	# rely on existing __eq__ def

	def __str__(self):
		"""Process string representation of vector."""
		return '<' + str(self._coords)[1:-1] + '>'
