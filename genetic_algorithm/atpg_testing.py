import subprocess
import multiprocessing
import random
import time

random.seed(0)


def compile_verilog_files(file_list: list, object_file_name):
    cmds = ['iverilog', '-o', object_file_name] + file_list
    t = subprocess.run(cmds, capture_output=True)
    if t.stderr:
        print(t.stderr.decode('utf-8'))
        return False
    else:
        return True


def gen_weighted_8bit_val(weights):
    """
    :param weights: percent probability of each bit
    :return: a weighted eight bit integer
    """
    s = ''
    for i in range(8):
        s += random.choices(['1', '0'], [weights[i], 255 - weights[i]])[0]
    return int(s, 2)


def compare_ETC_outputs(obj_files: list, inval: int):
    t1 = subprocess.run(['vvp', obj_files[0], '+A=' + str(inval), '+B=3', '+CIN=0'], capture_output=True)
    t2 = subprocess.run(['vvp', obj_files[1], '+A=' + str(inval), '+B=3', '+CIN=0'], capture_output=True)
    print('t1', t1.stdout)
    print('t2', t2.stdout)
    if t1.stdout.decode('utf-8') in t2.stdout.decode('utf-8'):
        return False
    return True


def rand_N_val_list(N: int, models):
    l = []
    for _ in range(N):
        if random.randint(0, 1):
            l.append(random.randint(1, models))
        else:
            l.append(0)
    return l


def create_FA_list(folder_path: str, num_list: list):
    l = []
    for i in range(1, 9):
        l.append(folder_path + 'full_adder' + str(i) + '_' + str(num_list[i-1]) + '.v')
    return l


# result file
# def testing(to_test, record_everything, process=0):

# if record_everything:
#     res_file = open('testing_result.txt', 'w')
#     res_file.write("%\"testCase\",\t \"faultModel\",\t \"didFind\",\t \"whichIteration\",\t \"primaryInput\";\n")
global_list_array = []
correct_num_list = [0] * 8
global_list_array.append(correct_num_list)
my_weights = [255, 46, 115, 231, 185, 231, 115, 92]
max_len = 15
FA_folder_path = '../FullAdders/'
TB_path = '../TestBenchs/test_bench.v'


def test_the_files(process):
    random_num_list = rand_N_val_list(8, 28)
    while random_num_list in global_list_array:
        random_num_list = rand_N_val_list(8, 28)

    # print(random_num_list)

    file_listc = [TB_path] + create_FA_list(FA_folder_path, correct_num_list)
    file_list = [TB_path] + create_FA_list(FA_folder_path, random_num_list)

    if compile_verilog_files(file_listc, 'main'+str(process)+'_0.vout'):
        if compile_verilog_files(file_list, 'main'+str(process)+'_1.vout'):
            didFind = True
            ivalue_list = []

            for iter_count in range(max_len):
                ivalue = gen_weighted_8bit_val(my_weights)

                while ivalue in ivalue_list:
                    ivalue = gen_weighted_8bit_val(my_weights)

                if compare_ETC_outputs(['main'+str(process)+'_0.vout', 'main'+str(process)+'_1.vout'], ivalue):
                    # if record_everything:
                    #     res_file.write(str(n)+",\t "+','.join(map(str, random_num_list))+",\t "+str(int(didFind))+",
                    #     \t "+str(iter_count)+",\t "+str(ivalue)+";\n")
                    print("found")
                    return True
                ivalue_list.append(ivalue)

            if didFind:
                print("not found!!!")
                return False

start = time.time()
test = 1000
det = 0
esc = 0
for i in range(test):
    if test_the_files(1):
        det += 1
    else:
        esc +=1

print("The detected faults are", det)
print("The fault coverage is", det/test*100)
print('The time taken is', time.time()-start)