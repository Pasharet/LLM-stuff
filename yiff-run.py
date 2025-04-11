import ctypes
import os
import random
import subprocess

ctypes.windll.kernel32.SetConsoleTitleW("yiff-run-01042025")

gguf_nvme = r'C:\AI\GGUF\\'
gguf_hdd = r'D:\BACKUP\AI\GGUF\\'

ascii_title = """
┬ ┬┬┌─┐┌─┐  ┬─┐┬ ┬┌┐┌
└┬┘│├┤ ├┤───├┬┘│ ││││
 ┴ ┴└  └    ┴└─└─┘┘└┘
"""

title = [ascii_title]

models = {
    # RP/ERP (Main)
    ' magnum-v3-34b-Q5_K_M (Yi-1.5)': {
        'path': gguf_hdd + 'magnum-v3-34b-Q5_K_M.gguf',
        'contextsize': 8192,
        'gpulayers': 10
    },
    ' magnum-v4-72b-Q4_K_M (Qwen2.5)': {
        'path': gguf_hdd + 'magnum-v4-72b-Q4_K_M.gguf',
        'contextsize': 16384,
        'gpulayers': 0
    },
    ' Midnight-Miqu-70B-v1.5.Q4_K_M (Miqu 1)': {
        'path': gguf_hdd + 'Midnight-Miqu-70B-v1.5.Q4_K_M.gguf',
        'contextsize': 8192, # Miqu 1 - 8K
        'gpulayers': 0
    },
    ' Cydonia-22B-v2k-Q6_K (Mistral Small 2409)': {
        'path': gguf_hdd + 'Cydonia-22B-v2k-Q6_K.gguf',
        'contextsize': 16384,
        'gpulayers': 14
    },
    # CODING & ASSISTANT
    ' Meta-Llama-3.1-8B-Instruct-Q5_K_M': {
        'path': gguf_hdd + 'Meta-Llama-3.1-8B-Instruct-Q5_K_M.gguf',
        'contextsize': 4096,
        'gpulayers': 33 # ALL layers!
    },
    ' gemma-3-27b-it-abliterated.q5_k_m': {
        'path': gguf_hdd + 'gemma-3-27b-it-abliterated.q5_k_m.gguf',
        'contextsize': 16384,
        'gpulayers': 12
    },
    ' qwen2.5-coder-32b-instruct-q5_K_M': {
        'path': gguf_hdd + 'qwen2.5-coder-32b-instruct-q5_k_m.gguf',
        'contextsize': 8192,
        'gpulayers': 10
    },
    ' qwq-32b-q5_k_m': {
        'path': gguf_hdd + 'qwq-32b-q5_k_m.gguf',
        'contextsize': 8192,
        'gpulayers': 10
    },
    ' DeepSeek-R1-Distill-Qwen-32B-Q5_K_M (Qwen2.5)': {
        'path': gguf_hdd + 'DeepSeek-R1-Distill-Qwen-32B-Q5_K_M.gguf',
        'contextsize': 8192,
        'gpulayers': 10
    },
    'c4ai-command-r-08-2024-Q5_K_M': {
        'path': gguf_hdd + 'c4ai-command-r-08-2024-Q5_K_M.gguf',
        'contextsize': 8192,
        'gpulayers': 10
    },
}

def run_model(model_name, model_info):
    command = [
        r'C:\_ai\koboldcpp_cu12.exe',
        '--model', model_info['path'],
        '--threads', '6',
        '--usecublas', 'normal', 'mmq', '0',
        # '--usecublas', 'normal', '0',
        '--contextsize', str(model_info['contextsize']),
        '--gpulayers', str(model_info['gpulayers']),
        '--skiplauncher',
        '--blasbatchsize', '512',
        '--blasthreads', '6',
        # '--usemmap',
        '--nommap',
        # '--usemlock',
        '--multiuser', '2',
        '--multiplayer',
        '--highpriority',
        '--quiet',
        '--password', 'knotting',
        # '--flashattention',
        # '--benchmark'
        # '--moeexperts', '8',
    ]
    
    try:
        subprocess.run(command, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Ошибка при запуске модели {model_name}: {e}")

def main():
    os.system('cls')
    print(random.choice(title))
    for i, (model_name, model_info) in enumerate(models.items(), start=1):
        print(f"{i}. {model_name}")

    while True:
        try:
            choice = int(input("\nВведите номер модели: "))
            if 1 <= choice <= len(models):
                selected_model_name = list(models.keys())[choice - 1]
                break
            else:
                print("Неверный номер. Попробуйте снова.")
        except ValueError:
            print("Пожалуйста, введите число.")

    os.system('cls')
    subprocess.run(['taskkill', '/f', '/im', 'koboldcpp_cu12.exe'], check=False)

    model_info = models[selected_model_name]
    run_model(selected_model_name, model_info)

if __name__ == "__main__":
    main()
