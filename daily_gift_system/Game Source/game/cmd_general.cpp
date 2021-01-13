// Search :
#include "../../common/VnumHelper.h"

// add Below(after)
#ifdef ENABLE_DAILY_GIFT
	#include "../../common/length.h"
#endif

// Search 
ACMD(do_click_mall)

// Add after This cmd

#ifdef ENABLE_DAILY_GIFT
ACMD(do_daily_gift)
{
	char arg1[256];
	one_argument(argument, arg1, sizeof(arg1));

	if (!ch)
		return;

	if (ch->GetLevel() <= 50)
	{
		ch->ChatPacket(CHAT_TYPE_INFO,"Your level Must be 50 at least");
		return;
	}

	if (!ch->IsPC() || NULL == ch)
		return;

	if (!*arg1)
	{
		ch->ChatPacket(CHAT_TYPE_INFO, "This argument is not valid.");
		return;
	}

	// for lfefa
	int bl_items_monster[] = { 71036, 71037, 71038, 71039, 71040, 71041, 71042, 71043 };
	// for gold
	int bl_items_gold[] = { 80001, 80001, 80002, 80003, 80004, 80005, 80006, 80007, 80008 };
	// for poitions 
	int bl_items_poitions[] = { 100000, 100001, 1000002, 39037, 39038, 39039, 39040, 39041, 39042 };
	// for energy

	int a_ite = number(0, _countof(bl_items_monster));

	if (*arg1)
	{
	switch (LOWER(*arg1))
		{
	case 'a':
		
		ch->AutoGiveItem(bl_items_monster[a_ite]);
		ch->ChatPacket(CHAT_TYPE_INFO, "You got a daily gift");
		
	break;
	
	case 'b':
	
		ch->AutoGiveItem(bl_items_gold[a_ite]);
		ch->ChatPacket(CHAT_TYPE_INFO, "You got a daily gift");
	
	break;
	
	case 'c':
	
		ch->AutoGiveItem(bl_items_poitions[a_ite]);
		ch->ChatPacket(CHAT_TYPE_INFO, "You got a daily gift");
	
	break;
	
	case 'd':
	
		ch->AutoGiveItem(bl_items_monster[a_ite]);
		ch->ChatPacket(CHAT_TYPE_INFO, "You got a daily gift");
	
	break;
		}
	}
}
#endif