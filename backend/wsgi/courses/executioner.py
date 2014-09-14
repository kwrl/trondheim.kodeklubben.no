import os
import sys
import resource
import subprocess

def set_resource(time, memory=-1, procs=-1):
    def result():
        nproc = resource.getrlimit(resource.RLIMIT_NPROC)
        tcpu = resource.getrlimit(resource.RLIMIT_CPU)
        mem = resource.getrlimit(resource.RLIMIT_DATA)
        # Set The maximum number of processes the current process may create.
        try:
            resource.setrlimit(resource.RLIMIT_NPROC, (procs, procs))
        except Exception:
            resource.setrlimit(resource.RLIMIT_NPROC, nproc)
            # Set The maximum amount of processor time (in seconds) that a process can use.
        try:
            resource.setrlimit(resource.RLIMIT_CPU, (time, time))
        except Exception:
            resource.setrlimit(resource.RLIMIT_CPU, tcpu)
            # Set The maximum area (in bytes) of address space which may be taken by the process.
        try:
            resource.setrlimit(resource.RLIMIT_AS, (memory, memory))
        except Exception:
            resource.setrlimit(resource.RLIMIT_AS, mem)
            os.nice(19)
    return result

def execute(cmd, input, limits=None, wdir=None):
    if limits:
        resource = set_resource(limits.time, memory=limits.memory, procs=limits.procs)
        proc = subprocess.Popen(cmd, shell=True, stdin=subprocess.PIPE, preexec_fn=resource)
    else:
        proc = subprocess.Popen(cmd, shell=True, stdin=subprocess.PIPE)

    stdout, stderr = proc.communicate(input=input) 
    retval = proc.poll()

    return retval, stdout, stderr 
