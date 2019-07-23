f1 = open('filelists/chinese_text_train_old_filelist.txt')
f2 = open('filelists/chinese_text_train_filelist.txt', 'w')
all_line = f1.read().splitlines()

for line in all_line:
    l = line.split('|')
    if len(l[1]) > 70 and len(l[1]) < 120:
        # print (line)
        f2.write(line + '\n')
