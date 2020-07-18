from accessify import protected
import vk_api
import LoginOnVk as log

class Finders(log.Confidential):
	
	__logOn = log.Confidential().Login()
	
	@protected
	def _GetIdFriends(self):
		return self.__logOn.method("friends.get")

	@protected
	def _GetIdFirstPerson(self, hisId):
		idH = self.__logOn.method("friends.get", 
			{
			"user_id":hisId
			})
		return idH['items']
	@protected
	def _GetIdSecondPerson(self, hisId):
		idH = self.__logOn.method("friends.get", 
			{
			"user_id":hisId
			})		
		return idH['items']

	def GetAllId(self, firstId, secondId):
		self.ourId = []
		allFriendsFirstPerson = self._GetIdFirstPerson(firstId)
		allFriendsSecondPerson = self._GetIdSecondPerson(secondId)
		for i in allFriendsFirstPerson:
			for j in allFriendsSecondPerson:
				if (i == j):
					self.ourId.append(i)
		return self.ourId 
	def MailGet(self):
		self.getMes = self.__logOn.method('messages.getConversations', {
										'count':1
										})['items'][0]['last_message']['text'].split(" ")
		if (self.getMes[0] == 'true'):
			try:
				return self.GetAllId(int(self.getMes[1]), int(self.getMes[2]))
			except:
				print("Ошибка в передаче id")
		else:
			pass