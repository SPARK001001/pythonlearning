#! /usr/bin/env python
# _*_ coding:utf-8 _*_
#内存使用率
import commands
import json
from datetime import datetime
def memory_stat():
        mem = {}
        f = open("/proc/meminfo")
        lines = f.readlines()
        f.close()
        for line in lines:
                name = line.split(':')[0]
                var = line.split(':')[1].split()[0]
                mem[name] = long(var) * 1024.0
        mem_use =  mem['MemAvailable'] / mem['MemTotal'] *100
        return mem_use
#cpu使用率
#CPU指标：user，nice, system, idle, iowait, irq, softirq
def cpu_stat():
        import time 
        def cpu_r():
                f = open("proc/stat")
                for f_line in f:
                        break
                f.close()
                f_line = f_line.split()
                f_line_a = []
                for i in f_line:
                        if i.isdigit():
                                i = int(i)
                                f_line_a.append(i)
                total = sum(f_line_a)
                idle = f_line_a[3]
                return total,idle
        total_a,idle_a = cpu_r()
        time.sleep(2)
        total_b,idle_b = cpu_r()
        sys_idle = idle_b - idle_a
        sys_total = total_b - total_a
        sys_us = sys_total - sys_idle
        cpu_use= (float(sys_us) / sys_total) * 100
        return cpu_use 
#磁盘使用率
def disk_stat():
        import commands
        f = commands.getstatusoutput('df -hl | grep ^/dev/*')
        dev = f[1].split('\n')
        disk_use = {}
        for i in dev:
                name = i.split()[0]
                var = i.split()[4]
                disk_use[name] = float(var.split('%')[0])
        return disk_use



if __name__ == "__main__":
        mem_use = memory_stat()
        cpu_use = cpu_stat()
        disk_use = disk_stat()
        d = {}
        d['time'] = str(datetime.now())
        d['mem_use'] = float(mem_use)
        d['cpu_use'] = float(cpu_use)
        d = dict(d,**disk_use)
        json_log = json.dumps(d)

        with open('/root/test/catchinfo_log','a') as f:
                f.write(json_log+'\n')
