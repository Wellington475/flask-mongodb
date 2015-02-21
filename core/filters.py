# -*- coding: utf8 -*-
import datetime

def Filters(app):
    @app.template_filter('datetime')
    def _jinja2_filter_datetime(date):
            return date.strftime('%d/%m/%Y ás %Hh%Mm').decode('utf8')