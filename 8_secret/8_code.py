def secret_replace(text, **kv):
    for k in kv:
        spisok = kv[k] * text.count(k)
        count = 0
        for i in range(len(text)):
            if text[i] == k:
                text = text.replace(text[i], spisok[count], 1)
                count += 1
            else:
                pass
    return text