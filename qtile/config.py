# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import os
import subprocess
from libqtile.config import Key, Screen, Group, Drag, Click
from libqtile.command import lazy
from libqtile import layout, bar, widget
from libqtile import hook

try:
    from typing import List  # noqa: F401
except ImportError:
    pass

mod = "mod4"
terminal = "alacritty"
colors = {
    'black1': '#000000',
    'black2': '#515151',
    'white1': '#ffffff',
    'white2': '#cccccc',
    'cyan': '#3e83d8',
    'blue': '#7f70e7',
    'magenta': '#9f65ed'
}

keys = [
    # general shortcuts
    Key([mod], "b", lazy.spawn("brave")),
    
    # Switch between windows in current stack pane
    Key([mod], "k", lazy.layout.down()),
    Key([mod], "j", lazy.layout.up()),

    # Change size of window
    Key([mod], "h", lazy.layout.shrink_main()),
    Key([mod], "l", lazy.layout.grow_main()),

    # Move windows up or down in current stack
    Key([mod, "control"], "k", lazy.layout.shuffle_down()),
    Key([mod, "control"], "j", lazy.layout.shuffle_up()),

    # Switch window focus to other pane(s) of stack
    Key([mod], "space", lazy.layout.next()),

    # Swap panes of split stack
    Key([mod, "shift"], "space", lazy.layout.rotate()),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key([mod, "shift"], "Return", lazy.layout.toggle_split()),
    Key([mod], "Return", lazy.spawn(terminal)),

    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout()),
    Key([mod], "w", lazy.window.kill()),

    Key([mod, "control"], "r", lazy.restart()),
    Key([mod, "control"], "q", lazy.shutdown()),
   #  Key([mod], "r", lazy.spawncmd()),

    # Change the volume from keyboard
#    Key(
#        [], "XF86AudioRaiseVolume",
#        lazy.spawn("amixer -c 0 -q set Master 2dB+")
#    ),
#    Key(
#        [], "XF86AudioLowerVolume",
#        lazy.spawn("amixer -c 0 -q set Master 2dB-")
#    ),
#    Key(
#        [], "XF86AudioMute",
#        lazy.spawn("amixer -q set Master toggle")
#    ),
#    
#    #change brightness
#    Key([], "XF86MonBrightnessDown", lazy.spawn("light -U 5")),
#    Key([], "XF86MonBrightnessUp", lazy.spawn("light -A 5")),
#

    ###change volume with notification
    Key(
        [], "XF86AudioRaiseVolume",
        lazy.spawn("sh /home/biraj/scripts/volumeControl.sh up")
    ),
    Key(
        [], "XF86AudioLowerVolume",
        lazy.spawn("sh /home/biraj/scripts/volumeControl.sh down")
    ),
    # toggle sound
    Key(
        [], "XF86AudioMute",
        lazy.spawn("sh /home/biraj/scripts/volumeControl.sh mute")
    ),
    ###change brightness with notification
    Key(
        [], "XF86MonBrightnessDown",
        lazy.spawn("sh /home/biraj/scripts/brightnessControl.sh down")
    ),
    Key(
        [], "XF86MonBrightnessUp",
        lazy.spawn("sh /home/biraj/scripts/brightnessControl.sh up")
    ),
    
    ### Dmenu Run Launcher
    Key(
        [mod, "control"], "Return",
        lazy.spawn("dmenu_run -fn 'UbuntuMono Nerd Font:size=10' -nb '#282a36' -nf '#ffffff' -sb '#bd93f9' -sf '#282a36' -p 'dmenu:'")
    ),

    ###open telegram
    Key([mod],"t", lazy.spawn("telegram-desktop")),
    ###open ranger
    Key([mod],"f", lazy.spawn(terminal + " -e ranger")),
    ###focus to screen(0)
    Key([mod],"q", lazy.to_screen(0)),
    ###focus to screen(1)
    Key([mod],"e", lazy.to_screen(1)),
    ###betterlockscreen
    Key([mod],"p", lazy.spawn(terminal + " -e betterlockscreen -l blur")),

]

#groups = [Group(i) for i in "12345"]
#for i in groups:
#    keys.extend([
#        # mod1 + letter of group = switch to group
#        Key([mod], i.name, lazy.group[i.name].toscreen()),
#
#        # mod1 + shift + letter of group = switch to & move focused window to group
#        Key([mod, "shift"], i.name, lazy.window.togroup(i.name)),
#    ])

def init_group_names():
    return [(" ", {'layout': 'monadtall'}),
            (" ", {'layout': 'monadtall'}),
            (" ", {'layout': 'monadtall'}),
            (" ", {'layout': 'monadtall'}),
            (" ", {'layout': 'monadtall'}),
            (" ", {'layout': 'monadtall'}),
            (" ", {'layout': 'monadtall'}),
            (" ", {'layout': 'monadtall'}),
            (" ", {'layout': 'monadtall'}),
           ]

def init_groups():
    return [Group(name, **kwargs) for name, kwargs in group_names]

if __name__ in ["config", "__main__"]:
    group_names = init_group_names()
    groups = init_groups()

##### SETS GROUPS KEYBINDINGS #####

for i, (name, kwargs) in enumerate(group_names, 1):
    keys.append(Key([mod], str(i), lazy.group[name].toscreen()))          # Switch to another group
    keys.append(Key([mod, "shift"], str(i), lazy.window.togroup(name)))   # Send current window to another group

layouts = [
    layout.MonadTall(
        border_focus=colors['white1'],
        border_normal=colors['black1'],
        border_width=1,
        margin=10
    )
]

widget_defaults = dict(
    font='sans',
    fontsize=14,
    padding=4,
    background="#2e3440",
    foreground="#5e81ac",
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.GroupBox(
                    active = "#5e81ac",
                    inactive = "#b48ead",
                    this_current_screen_border = "#bf616a",
                    highlight_method = "line",
                    highlight_color=["#2e3440", "#2e3440"],
                    center_aligned=True,
                ),

                #widget.Prompt(
                #    prompt='Run:',
                #),
    
                widget.Spacer(bar.STRETCH),
                widget.TextBox(
                    text='|',
                    foreground="#5e81ac",
                ),
                widget.Battery(
                    format = '{percent:2.0%}'
                ),
                #widget.TextBox(
                #    text='|',
                #    foreground="#ebcb8b",
                #),
                #widget.TextBox(
                #    text=' ',
                #    foreground="#ebcb8b",
                #),
                #widget.Volume(
                #    foreground="#ebcb8b",
                #),
                #widget.TextBox(
                #    text='|',
                #    foreground="#88c0d0",
                #),
                #widget.TextBox(
                #    text='',
                #    foreground="#88c0d0",
                #),
                #widget.Backlight(
                #    foreground="#88c0d0",
                #    backlight_name="intel_backlight",
                #),
                widget.TextBox(
                    text='|',
                    foreground="#88c0d0",
                ),
                widget.TextBox(
                    text=' ',
                    foreground="#a3be8c",
                ),
                widget.Clock(
                    format='%a %I:%M',
                    foreground = "#a3be8c",
                ),
                widget.TextBox(
                    text='|',
                    foreground="#bf6a6a",
                ),
                widget.TextBox(
                    text=' ',
                    foreground="#bf6a6a",
                ),
                widget.Clock(
                    foreground = "#bf6a6a",
                    format="%B %d"
                ),
                widget.TextBox(
                    text='|',
                    foreground="#1995ad",
                ),
                widget.TextBox(
                    text=' ',
                    foreground="#1995ad",
                ),
                widget.Wlan(
                    foreground="#1995ad",
                    interface="wlo1",
                    format="{essid}",
                    disconnected_message='Disconnected',
                ),
                widget.Net(
                    foreground="#1995ad",
                    interface="wlo1",
                ),
                widget.Systray(),
            ],
            26,
            background="#2e3440"
        ),
    ),

    Screen(
        top=bar.Bar(
            [
                widget.GroupBox(
                    active = "#5e81ac",
                    inactive = "#b48ead",
                    this_current_screen_border = "#bf616a",
                    highlight_method = "line",
                    highlight_color=["#2e3440", "#2e3440"],
                    center_aligned=True,
                ),
                widget.Spacer(bar.STRETCH),
                widget.Systray(),
            ],
            26,
            background="#2e3440"
        ),
    ),
]



# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
main = None
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(float_rules=[
    {'wmclass': 'confirm'},
    {'wmclass': 'dialog'},
    {'wmclass': 'download'},
    {'wmclass': 'error'},
    {'wmclass': 'file_progress'},
    {'wmclass': 'notification'},
    {'wmclass': 'splash'},
    {'wmclass': 'toolbar'},
    {'wmclass': 'confirmreset'},  # gitk
    {'wmclass': 'makebranch'},  # gitk
    {'wmclass': 'maketag'},  # gitk
    {'wname': 'branchdialog'},  # gitk
    {'wname': 'pinentry'},  # GPG key password entry
    {'wmclass': 'ssh-askpass'},  # ssh-askpass
])
auto_fullscreen = True
focus_on_window_activation = "smart"

@hook.subscribe.startup_once
def start_once():
    home = os.path.expanduser('~/.config/qtile/autostart.sh')
    subprocess.call([home])

@hook.subscribe.client_new
def floating_dialogs(window):
    dialog = window.window.get_wm_type() == 'dialog'
    transient = window.window.get_wm_transient_for()
    if dialog or transient:
        window.floating = True


# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, github issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "qtile"
