import time
from datetime import datetime
# import heroku3

from config import Config

FIRST_A_APIKEY = Config.FIRST_A_APIKEY
FIRST_A_APPNAME = Config.FIRST_A_APPNAME
FIRST_B_APPNAME = Config.FIRST_B_APPNAME
FIRST_B_APIKEY = Config.FIRST_B_APIKEY
FIRST_PROCESSTYPE = Config.FIRST_PROCESSTYPE

print(FIRST_A_APIKEY, FIRST_A_APPNAME, FIRST_B_APPNAME,
      FIRST_B_APIKEY, FIRST_PROCESSTYPE)
# while True:
#     today = datetime.now()
#     print("[#1] Checking the conditions for the first app..")
#     if len(FIRST_PROCESSTYPE) == 0 or len(FIRST_A_APIKEY) == 0 or len(
#         FIRST_A_APPNAME) == 0 or len(FIRST_B_APIKEY) == 0 or len(
#             FIRST_B_APPNAME) == 0:
#         print("Variables for the first app are not fully filled.")
#     elif (today.day == 15):
#         print("Changing the dyno to the second acc..")
#         heroku_conn = heroku3.from_key(FIRST_A_APIKEY)
#         app = heroku_conn.app(FIRST_A_APPNAME)
#         app.process_formation()[FIRST_PROCESSTYPE].scale(0)
#         print("The first app in the first acc has been scaled down.")
#         time.sleep(5)
#         heroku_conn = heroku3.from_key(FIRST_B_APIKEY)
#         app = heroku_conn.app(FIRST_B_APPNAME)
#         app.process_formation()[FIRST_PROCESSTYPE].scale(1)
#         print("The first app in the second acc has been scaled up.")
#         print("Your first app has been shifted to the second acc.")
#     elif(today.day == 10):
#         print("Changing the dyno to the first acc..")
#         heroku_conn = heroku3.from_key(FIRST_B_APIKEY)
#         app = heroku_conn.app(FIRST_B_APPNAME)
#         app.process_formation()[FIRST_PROCESSTYPE].scale(0)
#         print("The first app in the second acc has been scaled down.")
#         time.sleep(5)
#         heroku_conn = heroku3.from_key(FIRST_A_APIKEY)
#         app = heroku_conn.app(FIRST_A_APPNAME)
#         app.process_formation()[FIRST_PROCESSTYPE].scale(1)
#         print("The first app in the first acc has been scaled up.")
#         print("Your first app has been shifted to the first acc.")
#     else:
#         print("Today is not 1st or 15nd.")
