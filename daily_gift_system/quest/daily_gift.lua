-- Quest 
-- Create By Maradona
-- Discoord Maradona#4588
-- daily Gift System
-- 2021

quest daily_gift begin
	state start begin

		when 9004.chat." ������ ��� ������ ������� " begin
			if pc.get_level() <= 50 then
				say_title(" ������ ������� ")
				say(" ��� �� ���� ������ ���� �� 50 ")
				return
			end
			if get_time() > pc.getqf("duration") then
				say_title(" ������ ������� ")
				setdelay(10)
				say(" �� ��� ����� ������ ��� ������ ������� ")
				say(" ���� �� ���� ���� ���� �� ����� ")
				say(" ���� ������� ��� ������� ����� ������� ")
				say(" ��� ����� ��� ��� ���� ����� ������� ���� ��� ����� ���� ")
				say(" �� ������ ����� ����� ��� ��� ���� 24 ���� ")
				local s = select(" ��� ����� ������� "," �� , ��� ���� ")
				if s == 1 then
					cmdchat("OpenDailyGiftSystem")
					pc.setqf("duration",get_time()+60*60*24) 			--24h = 60*60*24
				elseif s == 2 then
					return
				end
				--pc.give_item2(setting.fruit)
			else	
				say_title(" ������ ������� ")
				setdelay(10)
				say(" ��� ������ ����� ������ ")
				say(" ���� �������� 24 ���� ������� ������ ��� ���� ")
			end
		end

		when 9004.chat." ������� ����� ������� " begin
				say_title(" ����� ������� ")
				local ss = select(" ������ ������ "," ������ ������� "," ������ ������� "," ���� ")
				if ss == 1 then
				
					setdelay(10)
					say(" 1.����� ������� ")
					say(" �� ��� ����� ������� ���� ������� ")
					say(" ���� ������ ���� �������� ")
					say(" ���� ��� ��� : ")
					say_item_vnum(71036)
					say(" ���� ��� ��� �� ������ ")
					say(" ������ : ")
					say(" ��� ��� ���� ������� ���� ��� ")
					say(" ������ ������ ��� ")
				elseif ss == 2 then
				
					setdelay(10)
					say(" 2.����� ������� ")
					say(" �� ��� ����� ������� ���� ������� ")
					say(" ���� ������ ���� �������� ������� ")
					say(" ���� ��� ��� : ")
					say_item_vnum(80005)
					say(" ���� ��� ��� �� ������ ")
					say(" ������ : ")
					say(" ��� ��� ���� ������� ���� ��� ")
					say(" ������ ������ ��� ")
				elseif ss == 3 then
				
					setdelay(10)
					say(" 1.����� �������� ")
					say(" �� ��� ����� ������� ���� ������� ")
					say(" ���� ������ ���� ��������� ")
					say(" ���� ��� ��� : ")
					say_item_vnum(100000)
					say(" ���� ��� ��� �� ������ ")
					say(" ������ : ")
					say(" ��� ��� ���� ������� ���� ��� ")
					say(" ������ ������ ��� ")
				end -- if statement
		end-- when

	end	-- state
end	--quest