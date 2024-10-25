# SysTune: LLM-Based Hardware-Software Parameter Optimization
Here we implement an autotuner for tuning hardware and software parameters of large-scale high performance computing (HPC) applications using OpenAI's GPT-4 language model. The system iteratively refines parameter configurations based on performance feedback to optimize for execution time.

Optimizing hardware and software parameters for HPC applications can be a complex and time-consuming task due to the vast number of possible configurations. This project aims to automate the tuning process by leveraging OpenAI's GPT-4 language model to suggest optimal parameter settings based on iterative performance feedback.

The system consists of several modules that work together in a feedback loop:
- **Prompt Generator**: Creates prompts for the LLM based on previous performance and parameters.
- **Option Evaluator**: Parses the LLM responses to extract new parameter values.
- **Safety Enforcer**: Ensures the suggested parameters are safe and valid.
- **Performance Analyzer**: Compiles and runs FFmpeg with the given parameters and measures performance.
- **Main Script**: Orchestrates the tuning process.


## Prerequisites
- Python 3.7 or higher
- OpenAI Python library (`openai`)
- FFmpeg source code (Download and extract to `ffmpeg_source/` directory)
- GCC compiler and build tools (`make`, `gcc`, etc.)
- An input video file `input.mp4` in the parent directory of `ffmpeg_source/`
- OpenAI API key (with access to GPT-4 model)

## Setup Instructions

### 1. Install Required Python Libraries
Ensure you have `pip` installed. Then install the OpenAI Python library:
```bash
pip install openai
```

### 2. Set Up OpenAI API Key
Obtain your OpenAI API key from OpenAI's website and set it as an environment variable:
```bash
export OPENAI_API_KEY='your-api-key'
```
Alternatively, you can set the `OPENAI_API_KEY` variable directly in `config.py`.

### 3. Download FFmpeg Source Code
Download the FFmpeg source code from [https://ffmpeg.org/download.html](https://ffmpeg.org/download.html) and extract it to the `ffmpeg_source/` directory.

Example using `wget`:
```bash
wget https://ffmpeg.org/releases/ffmpeg-4.4.tar.gz
tar -xzf ffmpeg-4.4.tar.gz
mv ffmpeg-4.4 ffmpeg_source
```

### 4. Prepare an Input Video File
Place an input video file named `input.mp4` in the parent directory of `ffmpeg_source/`. Alternatively, adjust the file path in `performance_analyzer.py` to point to your video file.

Example:
```bash
cp /path/to/your/video.mp4 ./input.mp4
```

### 5. Ensure Build Tools are Installed
Make sure you have the necessary build tools installed (`gcc`, `make`, etc.).

On Debian/Ubuntu-based systems:
```bash
sudo apt update
sudo apt install build-essential
```

### 6. Configure Parameters
Edit the `config.py` file to adjust any configuration settings if necessary. You can add or remove parameters to tune, set the maximum number of iterations, and adjust other settings.

### 7. Ensure Sudo Privileges
Adjusting system parameters requires sudo privileges. You may need to run the main script with sudo:
```bash
sudo python main.py
```
Alternatively, you can configure your `sudoers` file to allow your user to execute `sysctl` commands without a password. Be cautious when editing the `sudoers` file to avoid security risks.

## Usage Instructions
To start the tuning process, run the main script:
```bash
sudo python main.py
```
The script will perform the following steps:
1. Generate a prompt for the LLM based on previous parameters and performance.
2. Use GPT-4 to suggest new parameter values.
3. Evaluate the LLM's suggestions for safety and validity.
4. Apply the new system parameters.
5. Compile FFmpeg with the new compiler flags.
6. Run FFmpeg and measure its performance.
7. Compare the performance with previous iterations.
8. Repeat the process for the specified number of iterations or until no further improvements are found.


## Code Description

### 1. config.py
Configuration settings and lists of parameters.

### 2. prompt_generator.py
Generates prompts for the LLM based on previous performance and parameters.

### 3. option_evaluator.py
Parses the LLM responses to extract new parameter values.

### 4. safety_enforcer.py
Ensures the suggested parameters are safe and valid.

### 5. performance_analyzer.py
Compiles FFmpeg with new compiler flags, sets system parameters, runs FFmpeg, and measures performance.

### 6. main.py
The main script that orchestrates the tuning process.
