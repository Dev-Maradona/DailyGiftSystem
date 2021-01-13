
import ui
import player
import localeInfo
import constInfo
import chat
import wndMgr
import math
import net
import ui,dbg,app,grp
import chat
#------ User Name
import net
import player
import item
import snd
import shop
import wndMgr
import app
import chat
import chr

import ui
import uiCommon
import uiToolTip
import mouseModule
import localeInfo
import constInfo
#------ User Name
#------ FACE IMAGE
import dbg
import ui
import snd
import systemSetting
import chat
import app
import localeInfo
import constInfo
import chrmgr
import background
import player
import musicInfo
import ui
import player 
import constInfo
import snd
import app
import uiToolTip
import dbg
import playerSettingModule
import uicharacter
import event
import chat
import grp
import item
import time
import wndMgr
import uiCommon
import os
import chr
import chrmgr
import quest
import ime
import interfaceModule
import uiScriptLocale
import dbg
import ui
import snd
import systemSetting
import chat
import app
import localeInfo
import ui
import snd
import systemSetting
import chat
import app
import localeInfo
import constInfo
import chrmgr
import player
import background
import serverinfo
import constInfo
import playerSettingModule
import chrmgr
import background
import player
import musicInfo
import uiSelectMusic
import background
#------ FACE IMAGE

FACE_IMAGE_DICT = {
	playerSettingModule.RACE_WARRIOR_M	: "icon/face/warrior_m.tga",
	playerSettingModule.RACE_WARRIOR_W	: "icon/face/warrior_w.tga",
	playerSettingModule.RACE_ASSASSIN_M	: "icon/face/assassin_m.tga",
	playerSettingModule.RACE_ASSASSIN_W	: "icon/face/assassin_w.tga",
	playerSettingModule.RACE_SURA_M		: "icon/face/sura_m.tga",
	playerSettingModule.RACE_SURA_W		: "icon/face/sura_w.tga",
	playerSettingModule.RACE_SHAMAN_M	: "icon/face/shaman_m.tga",
	playerSettingModule.RACE_SHAMAN_W	: "icon/face/shaman_w.tga",
}

class gift(ui.ScriptWindow):

	def __init__(self):
		ui.ScriptWindow.__init__(self)

		self.__LoadDialog()
		self.OnUpdate()

		#self.wndOperation = uiOperation.OperationWindow()

	def __del__(self):
		ui.ScriptWindow.__del__(self)

	def Show(self):
		self.SetCenterPosition()
		self.SetTop()
		self.__LoadDialog()
		
		# Set UserName
		if (chr.GetRace() in [0, 2, 5, 7]):
			self.userName.SetText(player.GetName()+ self.color["Levelcolor"] +"  Lv." + str(player.GetStatus(player.LEVEL)) + "")
		else:
			self.userName.SetText(player.GetName()+ self.color["Levelcolor"] +"  Lv." + str(player.GetStatus(player.LEVEL)) + "")
		# End Of User name 1

		race = net.GetMainActorRace()
		faceImageName = FACE_IMAGE_DICT[race]

		self.Face_image.SetPosition(150, 40)#25, 40
		self.Face_image.LoadImage(faceImageName)
		self.Face_image.Show()
		# End Of Set UserName
			
		ui.ScriptWindow.Show(self)

	def __LoadDialog(self):

		try:

			pyScrLoader = ui.PythonScriptLoader()
			pyScrLoader.LoadScriptFile(self, "uiscript/gift.py")

			self.board = self.GetChild("board")
			self.GetChild("TitleBar").SetCloseEvent(ui.__mem_func__(self.Close))
			self.Gift1 = self.GetChild("Gift1")
			self.Gift2 = self.GetChild("Gift2")
			self.Gift3 = self.GetChild("Gift3")

			self.userName = self.GetChild("UserName")
			self.Face_image = self.GetChild("Face_image")

			#---- color
			self.color = {
			"Levelcolor" : "|cff00ff00|h",
			"Blue" : "|cff00ffff|h",
			"Red" : "|cffff6060|h",
			"yellow"	:	"|cffffff00|h",
			"gold" : "|cffffcc00|h"
		}
			#---- color
			

			self.Gift1.SetEvent(ui.__mem_func__(self.ClickGift1))
			self.Gift2.SetEvent(ui.__mem_func__(self.ClickGift2))
			self.Gift3.SetEvent(ui.__mem_func__(self.ClickGift3))
			self.SetPosition(
					(wndMgr.GetScreenWidth() / 2) - int(math.floor(self.GetWidth() / 2.)),
					(wndMgr.GetScreenHeight() / 2) - int(math.floor(self.GetHeight() / 2.))
					)

		except:
			import exception
			exception.Abort("DuelloDialog.LoadDialog.BindObject")

	def Close(self):
		self.Hide()

	def OnPressEscapeKey(self):
		self.Close()
		return TRUE

	def OnUpdate(self):
		return TRUE


	def ClickGift1(self):
		net.SendChatPacket("/daily_gift a")
		self.Close()
		
	def ClickGift2(self):
		net.SendChatPacket("/daily_gift b")
		self.Close()

	def ClickGift3(self):
		net.SendChatPacket("/daily_gift c")
		self.Close()


class ComboBox(ui.Window):

	class ListBoxWithBoard(ui.ListBox):

		def __init__(self, layer):
			ui.ListBox.__init__(self, layer)

		def OnRender(self):
			xRender, yRender = self.GetGlobalPosition()
			yRender -= self.TEMPORARY_PLACE
			widthRender = self.width
			heightRender = self.height + self.TEMPORARY_PLACE*2
			grp.SetColor(ui.BACKGROUND_COLOR)
			grp.RenderBar(xRender, yRender, widthRender, heightRender)
			grp.SetColor(ui.DARK_COLOR)
			grp.RenderLine(xRender, yRender, widthRender, 0)
			grp.RenderLine(xRender, yRender, 0, heightRender)
			grp.SetColor(ui.BRIGHT_COLOR)
			grp.RenderLine(xRender, yRender+heightRender, widthRender, 0)
			grp.RenderLine(xRender+widthRender, yRender, 0, heightRender)

			ui.ListBox.OnRender(self)

	def __init__(self):
		ui.Window.__init__(self)
		self.x = 0
		self.y = 0
		self.width = 0
		self.height = 0
		self.isSelected = FALSE
		self.isOver = FALSE
		self.isListOpened = FALSE
		self.event = lambda *arg: None
		self.enable = TRUE

		self.textLine = ui.MakeTextLine(self)
		self.textLine.SetText(localeInfo.UI_ITEM)

		self.listBox = self.ListBoxWithBoard("TOP_MOST")
		self.listBox.SetPickAlways()
		self.listBox.SetParent(self)
		self.listBox.SetEvent(ui.__mem_func__(self.OnSelectItem))
		self.listBox.Hide()

	def __del__(self):
		ui.Window.__del__(self)

	def Destroy(self):
		self.textLine = None
		self.listBox = None

	def SetPosition(self, x, y):
		ui.Window.SetPosition(self, x, y)
		self.x = x
		self.y = y
		self.__ArrangeListBox()

	def SetSize(self, width, height):
		ui.Window.SetSize(self, width, height)
		self.width = width
		self.height = height
		self.textLine.UpdateRect()
		self.__ArrangeListBox()

	def __ArrangeListBox(self):
		self.listBox.SetPosition(0, self.height + 5)
		self.listBox.SetWidth(self.width)

	def Enable(self):
		self.enable = TRUE

	def Disable(self):
		self.enable = FALSE
		self.textLine.SetText("")
		self.CloseListBox()

	def SetEvent(self, event):
		self.event = event

	def ClearItem(self):
		self.CloseListBox()
		self.listBox.ClearItem()

	def InsertItem(self, index, name):
		self.listBox.InsertItem(index, name)
		self.listBox.ArrangeItem()

	def SetCurrentItem(self, text):
		self.textLine.SetText(text)

	def GetCurrentText(self):
		return self.textLine.GetText()

	def GetCurrentIndex(self):
		return self.listBox.selectedLine
		
	def SelectItem(self, key):
		self.listBox.SelectItem(key)

	def OnSelectItem(self, index, name):
		self.SetCurrentItem(name)
		self.CloseListBox()
		self.event(index)

	def CloseListBox(self):
		self.isListOpened = FALSE
		self.listBox.Hide()

	def OnMouseLeftButtonDown(self):

		if not self.enable:
			return

		self.isSelected = TRUE

	def OnMouseLeftButtonUp(self):

		if not self.enable:
			return

		self.isSelected = FALSE

		if self.isListOpened:
			self.CloseListBox()
		else:
			if self.listBox.GetItemCount() > 0:
				self.isListOpened = TRUE
				self.listBox.Show()
				self.__ArrangeListBox()

	def OnUpdate(self):

		if not self.enable:
			return

		if self.IsIn():
			self.isOver = TRUE
		else:
			self.isOver = FALSE

	def OnRender(self):
		self.x, self.y = self.GetGlobalPosition()
		xRender = self.x
		yRender = self.y
		widthRender = self.width
		heightRender = self.height
		import ui,dbg,app,grp
		grp.SetColor(ui.BACKGROUND_COLOR)
		grp.RenderBar(xRender, yRender, widthRender, heightRender)
		grp.SetColor(ui.DARK_COLOR)
		grp.RenderLine(xRender, yRender, widthRender, 0)
		grp.RenderLine(xRender, yRender, 0, heightRender)
		grp.SetColor(ui.BRIGHT_COLOR)
		grp.RenderLine(xRender, yRender+heightRender, widthRender, 0)
		grp.RenderLine(xRender+widthRender, yRender, 0, heightRender)

		if self.isOver:
			grp.SetColor(ui.HALF_WHITE_COLOR)
			grp.RenderBar(xRender + 2, yRender + 3, self.width - 3, heightRender - 5)

			if self.isSelected:
				grp.SetColor(ui.WHITE_COLOR)
				grp.RenderBar(xRender + 2, yRender + 3, self.width - 3, heightRender - 5)	
class RestoreDialog1(ui.ScriptWindow):
	def __init__(self):
		ui.ScriptWindow.__init__(self)
		self.isLoaded = 0
		self.LoadButtons()

	def __del__(self):
		ui.ScriptWindow.__del__(self)
		
	def LoadButtons(self):
		if self.isLoaded == 1:
			return
		self.isLoaded = 1
			
	def OpenPanel(self):
		self.dial = Dialog1()
		self.dial.Show()
		self.Close()
		
	def Close(self):
		self.Button1.Hide()
class Component:
	def Button(self, parent, buttonName, tooltipText, x, y, func, UpVisual, OverVisual, DownVisual):
		button = ui.Button()
		if parent != None:
			button.SetParent(parent)
		button.SetPosition(x, y)
		button.SetUpVisual(UpVisual)
		button.SetOverVisual(OverVisual)
		button.SetDownVisual(DownVisual)
		button.SetText(buttonName)
		button.SetToolTipText(tooltipText)
		button.Show()
		button.SetEvent(func)
		return button

	def ToggleButton(self, parent, buttonName, tooltipText, x, y, funcUp, funcDown, UpVisual, OverVisual, DownVisual):
		button = ui.ToggleButton()
		if parent != None:
			button.SetParent(parent)
		button.SetPosition(x, y)
		button.SetUpVisual(UpVisual)
		button.SetOverVisual(OverVisual)
		button.SetDownVisual(DownVisual)
		button.SetText(buttonName)
		button.SetToolTipText(tooltipText)
		button.Show()
		button.SetToggleUpEvent(funcUp)
		button.SetToggleDownEvent(funcDown)
		return button

	def EditLine(self, parent, editlineText, x, y, width, heigh, max):
		SlotBar = ui.SlotBar()
		if parent != None:
			SlotBar.SetParent(parent)
		SlotBar.SetSize(width, heigh)
		SlotBar.SetPosition(x, y)
		SlotBar.Show()
		Value = ui.EditLine()
		Value.SetParent(SlotBar)
		Value.SetSize(width, heigh)
		Value.SetPosition(1, 1)
		Value.SetMax(max)
		Value.SetLimitWidth(width)
		Value.SetMultiLine()
		Value.SetText(editlineText)
		Value.Show()
		return SlotBar, Value

	def TextLine(self, parent, textlineText, x, y, color):
		textline = ui.TextLine()
		if parent != None:
			textline.SetParent(parent)
		textline.SetPosition(x, y)
		if color != None:
			textline.SetFontColor(color[0], color[1], color[2])
		textline.SetText(textlineText)
		textline.Show()
		return textline

	def RGB(self, r, g, b):
		return (r*255, g*255, b*255)

	def SliderBar(self, parent, sliderPos, func, x, y):
		Slider = ui.SliderBar()
		if parent != None:
			Slider.SetParent(parent)
		Slider.SetPosition(x, y)
		Slider.SetSliderPos(sliderPos / 100)
		Slider.Show()
		Slider.SetEvent(func)
		return Slider

	def ExpandedImage(self, parent, x, y, img):
		image = ui.ExpandedImageBox()
		if parent != None:
			image.SetParent(parent)
		image.SetPosition(x, y)
		image.LoadImage(img)
		image.Show()
		return image

	def ComboBox(self, parent, text, x, y, width):
		combo = ComboBox()
		if parent != None:
			combo.SetParent(parent)
		combo.SetPosition(x, y)
		combo.SetSize(width, 15)
		combo.SetCurrentItem(text)
		combo.Show()
		return combo

	def ThinBoard(self, parent, moveable, x, y, width, heigh, center):
		thin = ui.ThinBoard()
		if parent != None:
			thin.SetParent(parent)
		if moveable == TRUE:
			thin.AddFlag('movable')
			thin.AddFlag('float')
		thin.SetSize(width, heigh)
		thin.SetPosition(x, y)
		if center == TRUE:
			thin.SetCenterPosition()
		thin.Show()
		return thin

	def Gauge(self, parent, width, color, x, y):
		gauge = ui.Gauge()
		if parent != None:
			gauge.SetParent(parent)
		gauge.SetPosition(x, y)
		gauge.MakeGauge(width, color)
		gauge.Show()
		return gauge

	def ListBoxEx(self, parent, x, y, width, heigh):
		bar = ui.Bar()
		if parent != None:
			bar.SetParent(parent)
		bar.SetPosition(x, y)
		bar.SetSize(width, heigh)
		bar.SetColor(0x77000000)
		bar.Show()
		ListBox=ui.ListBoxEx()
		ListBox.SetParent(bar)
		ListBox.SetPosition(0, 0)
		ListBox.SetSize(width, heigh)
		ListBox.Show()
		scroll = ui.ScrollBar()
		scroll.SetParent(ListBox)
		scroll.SetPosition(width-15, 0)
		scroll.SetScrollBarSize(heigh)
		scroll.Show()
		ListBox.SetScrollBar(scroll)
		return bar, ListBox

rest = RestoreDialog1()
rest.Show()
