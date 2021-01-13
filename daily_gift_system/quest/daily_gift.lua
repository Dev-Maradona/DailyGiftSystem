-- Quest 
-- Create By Maradona
-- Discoord Maradona#4588
-- daily Gift System
-- 2021

quest daily_gift begin
	state start begin

		when 9004.chat." ÇáÍÕæá Úáí ÇáåÏíÉ ÇáíæãíÉ " begin
			if pc.get_level() <= 50 then
				say_title(" ÇáåÏíÉ ÇáíæãíÉ ")
				say(" íÌÈ Çä íßæä ãÓÊæÇß ÇÚáí ãä 50 ")
				return
			end
			if get_time() > pc.getqf("duration") then
				say_title(" ÇáåÏíÉ ÇáíæãíÉ ")
				setdelay(10)
				say(" ãä åäÇ íãßäß ÇáÍÕæá Úáí ÇáåÏíÉ ÇáíæãíÉ ")
				say(" æÇĞÇ áã ÊÚÑİ ãÇĞÇ Úáíß Çä ÊÎÊÇÑ ")
				say(" Úáíß ÈÇáÑÌæÚ Çáí ãÚáæãÇÊ ŞÇÆãÉ ÇáåÏÇíÇ ")
				say(" ãÚÇ ÇáÚáã Çäß ÇĞÇ İÊÍÊ ŞÇÆãÉ ÇáåÏÇíÇ ÇáÇä æáã ÊÎÊÇÑ ÔíÆÂ ")
				say(" áä ÊÓÊØíÚ İÊÍåÇ ãÌÏÏÂ ÇáÇ ÈÚÏ ãÑæÑ 24 ÓÇÚÉ ")
				local s = select(" İÊÍ ŞÇÆãÉ ÇáåÏÇíÇ "," áÇ , áíÓ ÇáÇä ")
				if s == 1 then
					cmdchat("OpenDailyGiftSystem")
					pc.setqf("duration",get_time()+60*60*24) 			--24h = 60*60*24
				elseif s == 2 then
					return
				end
				--pc.give_item2(setting.fruit)
			else	
				say_title(" ÇáåÏíÉ ÇáíæãíÉ ")
				setdelay(10)
				say(" áŞÏ ÇÓÊáãÊ åÏíÊß ÈÇáİÚá ")
				say(" Úáíß ÇáÇäÊÙÇÑ 24 ÓÇÚÉ áÇÓÊáÇã ÇáåÏíÉ ãÑÉ ÇÎÑí ")
			end
		end

		when 9004.chat." ãÚáæãÇÊ ŞÇÆãÉ ÇáåÏÇíÇ " begin
				say_title(" ŞÇÆãÉ ÇáåÏÇíÇ ")
				local ss = select(" ÇáåÏíÉ ÇáÇæáí "," ÇáåÏíÉ ÇáËÇäíÉ "," ÇáåÏíÉ ÇáËÇáËÉ "," ÎÑæÌ ")
				if ss == 1 then
				
					setdelay(10)
					say(" 1.åÏÇíÇ ÇáÒÚãÇÁ ")
					say(" ãä åäÇ íãßäß ÇÓÊíáÇã åÏíÉ ÚÔæÇÆíÉ ")
					say(" æåĞå ÇáåÏíÉ ÎÇÕÉ ÈÇáÒÚãÇÁ ")
					say(" ãËÇá Úáí Ğáß : ")
					say_item_vnum(71036)
					say(" æÚáí ÍÓÈ ÍÙß İí ÇáåÏíÉ ")
					say(" ãÚáæãÉ : ")
					say(" Óæİ íÊã ÊÛíÑ ÇáÌæÇÆÒ İíãÇ ÈÚÏ ")
					say(" æÇÖÇİÉ ÇáÌÏíÏ áåÇ ")
				elseif ss == 2 then
				
					setdelay(10)
					say(" 2.åÏÇíÇ ÇáŞÓÇÆã ")
					say(" ãä åäÇ íãßäß ÇÓÊíáÇã åÏíÉ ÚÔæÇÆíÉ ")
					say(" æåĞå ÇáåÏíÉ ÎÇÕÉ ÈÇáŞÓÇÆã æÇáíÇäÛ ")
					say(" ãËÇá Úáí Ğáß : ")
					say_item_vnum(80005)
					say(" æÚáí ÍÓÈ ÍÙß İí ÇáåÏíÉ ")
					say(" ãÚáæãÉ : ")
					say(" Óæİ íÊã ÊÛíÑ ÇáÌæÇÆÒ İíãÇ ÈÚÏ ")
					say(" æÇÖÇİÉ ÇáÌÏíÏ áåÇ ")
				elseif ss == 3 then
				
					setdelay(10)
					say(" 1.åÏÇíÇ ÇáÇßÇÓíÑ ")
					say(" ãä åäÇ íãßäß ÇÓÊíáÇã åÏíÉ ÚÔæÇÆíÉ ")
					say(" æåĞå ÇáåÏíÉ ÎÇÕÉ ÈÇáÇßÇÓíÑ ")
					say(" ãËÇá Úáí Ğáß : ")
					say_item_vnum(100000)
					say(" æÚáí ÍÓÈ ÍÙß İí ÇáåÏíÉ ")
					say(" ãÚáæãÉ : ")
					say(" Óæİ íÊã ÊÛíÑ ÇáÌæÇÆÒ İíãÇ ÈÚÏ ")
					say(" æÇÖÇİÉ ÇáÌÏíÏ áåÇ ")
				end -- if statement
		end-- when

	end	-- state
end	--quest