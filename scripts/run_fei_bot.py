import asyncio
from dotenv import load_dotenv
import json
import os
import sys

sys.path.insert(
    0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../src"))
)

from fei_bot import FeiBot

load_dotenv()

loop = asyncio.get_event_loop()

# establishes Fei Bot    
fei_client = FeiBot(
        coingecko_token_id="fei-protocol",
        token_display="Fei",
        token_address=os.getenv("FEI_ADDRESS"),
        discord_id=os.getenv("BOT_ID_FEI"),
    )
   
loop.create_task(fei_client.start(os.getenv("BOT_TOKEN_FEI")))
   
loop.run_forever()
