
# add At end of file

	def OpenDailyGiftSystem(self):
		import uidailygift
		self.dailygiftsystem = uidailygift.gift()
		self.dailygiftsystem.Show()



# Search: 

		serverCommandList={

#Add :

			"OpenDailyGiftSystem"			:self.OpenDailyGiftSystem,