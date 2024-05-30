class Ticket:
    def __init__(self, title, description, status, created_at, creator, technician=None, closed_at=None):
        self.__title = title
        self.__description = description
        self.__status = status
        self.__created_at = created_at
        self.__creator = creator
        self.__technician = technician
        self.__closed_at = closed_at

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, title):
        self.__title = title

    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, description):
        self.__description = description

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, status):
        self.__status = status

    @property
    def created_at(self):
        return self.__created_at

    @created_at.setter
    def created_at(self, created_at):
        self.__created_at = created_at

    @property
    def closed_at(self):
        return self.__closed_at

    @closed_at.setter
    def closed_at(self, closed_at):
        self.__closed_at = closed_at

    #@property
    #def creator(self):
        #return self.__creator
   #@creator.setter
    #def creator(self, creator):
        #self.__creator = creator

    #@property
    #def technician(self):
        #return self.__technician

    #@technician.setter
    #def technician(self, technician):
        #self.__technician = technician
