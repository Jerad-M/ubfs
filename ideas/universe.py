from .entity import Entity
from .context import Context
from .spec import Spec
from .galaxy import Galaxy

class Universe(Entity, Context):
	"""Context based entity"""

	# Universes must have
	spec = Spec.UNIVERSE
	allowedChildEntities = [Spec.GALAXY]

	# Universes should handle the following methods a little differently
	def initEntityFromSpec(self, spec, key, path):
		"""Retrieve a new entity of a given child class, based on the spec. Not sure if this method belongs in this class"""
		if (spec == Spec.GALAXY):
			return Galaxy(key, path)

		raise FileNotFoundError("Entity '" + spec.name + "' cannot be found!")

	# Universes should be able to do this, custom-ly
