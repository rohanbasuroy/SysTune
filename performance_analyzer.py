# performance_analyzer.py

import subprocess
import time
import os

class PerformanceAnalyzer:
    def __init__(self):
        pass

    def compile_ffmpeg(self, compiler_flags):
        # Clean previous builds
        subprocess.run(['make', 'distclean'], cwd='ffmpeg_source', stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        configure_cmd = ['./configure', '--disable-doc', '--disable-debug', f'CFLAGS={" ".join(compiler_flags)}']
        start_time = time.time()
        try:
            # Configure
            subprocess.run(configure_cmd, check=True, cwd='ffmpeg_source', stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            # Build
            subprocess.run(['make', '-j4'], check=True, cwd='ffmpeg_source', stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            end_time = time.time()
            compile_time = end_time - start_time
            return compile_time
        except subprocess.CalledProcessError:
            print("FFmpeg compilation failed.")
            return None

    def set_system_params(self, system_params):
        for param, value in system_params.items():
            # Set sysctl parameters
            subprocess.run(['sudo', 'sysctl', f'{param}={value}'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    def run_ffmpeg(self):
        # Run the compiled FFmpeg on a test input and measure performance
        cmd = ['./ffmpeg', '-i', '../input.mp4', '-f', 'null', '-']
        start_time = time.time()
        try:
            subprocess.run(cmd, check=True, cwd='ffmpeg_source', stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            end_time = time.time()
            execution_time = end_time - start_time
            return execution_time
        except subprocess.CalledProcessError:
            print("FFmpeg execution failed.")
            return None

    def analyze_performance(self, compiler_flags, system_params):
        # Set system parameters
        self.set_system_params(system_params)
        # Compile FFmpeg with compiler flags
        compile_time = self.compile_ffmpeg(compiler_flags)
        if compile_time is None:
            return None
        # Run FFmpeg and measure execution time
        execution_time = self.run_ffmpeg()
        if execution_time is None:
            return None
        return {
            'compile_time': compile_time,
            'execution_time': execution_time
        }

