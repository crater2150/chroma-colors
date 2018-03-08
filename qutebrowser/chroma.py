# define theme base colors
chroma = {
        'blue':        '#00afff',
        'lightblue':   '#87afff',
        'orange':      '#ffaf5f',
        'yellow':      '#ffd75f',
        'green':       '#87d75f',
        'red':         '#ff0000',
        'lightred':    '#ff5f5f',
        'white':       '#ffffff',
        'lightgray':   '#c6c6c6',
        'gray':        '#8a8a8a',
        'bggray':      '#1c1c1c',
        'lightbggray': '#262626',
        'visualgray':  '#303030',
        'black':       '#000000',
        'purple':      '#9500ff'
}

## Completion colors
c.colors.completion.category.fg = chroma['lightblue']
c.colors.completion.category.bg = chroma['visualgray']
c.colors.completion.category.border.bottom = chroma['lightblue']
c.colors.completion.category.border.top = chroma['black']
c.colors.completion.even.bg = chroma['bggray']
c.colors.completion.odd.bg = chroma['lightbggray']
c.colors.completion.fg = chroma['white']
c.colors.completion.item.selected.bg = chroma['blue']
c.colors.completion.item.selected.border.bottom = chroma['lightblue']
c.colors.completion.item.selected.border.top = chroma['lightblue']
c.colors.completion.item.selected.fg = chroma['white']
c.colors.completion.match.fg = chroma['lightblue']
c.colors.completion.scrollbar.bg = chroma['bggray']
c.colors.completion.scrollbar.fg = chroma['visualgray']

## download bar colors
c.colors.downloads.bar.bg = 'black'
c.colors.downloads.error.bg = 'red'
c.colors.downloads.error.fg = 'white'

# Color gradients for downloads
c.colors.downloads.start.bg = chroma['blue']
c.colors.downloads.stop.bg = chroma['green']
c.colors.downloads.start.fg = chroma['black']
c.colors.downloads.stop.fg = chroma['black']

c.colors.downloads.system.bg = 'hsv'
c.colors.downloads.system.fg = 'hsv'

# Background color for hints. Note that you can use a `rgba(...)` value
# for transparency.
# Type: QssColor
c.colors.hints.bg = 'qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgba(255, 247, 133, 0.8), stop:1 rgba(255, 197, 66, 0.8))'
c.colors.hints.fg = 'black'
c.colors.hints.match.fg = 'green'
c.colors.keyhint.bg = 'rgba(0, 0, 0, 80%)'
c.colors.keyhint.fg = '#FFFFFF'
c.colors.keyhint.suffix.fg = '#FFFF00'

c.colors.messages.error.bg = chroma['red']
c.colors.messages.error.border = chroma['lightred']
c.colors.messages.error.fg = chroma['white']

c.colors.messages.info.bg = chroma['bggray']
c.colors.messages.info.border = chroma['lightblue']
c.colors.messages.info.fg = chroma['white']

c.colors.messages.warning.bg = chroma['orange']
c.colors.messages.warning.border = chroma['yellow']
c.colors.messages.warning.fg = chroma['black']

c.colors.prompts.bg = chroma['bggray']
c.colors.prompts.fg = 'white'
c.colors.prompts.border = '1px solid ' + chroma['black']
c.colors.prompts.selected.bg = chroma['blue']

c.colors.statusbar.caret.bg = chroma['purple']
c.colors.statusbar.caret.fg = chroma['white']
c.colors.statusbar.caret.selection.bg = chroma['visualgray']
c.colors.statusbar.caret.selection.fg = chroma['white']

c.colors.statusbar.command.bg = chroma['black']
c.colors.statusbar.command.fg = chroma['white']

c.colors.statusbar.command.private.bg = chroma['bggray']
c.colors.statusbar.command.private.fg = chroma['white']
c.colors.statusbar.private.bg = chroma['bggray']
c.colors.statusbar.private.fg = chroma['white']
c.colors.statusbar.insert.bg = chroma['green']
c.colors.statusbar.insert.fg = chroma['black']
c.colors.statusbar.passthrough.bg = chroma['blue']
c.colors.statusbar.passthrough.fg = chroma['black']

c.colors.statusbar.normal.bg = chroma['black']
c.colors.statusbar.normal.fg = chroma['white']

c.colors.statusbar.progress.bg = chroma['white']

c.colors.statusbar.url.fg = chroma['lightblue']
c.colors.statusbar.url.hover.fg = chroma['yellow']
c.colors.statusbar.url.success.http.fg = chroma['lightblue']
c.colors.statusbar.url.success.https.fg = chroma['green']
c.colors.statusbar.url.warn.fg = chroma['orange']
c.colors.statusbar.url.error.fg = chroma['lightred']

c.colors.tabs.bar.bg = chroma['black']

c.colors.tabs.even.bg = chroma['visualgray']
c.colors.tabs.even.fg = chroma['lightgray']

c.colors.tabs.odd.bg = chroma['bggray']
c.colors.tabs.odd.fg = chroma['lightgray']

c.colors.tabs.indicator.error = chroma['red']
c.colors.tabs.indicator.start = chroma['blue']
c.colors.tabs.indicator.stop = chroma['green']
c.colors.tabs.indicator.system = 'hsv'

c.colors.tabs.selected.even.bg = chroma['black']
c.colors.tabs.selected.even.fg = chroma['orange']
c.colors.tabs.selected.odd.bg = chroma['black']
c.colors.tabs.selected.odd.fg = chroma['orange']
