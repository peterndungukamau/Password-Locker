

class Credentials:
    """
    Class that generates new instances of credentials
    """

    credential_list = []

    def __init__(self, account_name, password):

        self.account_name = account_name
        self.password = password


    def __repr__(self):
        return "accountname: %s password: %s" %(self.account_name,self.password)

    def save_credentials(self):
        '''
        save_credentials method that saves credential object into credentials_list
        '''

        Credentials.credential_list.append(self)

    @classmethod
    def view_credentials(cls):
        '''
        method to view credentials list
        '''

        return cls.credential_list

    def delete_credentials(self):
        '''
        delete method for deleting credential_list
        '''

        Credentials.credential_list.remove(self)