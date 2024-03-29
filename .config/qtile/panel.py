from libqtile.config import Group, Key
from libqtile.lazy import lazy

mod = "mod4"  # Sets mod key to SUPER/WINDOWS


def panel_setup(keys):
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
    ]

    # group_labels = ["1", "2", "3", "4", "5", "6", "7", "8", "9",]
    group_labels = [
        "dev",
        "www",
        "sys",
        "doc",
        "vbox",
        "chat",
        "mus",
        "vid",
        "gfx",
    ]
    # group_labels = ["", "", "", "", "", "", "", "", "",]

    for i in range(len(group_names)):
        groups.append(
            Group(
                name=group_names[i],
                layout="monadtall",
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
                    desc="switch to group {}".format(i.name),
                ),
                # mod1 + shift + letter of group = move focused window to group
                Key(
                    [mod, "shift"],
                    i.name,
                    lazy.window.togroup(i.name, switch_group=False),
                    desc="move focused window to group {}".format(i.name),
                ),
            ]
        )
    return groups
