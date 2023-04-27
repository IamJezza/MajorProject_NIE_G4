import subprocess
import multiprocessing
import time

# for 8-bit vectors
def compile_verilog_files(files):
    cmds = ["iverilog"]
    for i in files:
        cmds.append(i)

    t = subprocess.run(cmds, capture_output=True)
    if not t.stderr:
        return True
    else:
        if t.stderr:
            print(str(t.stderr)[2:-3])
            return False
        else:
            print("ERROR OCCURRED")
            return False


def run_verilog(output_file_name, input_args, result_file):
    cmds = ["vvp", output_file_name]
    outFile = open(result_file, 'a')
    for i in input_args:
        cmds.append(i)
    t = subprocess.run(cmds, capture_output=True)

    if t.stdout:
        outFile.write(str(t.stdout)[2:-3]+", ")
        outFile.close()
        return "", True
    else:
        return "Error: incorrect statement", False


def create_processes(Input_files, output_file, result_file):
    if compile_verilog_files(Input_files):
        for i in range(2**8):
            run_verilog(output_file, ["+A="+str(i), "+B=3", "+CIN=0"], result_file)


def TB(i):
    return "TestBenchs/test_bench"+str(i)+".v"


def FA(i):
    return "FullAdders/full_adder"+str(i)+".v"


def my_run(full_adder_indices, test_bench_index: int):

    files = ["-o", "out"+str(test_bench_index)+str(full_adder_indices), TB(test_bench_index)]
    for i in full_adder_indices:
        files.append(FA(i))
    outFile = open("Results/Output"+str(test_bench_index)+str(full_adder_indices)+".txt", "w")
    outFile.write("out"+str(test_bench_index)+str(full_adder_indices)+" = [")
    outFile.close()

    create_processes(files, "out"+str(test_bench_index)+str(full_adder_indices), "Results/Output"+str(test_bench_index)+str(full_adder_indices)+".txt")

    with open("Results/Output"+str(test_bench_index)+str(full_adder_indices)+".txt", 'rb+') as f:
        f.seek(-2, 2)
        f.truncate()
        f.close()
    with open("Results/Output"+str(test_bench_index)+str(full_adder_indices)+".txt", 'a') as f:
        f.write("]\n")
        f.close()
    return True


if __name__ == "__main__":
    start = time.time()
    pros = [multiprocessing.Process(target=my_run, args=([0], 0))]
    for i in range(1, 9):
        for j in range(1, 29):
            pros.append(multiprocessing.Process(target=my_run, args=([0, j], i)))

    while pros:
        for i in range(multiprocessing.cpu_count()):
            try:
                pros[i].start()
            except IndexError:
                pass
        for _ in range(multiprocessing.cpu_count()):
            try:
                pros[0].join()
                pros.pop(0)
            except IndexError:
                pass
    end = time.time()
    print("the code ended in "+str(end-start)+"s")


'''# For 16 bit vector!
def compile_verilog_code_once(input_list):
    compile_cmd = ["iverilog", input_list[0], input_list[1]]
    return subprocess.call(compile_cmd)


def run_verilog_code_once(input_list):
    run_cmd = ['vvp', 'a.out']
    for j in range(len(input_list)):
        run_cmd.append(input_list[j])
    return subprocess.run(run_cmd)


if __name__ == "__main__":
    testBenchName = "test_bench0.v"
    fullAdderName = "full_adder0.v"
    compile_list = [testBenchName, fullAdderName]
    start = time.time()
    compile_output = compile_verilog_code_once(compile_list)
    run_output=[]
    if compile_output == 0:
        for i in range(2**8):
            for j in range(3, 4):
                for k in range(1):
                    run_list = ["+A="+str(i), "+B="+str(j), "+CIN="+str(k)]
                    run_output.append(multiprocessing.Process(target=run_verilog_code_once, args=(run_list,)))

    while run_output:
        for i in range(multiprocessing.cpu_count() * 2):
            try:
                run_output[i].start()
            except IndexError:
                pass
        for _ in range(multiprocessing.cpu_count()*2):
            try:
                run_output[0].join()
                run_output.pop(0)
            except IndexError:
                pass
    end = time.time()
    print("the code finished in " + str(end - start) + "s")
'''
