from package import Package
"""
gives access to class Package
"""
class StandardPackage(Package):
    """
    Class used to represent StandardPackage:
    Subclass of Package
    """
    FEE = 2.0
    """
    :FEE: setted fee for a standardpackage (example = 2.0)
    :type FEE: constant 
    """
    def __init__(self, id_package: int = 0, weight: float = 0.0, description: str = 'Description'):
        """
        StandardPackage constructor object.
        :param id_package: id of standardPackage
        :type id_package: int
        :param weight: weight of standardPackage
        :type weight: float
        :param description: description of standardPackage
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
        """ calculates cost of the standardpackage with the setted fee
            :returns: weight * W_GR_100 + FEE
            :rtype: float
        """
        return ((weight * self.W_GR_100) + self.FEE)
    
    def __str__(self):
        """ returns str of standardpackage
            :returns: string standardpackage
            :rtype: str
        """
        return 'id, peso, descripcion, costo = ({0}, {1}, {2}, {3})'.format(self._id_package, self._weight, self._description, self._cost)
