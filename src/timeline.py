# 3) Timescale Dropdown
#  - Yearly
#  - Quarterly
#  - Monthly
#  - Bi-Weekly
#  - Weekly

# Using the flet GUI library in python to create a dropdown menu for the timescale of the timeline that breaks down the timeline into Yearly, Quarterly, Monthly, Bi-Weekly, and Weekly intervals.

# Example 


import logging
import os

import flet

from flet import Dropdown, ElevatedButton, dropdown
from flet import (
    Column,
    FloatingActionButton,
    Icon,
    NavigationRail,
    NavigationRailDestination,
    Page,
    Row,
    Text,
    VerticalDivider,
    icons,
)


logging.basicConfig(level=logging.INFO)

def main(page: flet.Page):
# Create a dropdown menu with the following options

    def dropdown_changed(e):
        t.value = f"Dropdown changed to {timescale_dropdown.value}"
        page.update()


    t = flet.Text()
    timescale_dropdown = flet.Dropdown(
        #selected_index=0,
        on_change=dropdown_changed,
        #label_type="all",
        # extended=True,
        width=200,
        
        #height= 50,
        
        #min_width=100,
        #min_extended_width=400,
        options=[
            flet.dropdown.Option("Y","Yearly"),
            flet.dropdown.Option("Q", "Quarterly"),
            flet.dropdown.Option("M", "Monthly"),
            flet.dropdown.Option("B", "Bi-Weekly"),
            flet.dropdown.Option("W", "Weekly"),
        ],
    #on_change=lambda e: print("Selected destination:", e.control.selected_index),
    )

# Display the dropdown menu
    page.add(timescale_dropdown, t)

flet.app(target=main)





# def main(page: Page):

#     rail = NavigationRail(
#         selected_index=0,
#         label_type="all",
#         # extended=True,
#         min_width=100,
#         min_extended_width=400,
#         leading=FloatingActionButton(icon=icons.CREATE, text="Add"),
#         group_alignment=-0.9,
#         destinations=[
#             NavigationRailDestination(
#                 icon=icons.FAVORITE_BORDER, selected_icon=icons.FAVORITE, label="First"
#             ),
#             NavigationRailDestination(
#                 icon_content=Icon(icons.BOOKMARK_BORDER),
#                 selected_icon_content=Icon(icons.BOOKMARK),
#                 label="Second",
#             ),
#             NavigationRailDestination(
#                 icon=icons.SETTINGS_OUTLINED,
#                 selected_icon_content=Icon(icons.SETTINGS),
#                 label_content=Text("Settings"),
#             ),
#         ],
#         on_change=lambda e: print("Selected destination:", e.control.selected_index),
#     )

#     page.add(
#         Row(
#             [
#                 rail,
#                 VerticalDivider(width=1),
#                 Column([Text("Body!")], alignment="start", expand=True),
#             ],
#             expand=True,
#         )
#     )


# flet.app(target=main)