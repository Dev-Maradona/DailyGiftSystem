// Search :
struct command_info cmd_info[] =

// Add above 
#ifdef ENABLE_DAILY_GIFT
ACMD (do_daily_gift);
#endif


// Search :
	{ "\n",		NULL,			0,			POS_DEAD,	GM_IMPLEMENTOR	}

// Add above
#ifdef ENABLE_DAILY_GIFT
	{ "daily_gift",		do_daily_gift,			0,	POS_DEAD,	GM_PLAYER },
#endif