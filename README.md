Chroma color themes
===================

various color themes derived from my vim theme (also linked in here).

# Base colors for all themes

| Color name  | RGB-Hex | Term | Foreground preview         | Background preview                                                    |
|-------------|---------|------|----------------------------|-----------------------------------------------------------------------|
| blue        | #00afff |   39 | ![#00afff](doc/00afff.png) | ![#00afff](doc/00afff-bg-dark.png)![#00afff](doc/00afff-bg-light.png) |
| lightblue   | #87afff |  111 | ![#87afff](doc/87afff.png) | ![#87afff](doc/87afff-bg-dark.png)![#87afff](doc/87afff-bg-light.png) |
| orange      | #ffaf5f |  215 | ![#ffaf5f](doc/ffaf5f.png) | ![#ffaf5f](doc/ffaf5f-bg-dark.png)![#ffaf5f](doc/ffaf5f-bg-light.png) |
| yellow      | #ffd75f |  221 | ![#ffd75f](doc/ffd75f.png) | ![#ffd75f](doc/ffd75f-bg-dark.png)![#ffd75f](doc/ffd75f-bg-light.png) |
| green       | #87d75f |  113 | ![#87d75f](doc/87d75f.png) | ![#87d75f](doc/87d75f-bg-dark.png)![#87d75f](doc/87d75f-bg-light.png) |
| red         | #ff0000 |  196 | ![#ff0000](doc/ff0000.png) | ![#ff0000](doc/ff0000-bg-dark.png)![#ff0000](doc/ff0000-bg-light.png) |
| lightred    | #ff5f5f |  203 | ![#ff5f5f](doc/ff5f5f.png) | ![#ff5f5f](doc/ff5f5f-bg-dark.png)![#ff5f5f](doc/ff5f5f-bg-light.png) |
| white       | #ffffff |  255 | ![#ffffff](doc/ffffff.png) | ![#ffffff](doc/ffffff-bg-dark.png)![#ffffff](doc/ffffff-bg-light.png) |
| lightgray   | #c6c6c6 |  251 | ![#c6c6c6](doc/c6c6c6.png) | ![#c6c6c6](doc/c6c6c6-bg-dark.png)![#c6c6c6](doc/c6c6c6-bg-light.png) |
| gray        | #8a8a8a |  244 | ![#8a8a8a](doc/8a8a8a.png) | ![#8a8a8a](doc/8a8a8a-bg-dark.png)![#8a8a8a](doc/8a8a8a-bg-light.png) |
| bggray      | #1c1c1c |  234 | ![#1c1c1c](doc/1c1c1c.png) | ![#1c1c1c](doc/1c1c1c-bg-dark.png)![#1c1c1c](doc/1c1c1c-bg-light.png) |
| lightbggray | #262626 |  235 | ![#262626](doc/262626.png) | ![#262626](doc/262626-bg-dark.png)![#262626](doc/262626-bg-light.png) |
| visualgray  | #303030 |  236 | ![#303030](doc/303030.png) | ![#303030](doc/303030-bg-dark.png)![#303030](doc/303030-bg-light.png) |
| black       | #000000 |    0 | ![#000000](doc/000000.png) | ![#000000](doc/000000-bg-dark.png)![#000000](doc/000000-bg-light.png) |

# Usage

## dmenu / urxvt

copy the lines from the `Xresources` file in the corresponding folder to your
own `.Xresources` or `.Xdefaults`

## intellij

Import via "Editor > Color Scheme > little gear icon > Import Scheme"

## (neo)mutt

Put the file somewhere and add `source <path to theme file>` in your muttrc or
neomuttrc

## (neo)vim

Copy `chroma.vim` to your `colors` dir or use your favorite plugin manager. The
vim theme is in a separate repo, so most plugin managers can clone that directly

## qutebrowser (>= 1.1.0)

Add `config.source('chroma.py')` to your `config.py`

## tmux

Add the lines from the file to your `tmux.conf`

The tmux theme includes different formatting for the status line. If you don't
want that, the comment at the top contains all color codes used.

## weechat

Add the lines to `weechat.conf`, replacing any existing `[palette]` or `[color]`
sections.
