from flask import Blueprint, render_template, flash, current_app

import requests

user_view = Blueprint('user', __name__, template_folder='templates')

@user_view.route('/users/')
def users():
    user_uri = current_app.config.get("USERS_API_ENDPOINT")
    users = requests.get(user_uri).json()
    return render_template('users.html', users=users, delmiter='---'*10)


@user_view.route('/users/<int:user_id>')
def user_profile(user_id):
    user_uri = current_app.config.get("USERS_API_ENDPOINT")
    user = requests.get(user_uri + str(user_id)).json()

    if not user:
        flash("No Data available at " + request.full_path)
        return redirect(url_for('users'))

    return render_template('profile.html', user=user)