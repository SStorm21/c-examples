
with open('names.txt', 'r+') as file:
    file_content = file.read()
    lines = file_content.split('\n')
    lines.insert(67, 'LANG.english()')
    file.seek(0)
    file.write('\n'.join(lines))
    file.close()
