import vk_api

class Confidential():

	token = "bcc1ff52fc0f71d00849e3ac3e69ede3620ade336c292d137a57ea70242a4222be4a9dd324d7eb3d9a0d1"
	# токен для входа в вк (создавать токен группы)


	def Login(self):
		return vk_api.VkApi(token=self.token)

	def LogPass(self):
		return vk_api.VkApi(Login = "", Password="") # альтернативный вариант для входа

# need two library -> accessify /vk_api || pip3 install accessify, vk_api
