import opps.admin
from opps.admin import views
from models import UserSettings
from opps.admin.layout import *


class UserSettingsAdmin(object):
    model_icon = 'cog'
opps.admin.site.register(UserSettings, UserSettingsAdmin)
