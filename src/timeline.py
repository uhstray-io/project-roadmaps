# 3) Timescale Dropdown
#  - Yearly
#  - Quarterly
#  - Monthly
#  - Bi-Weekly
#  - Weekly

# Using the flet GUI library in python to create a dropdown menu for the timescale of the timeline that breaks down the timeline into Yearly, Quarterly, Monthly, Bi-Weekly, and Weekly intervals.

# Example 
""" import logging
import os

import flet
from flet import Dropdown, ElevatedButton, dropdown

logging.basicConfig(level=logging.INFO)


def main(page):
    dd = Dropdown(
        options=[
            dropdown.Option("a", "Item A"),
            dropdown.Option("b", "Item B"),
            dropdown.Option("c", "Item C"),
        ]
    )

    def btn2_click(e):
        dd.options.append(dropdown.Option("d", "Item D"))
        page.update()

    def btn3_click(e):
        dd.options[1].text = "Item Blah Blah Blah"
        page.update()

    btn2 = ElevatedButton("Add new item!", on_click=btn2_click)
    btn3 = ElevatedButton("Change second item", on_click=btn3_click)

    page.add(dd, btn2, btn3)


flet.app(target=main) """

import logging
import os

import flet

from flet import Dropdown, ElevatedButton, dropdown

logging.basicConfig(level=logging.INFO)

def main(page):
# Create a dropdown menu with the following options
    timescale_dropdown = Dropdown(
        options=[
            dropdown.Option("Y", "Yearly"),
            dropdown.Option("Q", "Quarterly"),
            dropdown.Option("M", "Monthly"),
            dropdown.Option("B", "Bi-Weekly"),
            dropdown.Option("W", "Weekly"),
        ]
    )

# Display the dropdown menu
    page.add(timescale_dropdown)

flet.app(target=main)