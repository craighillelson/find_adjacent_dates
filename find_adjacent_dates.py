"""
Prompt user for to pick a day of the week.
Based on the day selected, return the dates for that day in the immediately
preceding week and the next occurrance of that day.
"""

from datetime import (date,
                      datetime)
import pyinputplus as pyip
from dateutil.relativedelta import (relativedelta,
                                    MO,
                                    TU,
                                    WE,
                                    TH,
                                    FR,
                                    SA,
                                    SU)


def next_selected_day(int_1, selected_day):
    """Find the date for the next occurrance of the selected day."""

    datetime_obj = TODAY + relativedelta(days=1,
                                         weekday=selected_day_abbrev(+int_1))
    print(f"Next {selected_day}: {datetime_obj.date()}\n")


def last_selected_day(int_1, selected_day):
    """Find the date for the last occurrance of the selected day."""

    datetime_obj = TODAY + relativedelta(weekday=selected_day_abbrev(int_1))
    print(f"\nLast {selected_day}: {datetime_obj.date()}")


options_map = {
    1: ["Monday", MO,],
    2: ["Tuesday", TU,],
    3: ["Wednesday", WE,],
    4: ["Thursday", TH,],
    5: ["Friday", FR,],
    6: ["Saturday", SA,],
    7: ["Sunday", SU,]
}

NUM_OPTIONS = len(options_map)

print("\nPlease select from an option below.")
for num, options in options_map.items():
    print(num, options[0])
response = pyip.inputInt("> ", min=1, max=NUM_OPTIONS)
if response <= NUM_OPTIONS:
    user_selected_day = options_map[response][0]
    selected_day_abbrev = options_map[response][1]
else:
    pass

day_index = response - 1
TODAY = datetime.now()
if date.today().weekday() == day_index:
    print(f"\nYou selected {user_selected_day}. Today is {user_selected_day}.")
    last_selected_day(-2, user_selected_day)
else:
    print(f"\nYou selected {user_selected_day}.")
    last_selected_day(-1, user_selected_day)

next_selected_day(1, user_selected_day)
