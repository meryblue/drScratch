#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.contrib import admin
from app.models import Project, Attribute, Sprite, Mastery, Dead, Dashboard, Duplicate

admin.site.register(Project)
admin.site.register(Dashboard)
admin.site.register(Attribute)
admin.site.register(Dead)
admin.site.register(Sprite)
admin.site.register(Mastery)
admin.site.register(Duplicate)
