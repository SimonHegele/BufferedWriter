from matplotlib import pyplot
from numpy      import min
from os         import getcwd, mkdir, path
from random     import randint
from time       import time

from buffered_writer import BufferedWriter

lines_to_write = 100_000
files_to_write = 1000
min_buffered   = 0
max_buffered   = 20

lines = [randint(0,1_000_000_000_000) for _ in range(lines_to_write)]

# 1. Regular writing

out_dir = path.join(getcwd(), "regular")

mkdir(out_dir)
start   = time()

for line in lines:

    file_path = path.join(out_dir, f"file_{line%files_to_write}")
    with open(file_path, "a") as file:
        file.write(str(line)+"\n")

regular_time = time() - start

# 2. Buffered writing 

buffered_lines = list(range(min_buffered,max_buffered+1))
buffered_times = []

for i in buffered_lines:

    print(i)

    out_dir = path.join(getcwd(), f"buffered_{i}_lines")
    mkdir(out_dir)

    start = time()

    with BufferedWriter(out_dir=out_dir, lines_per_file=i) as writer:

        for line in lines:
            writer.write_line(f"file_{str(line%files_to_write)}", str(line))
    
    buffered_times.append(time()-start)

fig, axes = pyplot.subplots()

m = buffered_times.index(min(buffered_times))
axes.scatter(buffered_lines, buffered_times, label="Buffered writing")
axes.set_xlabel("Buffered lines per file", fontweight="bold")
axes.set_ylabel("Time (s)", fontweight="bold")
axes.plot([min_buffered,max_buffered],[regular_time,regular_time], label="Regular writing")
axes.plot([m, m],[min(buffered_times),regular_time], color="red")
axes.text(min(buffered_times)+((regular_time-min(buffered_times))/2), m+0.5, f"{int(regular_time/min(buffered_times))}x", color="red")
axes.legend()
pyplot.show()