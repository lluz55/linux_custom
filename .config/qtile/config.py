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

from libqtile import qtile
from libqtile import bar, layout
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

from qtile_extras import widget
from qtile_extras.widget.decorations import RectDecoration
from libqtile import hook
import os
import subprocess

mod = "mod1"

# terminal = guess_terminal()
terminal = "kitty"
browser = "firefox"

keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
    Key([mod], "left", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "right", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "down", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "up", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(),
        desc="Move window focus to other window"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "left", lazy.layout.shuffle_left(),
        desc="Move window to the left"),
    Key([mod, "shift"], "right", lazy.layout.shuffle_right(),
        desc="Move window to the right"),
    Key([mod, "shift"], "down", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "up", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "left", lazy.layout.grow_left(),
        desc="Grow window to the left"),
    Key([mod, "control"], "right", lazy.layout.grow_right(),
        desc="Grow window to the right"),
    Key([mod, "control"], "down", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "up", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    Key([mod], "b", lazy.spawn(browser), desc="Launch browser"),
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "x", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
]

groups = [Group(i, label="○") for i in "12345"]


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
            # Key(
            # [mod, "shift"],
            # i.name,
            # lazy.window.togroup(i.name, switch_group=True),
            # desc="Switch to & move focused window to group {}".format(i.name),
            # ),
            # Or, use below if you prefer not to switch to that group.
            # # mod1 + shift + letter of group = move focused window to group
            Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
                desc="move focused window to group {}".format(i.name)),
        ]
    )

layouts = [
    layout.Columns(
        border_focus_stack=["#00bfff", "#00bfff"],
        border_width=2,
        margin=5,
        border_focus="#00bfff",
        border_normal="#bbbbbb"
    ),
    # layout.Max(),
    # Try more layouts by unleashing below layouts.
    layout.Stack(
        num_stacks=2,
        border_focus_stack=["#00bfff", "#00bfff"],
        border_width=2,
        margin=5,
        border_focus="#00bfff",
        border_normal="#bbbbbb",
        autosplita=True,
    ),
    # layout.Bsp(),
    # layout.Matrix(),
    # layout.MonadTall(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

widget_defaults = dict(
    font="sans",
    fontsize=12,
    padding=10,
)
extension_defaults = widget_defaults.copy()

decoration_group = {
    "decorations": [
        RectDecoration(colour="#38424d", radius=10,
                       filled=True, padding_y=6, group=True)
    ],
    "padding": 10,
}

decoration_group2 = {
    "decorations": [
        RectDecoration(colour="#00000000", clip=True, padding_y=6, group=True)
    ],
    "padding": 10,
}


@hook.subscribe.setgroup
def setgroup():
    for i in range(0, 7):
        qtile.groups[i].label = "᭵"
    qtile.current_group.label = "⦿"
    qtile.current_group.fmt = "<b>{}</b>"


def build_widget_list():
    widget_list = [
        widget.GroupBox(
            rounded=False,
            highlight_method="text",
            # highlight_color="#adffca",
            active="#ffffff",
            inactive="#555",
            border_width=5,
            this_current_screen_border="#ffffff",
            padding_y=10,
            other_screen_border="#777777",
            fontsize=18,
            urgent_alert_method="text"
        ),
        widget.Prompt(),
        # widget.Spacer(),
        widget.WindowName(**decoration_group,
                          fmt='<b>{}</b>', max_chars=75, scroll=True),
        widget.Spacer(),
        # widget.Chord(
        #     chords_colors={
        #         "launch": ("#00bfff", "#ffffff"),
        #     },
        #     name_transform=lambda name: name.upper(),
        # ),
        # widget.PulseVolume(emoji=True, **decoration_group2),
        widget.WifiIcon(),
        widget.Bluetooth(),
        widget.KeyboardLayout(),
        widget.UPowerWidget(),
        widget.Volume(fmt=' {}', fontsize=14),
        # NB Systray is incompatible with Wayland, consider using StatusNotifier instead
        # widget.StatusNotifier(),
        widget.Systray(**decoration_group2),
        widget.Spacer(length=10),
        widget.Clock(format="%d %b | %H:%M", **decoration_group),
        widget.QuickExit(default_text="⏻", fontsize=20, countdown_format="{}"),
    ]
    return widget_list


def build_widget_list_screen1():
    widget_list1 = build_widget_list()
    del widget_list1[1:2]
    del widget_list1[5:6]
    return widget_list1


def build_screens():
    return [Screen(top=bar.Bar(build_widget_list(), background="#00000000", size=40, border_width=0)),
            Screen(top=bar.Bar(build_widget_list_screen1(), background="#00000000", size=40, border_width=0))]


screens = build_screens()

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
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


def window_to_previous_screen(qtile, switch_group=False, switch_screen=False):
    i = qtile.screens.index(qtile.current_screen)
    if i != 0:
        group = qtile.screens[i - 1].group.name
        qtile.current_window.togroup(group, switch_group=switch_group)
        if switch_screen:
            qtile.cmd_to_screen(i - 1)


def window_to_next_screen(qtile, switch_group=False, switch_screen=False):
    i = qtile.screens.index(qtile.current_screen)
    if i + 1 != len(qtile.screens):
        group = qtile.screens[i + 1].group.name
        qtile.current_window.togroup(group, switch_group=switch_group)
        if switch_screen:
            qtile.cmd_to_screen(i + 1)

keyboard = widget.KeyboardLayout(configured_keyboards=['us', 'br'])

keys.extend([
    # Change window through monitors
    Key([mod, "shift"], "page_down",  lazy.function(window_to_next_screen)),
    Key([mod, "shift"], "page_up", lazy.function(window_to_previous_screen)),

    # Change window through monitors and change focus
    Key([mod, "control"], "page_down",  lazy.function(
        window_to_next_screen, switch_screen=True)),
    Key([mod, "control"], "page_up", lazy.function(
        window_to_previous_screen, switch_screen=True)),

    # Change focus through monitors
    Key([mod], "page_down",  lazy.prev_screen(), desc="Previous monitor"),
    Key([mod], "page_up",  lazy.next_screen(), desc="Next monitor"),

    Key([mod], "f",  lazy.window.toggle_fullscreen(), desc="Toggle fullscreen"),
    # Sound; `alsa-utils` must be installed
    Key([], "XF86AudioMute", lazy.spawn("amixer -q set Master toggle")),
    Key([], "XF86AudioLowerVolume", lazy.spawn(
        "amixer set Master 5%- unmute")),
    Key([], "XF86AudioRaiseVolume", lazy.spawn(
        "amixer set Master 5%+ unmute")),
Key([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl set +5%")),
Key([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl set 5%-")),
    

    # Key([mod, "shift"], "down", lazy.layout.down(), desc="Move focus down"),
    # Key([mod, "shift"], "up", lazy.layout.up(), desc="Move focus up"),
])


@ hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~/.config/qtile/autostart.sh')
    subprocess.Popen([home])
