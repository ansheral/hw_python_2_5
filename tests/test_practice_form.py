import os
from pathlib import Path
from selene.support.shared import browser
from selene import command, have, by
from selene.support.shared.jquery_style import ss

def given_opened_form():
    browser.open('/automation-practice-form')
