#!/usr/bin/env python3
from nicegui import ui

## with ui.header().classes(replace='row items-center') as header:
##     ui.label('Footer')

with ui.footer(value=False).classes('bg-primary text-white flex items-center').style('padding-top: 0px; padding-bottom: 0px;') as footer:
    ui.button(on_click=lambda: left_drawer.toggle(), icon='menu').props('flat color=white').classes('h-full')
    with ui.tabs().props('v-model="tab" inline-label switch-indicator') as tabs:
        ui.tab('A')
        ui.tab('B')
        ui.tab('C')

with ui.left_drawer().classes('bg-blue-100') as left_drawer:
    ui.label('Side menu')

## with ui.page_sticky(position='bottom-right', x_offset=20, y_offset=20):
##     ui.button(on_click=footer.toggle, icon='contact_support').props('fab')

with ui.element('q-page-sticky').props('position="bottom-right" x-offset="5" y-offset="5"'):
    ui.element('q-fab').props('square; direction="up" padding="none xl" icon="keyboard_arrow_up" label="Actions" color="primary"').on('click', footer.toggle).style('border-radius: 5px 5px 0 0')
    ## ui.button(on_click=footer.toggle).props('fab') ##, icon='contact_support'

with ui.tab_panels(tabs, value='A').classes('w-full'):
    with ui.tab_panel('A'):
        ui.label('Content of A')
    with ui.tab_panel('B'):
        ui.label('Content of B')
    with ui.tab_panel('C'):
        ui.label('Content of C')

ui.run()