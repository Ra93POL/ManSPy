import time
import os
import sys
import os.path

tg_path = os.path.normpath(os.path.join(os.path.basename(__file__), '../../telegram/'))
sys.path.append(tg_path)
print(tg_path)

import telegram

passwords = None

class Interface():
    def __init__(self, API, settings):
        self.API = API
        self.settings = settings(read_text=self.read_text)

    def FromUser(self, m, comm_name, args, text):
        w_text = text
        from_user = m['chat_id']

        if w_text == None:
            return
        if w_text:
            self.API.write_text(w_text, self.settings, {'any_data': from_user})

    def read_text(self, r_text, from_user):
        print(r_text, from_user)
        if from_user:
            self.tg.send_message(from_user, r_text)

    def init(self):
        self.tg = telegram.TelegramBot(passwords['token'])

        commands = {
        }

        self.tg.run(commands, self.FromUser)
