lines = []
with open("ch_first_name.txt", encoding='utf-8') as f:
    lines = f.read()
    lines = lines.replace("、", "\n")
with open("ch_first_name.txt", 'w', encoding='utf-8') as f:
    f.seek(0)
    f.truncate()
    f.write(lines)