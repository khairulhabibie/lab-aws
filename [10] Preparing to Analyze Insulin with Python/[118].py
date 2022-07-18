# clean data
orifile = "preproinsulin-seq.txt"
cleanFile = "preproinsulin-seq-clean.txt"
delete_list = ["ORIGIN", " 1", "61", "//", " "]

orifile = open(orifile)
cleanFile = open(cleanFile, "w+")
for line in orifile:
    for word in delete_list:
        line = line.replace(word, "")
    cleanFile.write(line[1:112])

orifile.close()
cleanFile.close()

# ------------------------------------------------------
# select data
cleanFile = "preproinsulin-seq-clean.txt"
file1 = open("lsinsulin-seq-clean.txt", "w+")
file2 = open("lbinsulin-seq-clean.txt", "w+")
file3 = open("cinsulin-seq-clean.txt", "w+")
file4 = open("ainsulin-seq-clean.txt", "w+")

cleanFile = open(cleanFile)
data = str(cleanFile.read())

file1.write(data[0:25])
file2.write(data[25:55])
file3.write(data[55:90])
file4.write(data[90:111])

cleanFile.close()
file1.close()
file2.close()
file3.close()
file3.close()