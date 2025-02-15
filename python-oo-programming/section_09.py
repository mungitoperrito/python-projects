# Abstraction

class EmailServer:

    def _connect(self):
        print('Connecting ...')


    def _authenticate(self):
        print('Authenticating ...')


    def _disconnect(self):
        print('Disconnecting')


    def send_email(self):
        self._connect()
        self._authenticate()
        print('Sending email ...')
        self._disconnect()


############
### MAIN ###
############

if __name__ == '__main__':
    email_01 = EmailServer()
    email_01.send_email()
    # EmailServer.send_email()   # Fails, has to be @staticmethod, @classmethod
