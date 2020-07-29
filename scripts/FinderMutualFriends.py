from accessify import protected
import vk_api
import LoginOnVk as log
from random import randint

ConnectionToApi = False
Json = ""


class Finders(log.Confidential):
	'''работаем с апи вк получаем друзей и сравниваем их --- '''

	ConnectionToApi = False
	Json = ""

	try:
		__logOn = log.Confidential().Login()

	except:
		__logOn = log.Confidential.LogPass()
		__logOn.auth()
	finally:
		print("Авторизация выполнена")
	@protected
	def __GetIdFriends(self):
		return self.__logOn.method("friends.get")

	@protected
	def __GetIdPerson(self, hisId):
		try:
			idH = self.__logOn.method("friends.get",
				{
				"user_id":hisId
				})
		except Exception as e:
				print("Exception", e)
		return idH['items']
	@protected
	def __GetAllId(self, firstId: int, secondId: int):
		self.ourId = []
		allFriendsFirstPerson = self.__GetIdPerson(firstId)
		allFriendsSecondPerson = self.__GetIdPerson(secondId)
		for i in allFriendsFirstPerson:
			for j in allFriendsSecondPerson:
				if (i == j):
					self.ourId.append(i)
		return self.ourId

	@protected
	def __SendMessageUser(self, allIdUsers, id) -> None:
		self.__logOn('messages.send', {
		'user_id': id,
		'message': allIdUsers
		})


	def TryUnreadMessages(self):
		return   self.__logOn.method('messages.getConversations', {
				'count':1,
				'filter':'unread'
				})


	def MailGet(self):
		self.getJson = self.TryUnreadMessages()

		self.getMes = self.getJson['items'][0]['last_message']['text'].split(" ")
		self.getIdUser  = self.getJson['items'][0]['last_message']['from_id']

		print(self.getMes)
		if (self.getMes[0] == 'true'):
			try:
				self.__SendMessageUser(self.__GetAllId(int(self.getMes[1]), int(self.getMes[2])), self.getIdUser)
			except:
				try:
					self.__logOn.method('messages.send', {
					'user_id': self.getIdUser,
					'random_id':randint(1, 10*20),
					'message': "произошла внутренняя ошибка"
					})
				except Exception as e:
					print('Exception', e)
		else:
			try:
				self.__logOn.method('messages.send', {
				'user_id': self.getIdUser,
				'random_id':randint(1, 10**20),
				'message': "true не обработан"
				})
			except Exception as e:
				print("Exception", e)
