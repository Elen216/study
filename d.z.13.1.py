def remove_html_tags(input_file, output_file="cleaned.txt"):
    fin = open(input_file, 'r', encoding='utf-8')
    fout = open(output_file, 'w', encoding='utf-8')
    ignore = False
    char = fin.read(1)
    while char != '': 
        if char == '<':
            ignore = True 
        elif char == '>':
            ignore = False 
        elif not ignore:
            fout.write(char)
        char = fin.read(1)
    fin.close()
    fout.close()
    print("Завершено! Результат збережено:", output_file)
