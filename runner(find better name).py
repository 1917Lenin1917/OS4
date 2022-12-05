from dataclasses import dataclass
from subprocess import call
from time import sleep

@dataclass
class Configuration:
    name: str
    file: str 
    script: str 
    args: tuple

    def __post_init__(self):
        self.script = self.script.format(self.file, *self.args)

    def run(self):
        print(self.script)
        result = call(self.script, shell=True)

@dataclass
class ConfigManager:
    args = (100_000_000, 3, 4, 2)
    configurations = [
        Configuration(
            name='C++ (Optimization level 0)', 
            file='task.cpp', 
            script='g++ {} -O0 -o slow.out && (time -p ./slow.out {} {} {} {}) 2>&1 | tee results.log >> /dev/null',
            args=args
        ),
        Configuration(
            name='C++ (Optimization level 3)', 
            file='task.cpp', 
            script='g++ {} -O3 -o slow.out && (time -p ./slow.out {} {} {} {}) 2>&1 | tee results.log >> /dev/null',
            args=args
        ),
        Configuration(
            name='Python (Loop)',
            file='task_loop.py',
            script='(time -p python3 {} {} {} {} {}) 2>&1 | tee results.log >> /dev/null',
            args=args
        ),
        Configuration(
            name='Python (Reduce)',
            file='task_sum.py',
            script='(time -p python3 {} {} {} {} {}) 2>&1 | tee results.log >> /dev/null',
            args=args
        ), 
        Configuration(
            name='x86 asm',
            file='task.asm',
            script='nasm -f elf64 {} -o task_asm.o && g++ -no-pie task_asm.o -o task_asm && time -p ./task_asm 2>&1 | tee results.log >> /dev/null',
            args=args
        )
    ]


    def run(self):
        for config in self.configurations:
            print(f'*Running {config.name}')
            config.run()
            with open('results.log') as f_in:
                print(f_in.read())
            print('-'*10)



cf = ConfigManager()
cf.run()