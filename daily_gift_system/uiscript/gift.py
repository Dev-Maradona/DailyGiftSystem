
import uiScriptLocale

ROOT_PATH = "d:/ymir work/efsun_gui/"
FACE_SLOT_FILE = "d:/ymir work/ui/game/windows/box_face.sub"
image47 = "d:/ymir work/efsun_gui/"

window = {
	"name" : "Isinlanma",

	"x" : 0,
	"y" : 15+50+6+5+6+0,

	"style" : ("movable", "float",),

	"width" : 220,
	"height" : 225,

	"children" :
	(
		{
			"name" : "board",
			"type" : "board",
			"style" : ("attach", "ignore_size",),

			"x" : 0,
			"y" : 0,

            "horizontal_align" : "center",
            "vertical_align" : "center",

			"width" : 220,#550
			"height" : 225,

			"children" :
			(
				## Title
				{
					"name" : "TitleBar",
					"type" : "titlebar",
					"style" : ("attach",),

					"x" : 6,
					"y" : 6,

					"width" : 210,
					"color" : "yellow",

					"children" :
					(
						{
							"name" : "TitleName",
							"type" : "text",

							"x" : 0,
							"y" : 3,

							"horizontal_align" : "center",

							"text" : "Daily Gift System",

							"text_horizontal_align" : "center",
						},
					),
				},
				
				{
					"name" : "thinboard",
					"type" : "thinboard",
					"x": 14,
					"y":  93+3,
					"width": 200,
					"height": 120,
				},
				{
				 	"name" : "thinboard",
					"type" : "thinboard",
				 	"x": 14,
					"y":  35,
					"width": 523/2-60,
					"height": 60,
				},
				# {
				# 	"name" : "thinboard",
				# 	"type" : "thinboard",
				# 	"x": 217,
				# 	"y":  35,
				# 	"width": 523/2+59,
				# 	"height": 60,
				# },
				{
					"name" : "Face_image",
					"type" : "image",
					"x" : 23,
					"y" : 37,
				},
				{ "name" : "Face_Slot", "type" : "image", "x" : 23, "y" : 37, "image" : FACE_SLOT_FILE, },
				{
					"name" : "Character_Info_Bar",
					"type" : "image",
					"x" : 75,
					"y" : 37,
					"image" : image47+"private_leftNameImg.sub",
				},
				{
					"name" : "Character_Info",
					"type" : "text",
					"x" : 100,
					"y" : 41,
					"text" : "Character name",
				},
				{
					"name":"Name_Slot",
					"type":"image",

					"x":77,
					"y":37+26,#37+26

					"image":"d:/ymir work/ui/public/parameter_slot_04.sub",
				},
				{
					"name" : "UserName",
					"type" : "text",
					"x" : 85+2,
					"y" : 41+25,
				},
				{
					"name" : "Gift1",
					"type" : "button",

					"x" : 0,
					"y" : 15+50+6+5+6+28,

					"horizontal_align" : "center",

					"default_image" : ROOT_PATH + "offical_button.tga",
					"over_image" : ROOT_PATH + "offical_button_bastim.tga",
					"down_image" : ROOT_PATH + "offical_button.tga",

					"text" : "Daily Gift 1",#|cffffff00
				},
				{
					"name" : "Gift2",
					"type" : "button",

					"x" : 0,
					"y" : 15+50+6+5+6+28+28,

					"horizontal_align" : "center",

					"default_image" : ROOT_PATH + "offical_button.tga",
					"over_image" : ROOT_PATH + "offical_button_bastim.tga",
					"down_image" : ROOT_PATH + "offical_button.tga",

					"text" : "Daily Gift 2",#|cFFA52A2A
				},
				{
					"name" : "Gift3",
					"type" : "button",

					"x" : 0,
					"y" : 15+50+6+5+6+28+28+28,

					"horizontal_align" : "center",

					"default_image" : ROOT_PATH + "offical_button.tga",
					"over_image" : ROOT_PATH + "offical_button_bastim.tga",
					"down_image" : ROOT_PATH + "offical_button.tga",

					"text" : "Daily Gift 3",#|cff888888
				},
			),
		},
	),
}