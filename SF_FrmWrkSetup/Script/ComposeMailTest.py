import ComposeMail

def Compose_MailTest():
    #Clicks the 'linkSent' link.
    Aliases.browser.pageInbox5Zenithzehra67GmailComG.linkSent.Click()
    a =Aliases.browser.pageInbox5Zenithzehra67GmailComG.panelShowMoreMessages.contentText
    ComposeMail.Compose_Mail()
    Aliases.browser.pageInbox5Zenithzehra67GmailComG.linkSent.Click()
    b =Aliases.browser.pageInbox5Zenithzehra67GmailComG.panelShowMoreMessages.contentText
    if a!=b:
     Log.Message("Mail has been sent successfully")
    elif a==b:
     Log.Message("Mail has not been sent successfully",a,b)
