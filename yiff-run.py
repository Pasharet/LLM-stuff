import ctypes
import subprocess

ctypes.windll.kernel32.SetConsoleTitleW("yiff-run")

models = {
    # RP/ERP (Main)
    'Yi-1.5 FT: magnum-v3-34b-Q5_K_M': {
        'path': r'D:\BACKUP\AI\GGUF\magnum-v3-34b-Q5_K_M.gguf',
        'contextsize': 8192,
        'gpulayers': 10
    },
    'Qwen 2.5 FT: magnum-v4-72b-Q4_K_M': {
        'path': r'D:\BACKUP\AI\GGUF\magnum-v4-72b-Q4_K_M.gguf',
        'contextsize': 16384,
        'gpulayers': 0
    },
    'Miqu 1 FT: Midnight-Miqu-70B-v1.5.Q4_K_M': {
        'path': r'D:\BACKUP\AI\GGUF\Midnight-Miqu-70B-v1.5.Q4_K_M.gguf',
        'contextsize': 8192,
        'gpulayers': 0
    },
    # RP/ERP (Lifeless)
    'Gemma 2 FT: Cydonia-22B-v2k-Q6_K': {
        'path': r'D:\BACKUP\AI\GGUF\Cydonia-22B-v2k-Q6_K.gguf',
        'contextsize': 16384,
        'gpulayers': 15
    },
    'Gemma 2 FT: magnum-v4-22b-Q8_0': {
        'path': r'D:\BACKUP\AI\GGUF\magnum-v4-22b-Q8_0.gguf',
        'contextsize': 16384,
        'gpulayers': 15
    },
    'Mistral Small FT: magnum-v4-27b-Q5_K_M': {
        'path': r'D:\BACKUP\AI\GGUF\magnum-v4-27b-Q5_K_M.gguf',
        'contextsize': 8192,
        'gpulayers': 10
    },
    'Mistral Nemo FT: saiga_nemo_12b.Q8_0': {
        'path': r'D:\BACKUP\AI\GGUF\saiga_nemo_12b.Q8_0.gguf',
        'contextsize': 16384,
        'gpulayers': 20
    },
    # CODING & ASSISTANT
    'Base: qwen2.5-coder-32b-instruct-q5_k_m': {
        'path': r'C:\AI\GGUF\qwen2.5-coder-32b-instruct-q5_k_m.gguf',
        'contextsize': 8192,
        'gpulayers': 10
    },
    'Base: c4ai-command-r-08-2024-Q5_K_M (32.3B)': {
        'path': r'D:\BACKUP\AI\GGUF\c4ai-command-r-08-2024-Q5_K_M.gguf',
        'contextsize': 8192,
        'gpulayers': 10
    },
    'Qwen 2.5 FT: t-pro-it-1.0-q5_k_m (32.8B) - NOT ready-to-use': {
        'path': r'D:\BACKUP\AI\GGUF\t-pro-it-1.0-q5_k_m.gguf',
        'contextsize': 8192,
        'gpulayers': 10
    }
}

def run_model(model_name, model_info):
    command = [
        r'C:\AI\koboldcpp_cu12.exe',
        '--model', model_info['path'],
        '--threads', '6',
        '--usecublas', 'normal', 'mmq', '0',
        '--contextsize', str(model_info['contextsize']),
        '--gpulayers', str(model_info['gpulayers']),
        '--blasbatchsize', '512',
        '--blasthreads', '6',
        '--skiplauncher',
        '--multiuser', '2',
        '--quiet',
        '--password', 'yiff'
    ]
    
    try:
        subprocess.run(command, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Ошибка при запуске модели {model_name}: {e}")

def main():
    print("yiff-run-080125\n")
    for i, (model_name, model_info) in enumerate(models.items(), start=1):
        print(f"{i}. {model_name}")

    while True:
        try:
            choice = int(input("Введите номер модели: "))
            if 1 <= choice <= len(models):
                selected_model_name = list(models.keys())[choice - 1]
                break
            else:
                print("Неверный номер. Попробуйте снова.")
        except ValueError:
            print("Пожалуйста, введите число.")

    print("")
    subprocess.run(['taskkill', '/f', '/im', 'koboldcpp_cu12.exe'], check=False)
    print("")

    model_info = models[selected_model_name]
    run_model(selected_model_name, model_info)

if __name__ == "__main__":
    main()
