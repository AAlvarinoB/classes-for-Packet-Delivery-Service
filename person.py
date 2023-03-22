class Person(object):
    """
    Class used to represent a Person
    """
    def __init__(self, id_person: str = '123456789', name: str = 'name', last_name: str = 'lastName', contact_num: str = '123456789'):
        """
        Person constructor object
        :param id_person: id of person
        :type id_person: str
        :param name: name of person
        :type name: str
        :param last_name: last name of person
        :type last_name: str
        :param contact_num: contact number of person
        :type contact_num: str
        """
        self._id_person = id_person
        self._name = name
        self._last_name = last_name
        self._contact_num = contact_num

    @property
    def id_person(self) -> str:
        """ returns id of the person    
            :returns: id_person
            :rtype: str    
        """
        return self._id_person
    
    @id_person.setter
    def id_person(self, id_person: str):
        """ id of person
            :param id_person: id of person
            :type: str
        """
        self._id_person = id_person

    @property
    def name(self) -> str:
        """ returns name of the person
            :returns: name
            :rtype: str
        """
        return self._name
    
    @name.setter
    def name(self, name: str):
        """ name of person
            :param name: name of person
            :type: str
        """
        self._name = name

    @property
    def last_name(self) -> str:
        """ returns last name of the person
            :returns: last_name
            :rtype: str
        """
        return self._last_name
    
    @last_name.setter
    def last_name(self, last_name: str):
        """ last name of person
            :param last_name: last name of person
            :type: str
        """
        self._last_name = last_name

    @property
    def contact_num(self) -> str:
        """ returns contact number of the person
            :returns: contact_num
            :rtype: str
        """
        return self._contact_num
    
    @contact_num.setter
    def contact_num(self, contact_num: str):
        """ contact number of person
            :param contact_num: contact number of person
            :type: str
        """
        self._contact_num = contact_num

    def __str__(self):
        """ returns str of person
            :returns: string person
            :rtype: str
        """
        return 'id = ({0}), nombre = ({1}), apellido = ({2}), num_contacto = ({3})'.format(self._id_person, self._name, self._last_name, self._contact_num)
