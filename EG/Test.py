from pyOutlook import OutlookAccount

from O365 import Account
credentials = ('022b618e-081a-4ad9-b9e6-66d5584a098f', 'f9HU765MyLslv_X1.Nwrcrb_rYY~9wF5C_')

# the default protocol will be Microsoft Graph
# the default authentication method will be "on behalf of a user"

account = Account(credentials)


mailbox = account.mailbox()

inbox = mailbox.inbox_folder()

for message in inbox.get_messages():
    print(message, message.created)

sent_folder = mailbox.sent_folder()

for message in sent_folder.get_messages():
    print(message)