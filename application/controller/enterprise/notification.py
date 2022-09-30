from flask import render_template, redirect, url_for
from application.models.user import User
from application.models.notification import Notification
from application.models.e2u import E2U
from application.models.enterprise import Enterprise
from application.helper.check_session import get_type_session
from flask_login import current_user
from loguru import logger

def notification_get(session):
    if current_user.is_authenticated:
        if session['type'] == 2:
            id_user = current_user.get_id()
            list_notification = Notification.query.filter_by(id_receiver = id_user)
            
            return render_template("admin/notification.html", list_notification = list_notification)
        else:
            return redirect(url_for("index"))
    else:
        return redirect(url_for("index"))

def notification_post(session, request):
    pass