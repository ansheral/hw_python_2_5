import os
from pathlib import Path
from selene.support.shared import browser
from selene import command, have, by
from selene.support.shared.jquery_style import ss

from tests.test_data import users


def given_opened_form():
    browser.open('/automation-practice-form')


def test_verify_form():
    name = users.ana['name']
    last_name = users.ana['surname']
    email = users.ana['email']
    user_number = users.ana['phone']
    birth_day, birth_month, birth_year = users.ana['b_day'].split(' ')
    subjects = users.ana['subjects']
    current_address = users.ana['state_and_city']

    picture = users.ana['prof_picture']
