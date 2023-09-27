import os
from os import getenv
from dotenv import load_dotenv

load_dotenv(".env")


API_ID = int(getenv("API_ID", "26691248")) #optional
API_HASH = getenv("API_HASH", "7cc5f91b8389eaea67407887a7c1a6a3") #optional
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "6322234443").split()))
OWNER_ID = getenv("OWNER_ID", "6322234443")
MONGO_URL = getenv("MONGO_URL", "mongodb+srv://udoh:udoh@cluster0.sdmodpx.mongodb.net/?retryWrites=true&w=majority")
BOT_TOKEN = getenv("BOT_TOKEN", "6604047506:AAGJuRbXzX0n1EVswQQq6qWZaSZ76GtCQe0")
ALIVE_PIC = getenv("ALIVE_PIC")
ALIVE_TEXT = getenv("ALIVE_TEXT")
PM_LOGGER = getenv("PM_LOGGER")
OPENAI_API = getenv("OPENAI_API")
RMBG_API = getenv("RMBG_API", "3RCCWg8tMBfDWdAs44YMfJmC")
BOTLOG_CHATID = int(getenv("BOTLOG_CHATID") or 0)
PM_LIMIT = int(getenv("PM_LIMIT") or 5)
BLACKLIST_GCAST = {int(x) for x in getenv("BLACKLIST_GCAST", "").split()}
GIT_TOKEN = getenv("GIT_TOKEN", "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") #personal access token
REPO_URL = getenv("REPO_URL", "https://github.com/opet321/ngontol")
HEROKU_API_KEY = getenv("HEROKU_API_KEY")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
BRANCH = getenv("BRANCH", "main") #don't change
CMD_HNDLR = getenv("CMD_HNDLR", ".")
STRING_SESSION1 = getenv("STRING_SESSION1", "BQGXRrAAJqV6081YSq0-dyJhI2uZRj70a3Wlm4Q5d0KhqWsubMUkJ02togPzwC77ZKGrM0AISOC1nekPuUIdg10SybxxXuQkNG5X4FTtd2dLgozc4vfqueSb9rpkfKZqtRIpRX9dap1feM9VHnt19l9oWwhLrTVWjQxzQpY2VdoERx68BzuGebljUXrGbICS68FvlFR8zO3ZzEJIU0aPLXczrz4hnn-5YVHjpxZ-52sEUjYa_WGaIIjh3-xHqzqBQh9ZyzR0fpmJSpYet0yRYJ6QCKUN2D9OZua_sQFZBQTg67m2CSKynPJj_J3TB6axtKCqB3Q6TYvC-5nwWcWrRlAdKynrbAAAAAF41aRLAA")
STRING_SESSION2 = getenv("STRING_SESSION2", "BQADMVMAM4rq0vi9Ae62oF7T5JsDFc0G8iseHWJQU1xqHM1MMBFgs_adyj9jrzud9H1MSm7SNW72AHt1yhmBrcxzxe56rkOMtwIm9YQdyS3ti4Hb7f_H_VqS_kSG7CFJtSj5ri6AjAwdvIlm0seTAw2_KlTmc7apsmsgg3rQUnUK3oxZoQ5Y9GY79gBviRTVXI_TuMYlJl9JGRXPHcFt-nDGUIzlAujgr3bgvdbG1_BtcA1Qb200OcHjWsdOFD07QlGlgJpOVF_tVvZlfxD12jSNQqAcrZIrHsCHDNhIo0LaQiqg64sAPLwCsgwtJIjkvbQXL896xpY56DD7Z7EYb7optgzy1gAAAAFw3mctAA")
STRING_SESSION3 = getenv("STRING_SESSION3", "")
STRING_SESSION4 = getenv("STRING_SESSION4", "")
STRING_SESSION5 = getenv("STRING_SESSION5", "")
STRING_SESSION6 = getenv("STRING_SESSION6", "")
STRING_SESSION7 = getenv("STRING_SESSION7", "")
STRING_SESSION8 = getenv("STRING_SESSION8", "")
STRING_SESSION9 = getenv("STRING_SESSION9", "")
STRING_SESSION10 = getenv("STRING_SESSION10", "")
STRING_SESSION11 = getenv("STRING_SESSION11", "")
STRING_SESSION12 = getenv("STRING_SESSION12", "")
STRING_SESSION13 = getenv("STRING_SESSION13", "")
STRING_SESSION14 = getenv("STRING_SESSION14", "")
STRING_SESSION15 = getenv("STRING_SESSION15", "")



