# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
niilber = 0
count = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    count += 1
    niilber += float(line[20:].rstrip())
    print("Yu baina da")
print(niilber/count)
print("Done")
