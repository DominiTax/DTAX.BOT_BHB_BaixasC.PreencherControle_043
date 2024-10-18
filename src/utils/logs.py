from Logger import LogManager
from datetime import datetime
import os

now = datetime.now().strftime("%d-%m-%Y_%Hh-%Mm-%Ss")
bot_name = "DTAX.BOT_BHB_BaixasC.PreencherControle_043"
logger = LogManager(bot_name, now, log_dir=os.path.join(os.getcwd(), "logs"))
logger.log("info", f"Iniciando bot {bot_name}")
