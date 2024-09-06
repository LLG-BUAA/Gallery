from nicegui import ui

# 创建全屏容器，大小合适浏览器高度 (h-dvh)
with ui.element('div').style('width: 100%; height: 100dvh'):
    # 上方 div 充满上方空间
    with ui.element('div').style('height: calc(100dvh - 4rem); background-color: lightblue'):
        with ui.card().tight():
            ui.image('https://picsum.photos/id/684/640/360')
            with ui.card_section():
                ui.label('Lorem ipsum dolor sit amet, consectetur adipiscing elit, ...')

    # 下方 div 高度为 h-16，贴靠最下方
    with ui.element('div').style('height: 4rem; position: absolute; bottom: 0; width: 100%').classes('flex items-center justify-center'):
        with ui.row().classes('q-pa-lg flex justify-center'):
            ui.pagination(1, 5).props('boundary-links gutter="20px"')

ui.run()
