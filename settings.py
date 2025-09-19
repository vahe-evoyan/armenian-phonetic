# -*- coding: utf-8 -*-
"""
DMG build settings for Armenian Phonetic keyboard layouts.
Converted from appdmg.json configuration.
"""

# Volume name (title in appdmg.json)
volume_name = "Armenian Phonetic"

# Volume icon
icon = "ArmenianPhonetic.bundle/Contents/Resources/Armenian Phonetic.icns"

# Background image
background = "resources/background.png"

# Files to include
files = ["ArmenianPhonetic.bundle"]

# Symlinks to create
symlinks = {
    "Keyboard Layouts": "/Library/Keyboard Layouts"
}

# Icon positions (x, y coordinates from appdmg.json)
icon_locations = {
    "ArmenianPhonetic.bundle": (180, 230),
    "Keyboard Layouts": (520, 230),
}

# Window size (from appdmg.json window.size)
window_rect = ((100, 100), (700, 466))

# DMG format (UDZO is compressed, UDRO is read-only uncompressed)
format = "UDZO"

# Hide file extensions
hide_extensions = ['ArmenianPhonetic.bundle']

# Show icon preview
show_icon_preview = False

# Include all files (don't skip hidden files)
include_icon_view_settings = True

# Icon view settings
icon_view_settings = {
    'iconSize': 100,
    'gridOffset': (0, 0),
    'gridSpacing': 100,
    'scrollPosition': (0, 0),
    'labelOnBottom': True,
    'showItemInfo': False,
    'showIconPreview': False,
    'arrangeBy': None,
}

# Window view settings
default_view = 'icon-view'
show_status_bar = False
show_tab_view = False
show_toolbar = False
show_pathbar = False
show_sidebar = False
sidebar_width = 180

# Background settings
background_color = None  # Use background image instead
