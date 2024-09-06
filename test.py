from nicegui import ui

# 定义选项卡
tabs = ui.tabs().classes('w-full bg-primary text-white shadow-2').props('v-model="tab" inline-label switch-indicator indicator-color="primary"')
tab_panels = ui.tab_panels(tabs=tabs).classes('w-full')

# 添加选项卡
with tabs:
    one = ui.tab('One')
    two = ui.tab('Two')
    three = ui.tab('Three')
    four = ui.tab('Four')
    five = ui.tab('Five')
    six = ui.tab('Six')
    seven = ui.tab('Seven')
    eight = ui.tab('Eight')
    nine = ui.tab('Nine')
    ten = ui.tab('Ten')


# 添加对应的选项卡面板
with tab_panels:
    with ui.tab_panel(one):
        ui.image('https://picsum.photos/id/377/640/360')
    with ui.tab_panel(two):
        ui.image('https://picsum.photos/id/377/640/360')
    with ui.tab_panel(three):
        ui.image('https://picsum.photos/id/377/640/360')
    with ui.tab_panel(five):
        ui.image('https://picsum.photos/id/377/640/360')

ui.run()
