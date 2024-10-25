# config.py

import os

# List of application compiler flags to tune
APP_COMPILER_FLAGS = [
    '-O0', '-O1', '-O2', '-O3',         # Compiler optimization levels
    '-finline-functions',               # Function inlining
    '-fno-inline-functions',
    '-ftree-vectorize',                 # Vectorization
    '-fno-tree-vectorize',
    '-fvect-cost-model=unlimited',      # Vectorization cost
    '-fvect-cost-model=cheap',
    '-fprefetch-loop-arrays',           # Prefetching
    '-fno-prefetch-loop-arrays',
    '-funroll-loops',                   # Loop unrolling
    '-fno-unroll-loops',
    '-flto',                            # Link-time optimization
    '-fno-lto',
    '-mstackrealign',                   # Stack realignment
    '-fstack-protector',
    '-fno-stack-protector',
    '-ffast-math',
    '-fno-fast-math',
    '-fomit-frame-pointer',
    '-fno-omit-frame-pointer',
    '-fstrict-aliasing',
    '-fno-strict-aliasing',
    '-floop-block',
    '-floop-interchange',
    '-floop-strip-mine',
]

# List of system parameters to tune with their possible values
SYSTEM_PARAMS = {
    'vm.swappiness': list(range(0, 101, 10)),  # 0 to 100
    'vm.dirty_ratio': list(range(0, 101, 10)),  # 0 to 100
    'vm.overcommit_memory': [0, 1, 2],
    'vm.overcommit_ratio': list(range(50, 151, 10)),  # 50 to 150
    'vm.dirty_background_ratio': list(range(0, 101, 10)),  # 0 to 100
    'vm.dirty_expire_centisecs': [100, 500, 1000, 5000],
    'kernel.sched_migration_cost_ns': [500000, 1000000, 5000000],
    'kernel.timer_migration': [0, 1],
    'kernel.sched_autogroup_enabled': [0, 1],
    'kernel.sched_min_granularity_ns': [1000000, 2000000, 4000000],
    'kernel.sched_wakeup_granularity_ns': [1500000, 3000000, 6000000],
    'kernel.sched_rr_timeslice_ms': [10, 50, 100],
    'kernel.sched_rt_period_us': [1000000, 2000000, 4000000],
    'kernel.sched_rt_runtime_us': [950000, 1900000, 3800000],
    'kernel.sched_latency_ns': [10000000, 20000000, 40000000],
}

# Blacklist for safety enforcer (parameters that should not be changed)
PARAM_BLACKLIST = [
    # Add any parameters that should not be modified for safety reasons
]

# OpenAI API key (set to None to use environment variable)
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY', None)

# Other configuration settings
MAX_ITERATIONS = 10

