import FinderMutualFriends as Finder

while True:
    if (Finder.Finders().TryUnreadMessages()['count'] > 0):
        Finder.Finders().MailGet()
    else:
        pass
# need two library -> accessify /vk_api || pip3 install accessify, vk_api
