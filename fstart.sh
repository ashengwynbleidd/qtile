#!/bin/sh

# starting compositor
picom &

# setting wallpaper
[ -d ~/.config/qtile/wallpapers ] && \
    xwallpaper --zoom ~/.config/qtile/wallpapers/art_disco-elysium_1.jpg
