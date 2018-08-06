# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Parpol
from .models import Person
from .models import President
from .models import WakilPresident
from .models import Terpilih


admin.site.register(Person)
admin.site.register(Parpol)
admin.site.register(President)
admin.site.register(WakilPresident)
admin.site.register(Terpilih)

# Register your models here.
