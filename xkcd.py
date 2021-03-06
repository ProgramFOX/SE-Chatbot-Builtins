from Module import Command
import string

module_name = "xkcd"

def command_xkcdrandomnumber(cmd, bot, args, msg, event):
    return "[4 // Chosen by fair dice roll. Guaranteed to be random.](http://xkcd.com/221/)"


def command_xkcd(cmd, bot, args, msg, event):
    if len(args) < 1:
        return "Not enough arguments."
    try:
        id_ = int(args[0])
    except:
        return "Invalid arguments."
    return "http://xkcd.com/%i/" % id_

commands = [
    Command('xkcdrandomnumber', command_xkcdrandomnumber, "Returns a random number, based on an xkcd comic. Syntax: `$PREFIXxkcdrandomnumber`", False, False),
    Command('xkcd', command_xkcd, "Shows the specified xkcd comic. Syntax: `$PREFIXxkcd comic_id`", False, False, None, None, string.digits, None)
]
