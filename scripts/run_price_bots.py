import asyncio
from dotenv import load_dotenv
import json
import os
import sys

sys.path.insert(
    0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../src"))
)

from tribe_bot import TribeBot
from fei_bot import FeiBot

load_dotenv()

loop = asyncio.get_event_loop()

# establishes Tribe Bot    
tribe_client = TribeBot(
        coingecko_token_id="tribe-2",
        token_display="TRIBE",
        token_address=os.getenv("TRIBE_ADDRESS"),
        discord_id=os.getenv("BOT_ID_TRIBE"),
    )
    # establishes Fei Bot    
fei_client = FeiBot(
        coingecko_token_id="fei-protocol",
        token_display="Fei",
        token_address=os.getenv("FEI_ADDRESS"),
        discord_id=os.getenv("BOT_ID_FEI"),
    )
   
loop.create_task(tribe_client.start(os.getenv("BOT_TOKEN_TRIBE")))
       
loop.run_forever()
