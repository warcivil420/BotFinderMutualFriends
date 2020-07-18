import vk_api

class Confidential():

	token = ""

	def Login(self):
		return vk_api.VkApi(token=self.token)

	def LogPass(self):
		return vk_api.VkApi(Login = "", Password="")

# need two library -> accessify /vk_api || pip3 install accessify, vk_api