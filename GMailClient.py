class GMailClient:

    def __init__(self,userId):
        self.userId = userId
        self.password = '!'
        self.token = ''
        self.scopes = []
        self.redirect_uri = ''
        self.client_id = ''
        self.draft_credentials = GMailDraft()




    def convert_scopes(self):
        return ' '.join(self.scopes)



class GMailDraft(GMailClient):

    def __init__(self):
        self.draft_id = 'Hello world!'