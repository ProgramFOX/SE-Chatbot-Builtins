module_name = "nesting"

def nesting_deco(get_output):
    def check_nested(cmd_args, message, event, start):
        content = cmd_args
        final_content = ""
        temp_content = ""
        open_brackets = 0

        i = 0
        while i < len(content):
            if content[i] == '\\' and i < len(content) - 2 and content[i + 1:i + 3] in ['{{', '}}']:
                to_add = content[i + 1:i + 3]
                i += 2
            else:
                to_add = content[i]
                if content[i] == '{' and i < len(content) - 1 and content[i + 1] == '{':
                    i += 1
                    if open_brackets == 0:
                        to_add = ""
                    else:
                        to_add += content[i]
                    open_brackets += 1
                elif content[i] == '}' and i < len(content) - 1 and content[i + 1] == '}':
                    i += 1
                    if open_brackets == 1:
                        to_add = ""
                        cn = check_nested(temp_content, message, event, -1 if start == -1 else message.content_source.find('{{', start))
                        if cn is None or cn is False:
                            return None
                        final_content += cn
                        temp_content = ""
                    else:
                        to_add += content[i]
                    open_brackets -= 1
                    if open_brackets < 0:
                        return "Your nesting brackets '{{' and '}}' don't match up"
            if open_brackets > 0:
                temp_content += to_add
            else:
                final_content += to_add
            i += 1

        if open_brackets == 0:
            return get_output(final_content, message, event, start)
        else:
            return "Your nesting brackets '{{' and '}}' don't match up"
    return check_nested


def on_bot_load(bot):
    bot.command = nesting_deco(bot.command)


commands = []
