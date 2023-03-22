from package import Package
"""
gives acces to class Package
"""

class OverweightPackage(Package):
    """
    Class used to represent OverweightPackage:
    Subclass of Package
    """
    MIN_WEIGHT = 4.0
    """
    :MIN_WEIGHT: minimum weight for an OverweightPackage (example = 4.0)
    :type MIN_WEIGHT: constant
    """
    PRICE_EXT_WEIGHT = 1.0
    """
    :PRICE_EXT_WEIGHT: price for each extra kilogram of the package (example = 1.0)
    :type: PRICE_EXT_WEIGHT: constant
    """

    def __init__(self, id_package: int = 0, weight: float = 0.0, description: str = 'Description'):
        """
        OverweightPackage constructor object.
        :param id_package: id of overweightpackage
        :type id_package: int
        :param weight: weight of overweightpackage
        :type weight: float
        :param description: description of overweightpackage
        :type description: str
        """
        super().__init__(id_package, weight, description)
        """
        gives access to base class Package attributes
        :param id_package: id of package
        :type id_package: int
        :param weight: weight of package
        :type weight: float
        :param description: description of package
        :type description: str
        """
        self._cost = self.calculate(weight)

    def calculate(self, weight : float):
        """ calculates cost of overweightpackage with the overweight fee per kilogram
            :returns: weight * W_GR_100 + extra_weight * PRICE_EXT_WEIGHT
            :rtype: float
        """
        extra_weight: float = self._weight - self.MIN_WEIGHT
        return ((weight * self.W_GR_100) + (extra_weight * self.PRICE_EXT_WEIGHT))
    
    def __str__(self):
        """ returns str of overweightpackage
            :returns: string overweight
            :rtype: str
        """
        return 'id, peso, descripcion, costo =({0}, {1}, {2}, {3})'.format(self._id_package, self._weight, self._description, self._cost)
    