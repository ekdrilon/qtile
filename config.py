# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
#########################################################################
# Hello This Is Me Ekd143,                                             ##
# this is my config mostly default and some add ons                    ##
# some of it is copied from dt qtile config,                           ##
# https://gitlab.com/dwt1/dotfiles/-/tree/master/.config/qtile         ##
#########################################################################
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

from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from libqtile import extension
from libqtile.backend.base import Window
from libqtile.layout.base import Layout
from libqtile import hook
from libqtile import qtile
import os
import subprocess


@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~/.config/qtile/autostart.sh')
    subprocess.run([home])


mod = "mod4"
terminal = guess_terminal()
# browser = firefox()

keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
    Key([mod], "h",
        lazy.layout.left(),
        desc="Move focus to left"
        ),
    
    Key([mod], "l",
        lazy.layout.right(),
        desc="Move focus to right"
        ),
    
    Key([mod], "j", 
        lazy.layout.down(),
        desc="Move focus down"
        ),
    
    Key([mod], "k",
        lazy.layout.up(),
        desc="Move focus up"
        ),
    
    Key([mod], "space",
        lazy.layout.next(),
        desc="Move window focus to other window"
        ),
    
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    
    Key([mod, "shift"], "h",
        lazy.layout.shuffle_left(),
        desc="Move window to the left"
        ),
    
    Key([mod, "shift"], "l",
        lazy.layout.shuffle_right(),
        desc="Move window to the right"
        ),
    
    Key([mod, "shift"], "j",
        lazy.layout.shuffle_down(),
        desc="Move window down"
        ),

    Key([mod, "shift"], "k",
        lazy.layout.shuffle_up(),
        desc="Move window up"
        ),

    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    
    Key([mod, "control"], "h",
        lazy.layout.grow_left(),
        desc="Grow window to the left"
        ),

    Key([mod, "control"], "l",
            lazy.layout.grow_right(),
            desc="Grow window to the right"
            ),

    Key([mod, "control"], "j",
            lazy.layout.grow_down(),
            desc="Grow window down"
            ),
    
    Key([mod, "control"], "k",
            lazy.layout.grow_up(),
            desc="Grow window up"
            ),

    Key([mod], "n",
            lazy.layout.normalize(),
            desc="Reset all window sizes"
            ),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, "shift"], "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key([mod], "Return",
            lazy.spawn("kitty"),
            desc="Launch terminal"
            ),
    
    # Toggle between different layouts as defined below
    
    Key([mod], "Tab",
            lazy.next_layout(),
            desc="Toggle between layouts"
            ),
    
    Key([mod], "q",
            lazy.window.kill(),
            desc="Kill focused window"
            ),

    Key([mod, "control"], "r",
            lazy.reload_config(),
            desc="Reload the config"
            ),

    Key([mod, "control"], "x",
            lazy.shutdown(),
            desc="Shutdown Qtile"
            ),

    Key([mod], "w",
            lazy.spawn("firefox"),
            desc="launch browser"
            ),
    Key([mod], "f",
            lazy.window.toggle_fullscreen(),
            desc="toggle fullscreen"
            ),

	# Volume control
    Key([], "XF86AudioRaiseVolume",
            lazy.spawn("amixer sset Master 5%+")
            ),

	Key([], "XF86AudioLowerVolume",
             lazy.spawn("amixer sset Master 5%-")
             ),
    
	# Volume Mute
    Key([], "XF86AudioMute",
            lazy.spawn("amixer sset Master toggle")
            ),

	 # Microphone Mute

    Key([], "XF86AudioMicMute",
            lazy.spawn("amixer sset Capture toggle")
            ),

	 # Brightness Control
	Key([], "XF86MonBrightnessUp",
            lazy.spawn("xbacklight -inc 5")
            ),

	 Key([], "XF86MonBrightnessDown",
             lazy.spawn("xbacklight -dec 5")
             ),
	# i3 lockscreen
	
	Key([mod], "c",
		lazy.spawn("i3lock -i /usr/share/backgrounds/archlinux/split.png")
		),

    # screenshot

    Key([mod], "Print",
        lazy.spawn("flameshot full")
            ),


    # Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
    
    Key([mod], "p",
            lazy.run_extension(extension.DmenuRun(
        dmenu_prompt=">",
        demnu_font="sans",
        fontsize=10 ,
        background="#15181a",
        foreground="#ffffff",
        selected_background='2c0a28',
        selected_foreground="#fff",
        ))),
]

# groups = [Group(i) for i in "123456789"]

groups = []

group_names = [
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "0",
]

group_labels = [
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
]
for i in range(len(group_names)):
    groups.append(
        Group(
            name=group_names[i],
            label=group_labels[i],
        )
    )

for i in groups:
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),

            # mod1 + shift + letter of group = switch to & move focused window to group
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(i.name),
            ),

            # Or, use below if you prefer not to switch to that group.
            # # mod1 + shift + letter of group = move focused window to group
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
        ]
    )

layouts = [
    layout.Columns(
        border_focus= '#27205c',
        border_normal= '#000000',
        border_width=4,
        margin=8
        ),
    
    # layout.Max(),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    
    layout.MonadTall(
        border_focus= '#91600a',
        border_normal= '#000000',
        border_width=4,
        margin=8
        ),

    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
    layout.Floating(
        border_focus= '#b07819',
        border_normal= '#000000',
        border_width=2 
        ),
]

widget_defaults = dict(
    font="sans",
    fontsize=12,
    padding=3,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
                # widget.CurrentLayoutIcon(
                   #  background= "#e0ffde",
                    # ),
                widget.Sep(
                    foreground= "#ffffff"
                    ),

                widget.CurrentLayout(
                    background= "#e0ffde",
                    foreground= "#000000"
                    ),

                widget.Sep(
                    foreground= 'ffffff'
                    ),
                
                widget.GroupBox(
                    highlight_method= 'line',
                    highlight_color=['2c0a28','27205c']
                    ),
                
                widget.Sep(
                    foreground= 'ffffff'
                    ),
                
                widget.Prompt(),
                
                # widget.WindowName(),
                
                widget.Spacer(),
                
                widget.Chord(
                    chords_colors={
                        "launch": ("#ff0000", "#ffffff"),
                    },
                    name_transform=lambda name: name.upper(),
                ),
                # widget.TextBox("default config", name="default"),
                # widget.TextBox("Press &lt;M-r&gt; to spawn", foreground="#d75f5f"),
                # widget.Systray(),
                
                widget.DF(
                    format = '     {p} ({uf}{m}|{r:.0f}%)'
                    ),
                widget.Cmus(),
                
                widget.Sep(
                    foreground= 'ffffff'
                    ),
                # widget.ThermalZone(),
                
                widget.CPU(
                    format= '     {load_percent}%',
                    background= "#f5d9c7",
                    foreground= "#000000"
                    ),
                

                widget.Sep(
                    foreground= 'ffffff'
                    ),

                widget.ThermalSensor(
                    fmt = '     {}',
                    background= "#ffc0cb",
                    foreground= "#000000"
                    ),

                widget.Sep(
                    foreground= 'ffffff'
                    ),
                
                widget.Memory(
                    format= '     {MemUsed: .0f}{mm}/{MemTotal: .0f}{mm}',
                    background= "#ffd4ff",
                    foreground= "#000000"
                    ),
                
                widget.Sep(
                    foreground= 'ffffff'
                    ),

                widget.Battery(
                    format = '      {percent:2.0%} {hour:d}:{min:02d}',
                    background= "#ff85fa",
                    foreground= "#000000"
                    ),

                widget.Sep(
                    foreground= 'ffffff'
                    ),
                
                widget.Net(
                    format = '      {down} ↓↑ {up}',
                    background= "#b298ff",
                    foreground= "#000000"
                    ),

                widget.Sep(
                    foreground = 'ffffff'
                    ),

                widget.Clock(
                    format= '     %d/%m/%y %H:%M',
                    background= "f6ebff",
                    foreground= "000000"
                    ),
                
                # widget.Sep(
                 #   foreground= 'ffffff'
                   # ),
                
                #widget.QuickExit(),
            ],
            24,
            # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
            # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
            background= '#0d0a17'
        ),
    ),
]

# Drag floating layouts.

mouse = [
    Drag([mod], "Button1",
        lazy.window.set_position_floating(),
        start=lazy.window.get_position()
        ),
    
    Drag([mod], "Button3",
        lazy.window.set_size_floating(),
        start=lazy.window.get_size()
        ),
    
    Click([mod], "Button2",
        lazy.window.bring_to_front()
        ),
]

dgroups_key_binder = None

dgroups_app_rules = []  # type: list

follow_mouse_focus = True

bring_front_click = False

cursor_warp = False

floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        
        Match(wm_class="confirmreset"),  # gitk
        
        Match(wm_class="makebranch"),  # gitk
        
        Match(wm_class="maketag"),  # gitk
        
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        
        Match(title="branchdialog"),  # gitk
        
        Match(title="pinentry"),  # GPG key password entry
    ]
)

auto_fullscreen = True

focus_on_window_activation = "smart"

reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?

auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.

wl_input_rules = None

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
