#!/bin/zsh
echo "| Color name  | RGB-Hex | Term | Foreground preview         | Background preview                                                    |"
echo "|-------------|---------|------|----------------------------|-----------------------------------------------------------------------|"
for name hex term in $(<<COLORS
	blue        00afff    39
	lightblue   87afff   111
	orange      ffaf5f   215
	yellow      ffd75f   221
	green       87d75f   113
	red         ff0000   196
	lightred    ff5f5f   203
	white       ffffff   255
	lightgray   c6c6c6   251
	gray        8a8a8a   244
	bggray      1c1c1c   234
	lightbggray 262626   235
	visualgray  303030   236
	black       000000     0
COLORS
); do
	if [[ ! -e $hex.png ]]; then
		convert -background black -fill $hex -font Menlo-Regular-for-Powerline -size 80x30 -gravity Center -pointsize 14 label:example $hex.png >&2
	fi
	if [[ ! -e $hex-bg-dark.png ]]; then
		convert -background $hex -fill black -font Menlo-Regular-for-Powerline -size 80x30 -gravity Center -pointsize 14 label:example $hex-bg-dark.png >&2
	fi
	if [[ ! -e $hex-bg-light.png ]]; then
		convert -background $hex -fill white -font Menlo-Regular-for-Powerline -size 80x30 -gravity Center -pointsize 14 label:example $hex-bg-light.png >&2
	fi
	printf '| %-11s | #%s |  %3s | ![#%2$s](doc/%2$s.png) | ![#%2$s](doc/%2$s-bg-dark.png)![#%2$s](doc/%2$s-bg-light.png) |\n' $name $hex $term
done
