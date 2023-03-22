class Package(object):
    """
    Class used to represent a Package
    """

    W_GR_100 = 1.0
    """
    :W_GR_100: cost of 100 grams of any package
    :type W_GR_100: constant
    """

    #Constructor
    def __init__(self, id_package: int = 0, weight: float = 0.0, description: str = 'Description'):
        """
        Package constructor object.
        :param id_package: id of package
        :type id_package: int
        :param weight: weight of package
        :type weight: float
        :param description: description of package
        :type description: str
        """
        self._id_package = id_package
        self._weight = weight
        self._description = description
        self._cost = self.calculate(weight)
    
    #Properties: sets and gets

    @property
    def id_package(self) -> int:
        """ returns id_package of the package
            :returns: id_package
            :rtype: int
        """
        return self._id_package


    @id_package.setter
    def id_package(self, id_package : int):
        """ id of package
            :param id_package: id of package
            :type: int
        """
        self._id_package = id_package

    @property
    def weight(self) -> float:
        """ returns weight of the package
            :returns: weight
            :rtype: float
        """
        return self._weight

    @weight.setter
    def weight(self, weight : float):
        """ weight of package
            :param weight: weight of package
            :type: float
        """
        if(weight <= 0.0):
            self._weight = weight
        else:
            self._weight = 0.0

    @property
    def description(self) -> str:
        """ returns description of the package
            :returns: description
            :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description : str):
        """ description of package
            :param description: description of package
            :type: str
        """
        self._description = description

    @property
    def cost(self) -> float:
        """ returns cost of the package
            :returns: cost
            :rtype: float
        """
        return self._cost
    
    #Methods
    
    def calculate(self, weight : float) -> float:
        """ abstract method:
            calculates cost of package
            :returns: pass
            :rtype: float
        """
        pass
    
    def __str__(self):
        """ returns str of the package
            :returns: string package
            :rtype: str
        """
        return 'id = ({0}), peso = ({1}), descripcion = ({2}), costo = ({3})'.format(self._id_package, self._weight, self._description, self._cost)
       