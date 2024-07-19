import numpy as np
from scipy.io.wavfile import write
#pip install numpy scipy
def gerar_onda_quadrada(frequencia, duracao, taxa_amostragem=44100):
    """
    Gera uma onda quadrada com a frequência e duração especificadas.
    
    Args:
    - frequencia: Frequência da onda quadrada em Hz.
    - duracao: Duração da onda em segundos.
    - taxa_amostragem: Taxa de amostragem (samples per second), padrão é 44100 Hz.
    
    Returns:
    - samples: Amostras da onda quadrada.
    """
    t = np.linspace(0, duracao, int(taxa_amostragem * duracao), endpoint=False)
    samples = 0.5 * (1 + np.sign(np.sin(2 * np.pi * frequencia * t)))
    return samples

def main():
    # Input dos valores
    frequencia = float(input("(100 Hz > 40 kHz): "))
    duracao = float(input("seconds: "))
    
    # Validação dos valores de entrada
    if not (100 <= frequencia <= 40000):
        print(" 100 Hz > 40 kHz.")
        return
    if duracao <= 0:
        print("> 0 seconds.")
        return
    
    # Gerar a onda quadrada
    samples = gerar_onda_quadrada(frequencia, duracao)
    
    # Normalizar para a faixa de -32768 a 32767 (int16)
    samples = np.int16((samples - 0.5) * 2 * 32767)
    
    # Salvar o arquivo WAV
    nome_arquivo = "onda_quadrada.wav"
    write(nome_arquivo, 44100, samples)
    
    print(f"Arquivo '{nome_arquivo}' ok!")

print("\x1bc\x1b[47;34m")
if __name__ == "__main__":
    main()

