import httplib2
from apiclient import discovery
from oauth2client.service_account import ServiceAccountCredentials

from . import settings

credentials = ServiceAccountCredentials.from_json_keyfile_name(
    settings.GOOGLE_CREDENTIALS_FILE,
    ['https://www.googleapis.com/auth/spreadsheets',
     'https://www.googleapis.com/auth/drive'])
httpAuth = credentials.authorize(httplib2.Http())
google_client = discovery.build('sheets', 'v4', http=httpAuth)
