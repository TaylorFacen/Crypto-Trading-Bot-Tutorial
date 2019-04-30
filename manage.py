# Contains all scheduled tasks

from flask_script import Manager

from app import app
from deposit_funds import deposit_funds

manager = Manager(app)

@manager.command
def make_deposit():
    deposit_funds()