    def format_links(text, brackets="()[]"):
        replace_dict = {
            'Aureoboletus': 'boletus',
            'Butyriboletus': 'boletus',
            'Caloboletus': 'boletus',
            'Cyanoboletus': 'boletus',
        }
        count = [0] * (len(brackets) // 2) # count open/close brackets
        saved_chars = []
        for character in text:
            for i, b in enumerate(brackets):
                if character == b: # found bracket
                    kind, is_close = divmod(i, 2)
                    count[kind] += (-1)**is_close # `+1`: open, `-1`: close
                    if count[kind] < 0: # unbalanced bracket
                        count[kind] = 0  # keep it
                    else:  # found bracket to remove
                        break
            else: # character is not a [balanced] bracket
                if not any(count): # outside brackets
                    saved_chars.append(character)
                            # saved_chars = ''.join(saved_chars)
        list = saved_chars.split()
        changed = []
        if list[0] in replace_dict:
            changed.append(replace_dict[list[0]])
        else: 
            changed.append(list[0])
        changed.append(list[1])
        saved_chars = '-'.join(changed)
        if saved_chars[-1] == ' ':
            saved_chars = saved_chars[:-1]
        # return saved_chars