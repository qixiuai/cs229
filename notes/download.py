
import subprocess
subprocess.run(["ls", "-l"])

for i in range(1, 20):
    subprocess.run(["wget", "http://cs229.stanford.edu/notes/cs229-notes{}.pdf".format(i)])
