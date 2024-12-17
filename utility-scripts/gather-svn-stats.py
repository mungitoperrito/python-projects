''' 
Gather data on sizes of svn repos

Author: Dave Cuthbert
Copyright: GrammaTech 2017
'''

import os
import shutil
import subprocess
from datetime import datetime



def setup_dir(test_dir_name):
    if os.path.isdir(test_dir_name):
        shutil.rmtree(test_dir_name, ignore_errors=True)

    os.mkdir(test_dir_name)


def get_size():
    df = subprocess.check_output(["df", "/dev/sda2"])
    output = df.decode('utf-8').split("\n")
    device, size, used, available, percent, mountpoint = output[1].split()

    return available


def get_times(process_name):
    time_cmd = "/usr/bin/time -f \"%e :: %S :: %U :: %M\" " + process_name + " 1>/dev/null"
    try:
        times = subprocess.check_output(time_cmd, stderr=subprocess.STDOUT, shell=True).decode("utf-8") 
    except Exception as problem:
        times = "999 : 999 : 999 : 999\n"
        print("ERR: get_times({}) --> {}".format(problem.args)) 
    # Remove newline
    times = times[:-1]            
    real, system, user, mem = times.split(' :: ')
    # real sometimes picks up additional warnings from stderr
    if '\n' in real:
       real = real.split('\n')[-1]
   
    return real, system, user, mem


def get_stats(command):
    start_size = get_size()
    real, system, user, mem = get_times(command) 
    end_size = get_size()
    size_delta = int(start_size) - int(end_size)
     
    return real, system, user, mem, size_delta


def checkout_code():
    process_list = ["svn co -N svn+ssh://svn/svn/trunk",
                    "svn up -N third-party",
                    "svn up third-party/scons",
                    "svn up gtr",
                    "svn up codesonar",
                    ]
   
    output = ["Real    Sys    User    Mem    Delta       Command"]
    for p in process_list:
        cur_dir = os.path.basename(os.path.normpath(os.getcwd()))
        # Can't just add 'cd trunk', time complains since cd is a bash built in
        if((os.path.isdir('trunk')) and (cur_dir != 'trunk')):
            os.chdir('trunk')
        real, system, user, mem, delta = get_stats(p) 
        output.append("{}   {}   {}   {}   {}   {}"\
                      .format(real,system,user,mem,delta,p)
                     )

    return output


def run_build(build_cmd):
    real, system, user, mem, delta = get_stats(build_cmd) 
    output = "{}   {}   {}   {}   {}   {}"\
        .format(real,system,user,mem,delta,build_cmd)

    return output


##################
####   MAIN   ####
##################
STARTDIR = os.getcwd()
TESTDIR = "gather_stats"
timestamp = "".join(list(datetime.now().strftime('%Y%m%d-%H%M%S')))
OUTFILE = open("svn_stats_" + timestamp, "w")

build_list = [
    "codesonar/build --jobs=4 -k swyx=1 x86=1 ida_dev_ini=0",
    "codesonar/build --jobs=4 -k swyx=1 x64=1 ida_dev_ini=0",
    "codesonar/build --jobs=4 -k swyx=1 arm=1 ida_dev_ini=0"
    ]

for b in build_list:
    OUTFILE.write("STARTING: {}\n\n".format(b))
    OUTFILE.flush()

    setup_dir(TESTDIR)
    os.chdir(TESTDIR)

    checkout_results = checkout_code()
    for cr in checkout_results:
        OUTFILE.write("{}\n".format(cr))
    OUTFILE.flush()


    build_results = run_build(b)
    OUTFILE.write("{}\n".format(build_results))
    OUTFILE.flush()

    os.chdir(STARTDIR)
    OUTFILE.write("ENDING: {}\n\n".format(b))
#EOF
