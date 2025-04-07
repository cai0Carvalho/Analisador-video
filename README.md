# 🧠 Resumo Automático de Vídeos do YouTube com Python

Este projeto permite **baixar o áudio de um vídeo do YouTube**, transcrever automaticamente com **Whisper (OpenAI)** e gerar um **resumo formatado em Markdown** com a ajuda do modelo **GPT-4**.

---

## 📦 Tecnologias Utilizadas

- [Python](https://www.python.org/)
- [pytubefix](https://pypi.org/project/pytubefix/) — para baixar o vídeo
- [ffmpeg-python](https://github.com/kkroening/ffmpeg-python) — para processar o áudio
- [OpenAI API](https://platform.openai.com/docs) — para transcrição e geração de resumo

---

## 🚀 Como Usar

### 1. Clone o repositório:

```bash
git clone https://github.com/cai0Carvalho/Analisador-video.git
cd Analisador-video
```

### 2. Instale as dependências:

```bash
pip install pytubefix ffmpeg-python openai
```

### 3. Instale o FFmpeg:

- **Linux (Ubuntu/Debian):**
  ```bash
  sudo apt install ffmpeg
  ```

- **macOS (com Homebrew):**
  ```bash
  brew install ffmpeg
  ```

- **Windows:**
  Baixe em: [https://ffmpeg.org/download.html](https://ffmpeg.org/download.html)  
  E adicione o binário ao seu PATH.

---

### 4. Configure sua chave da OpenAI

Crie a variável de ambiente com sua chave da OpenAI:

#### Linux/macOS:
```bash
export OPENAI_API_KEY="sua-chave-aqui"
```

#### Windows (CMD):
```cmd
set OPENAI_API_KEY=sua-chave-aqui
```

---

### 5. Execute o script

```bash
python resumidor.py https://www.youtube.com/watch?v=VIDEO_ID
```

> 📁 O resumo será salvo como `resumo.md` no mesmo diretório.

---

## 🧾 Exemplo de Saída (resumo.md)

```markdown
# 🧠 Resumo do Vídeo

**🎥 URL do vídeo:** [Clique aqui](https://www.youtube.com/watch?v=...)

---

## ✏️ Transcrição Resumida

O vídeo discute conceitos de machine learning, incluindo algoritmos supervisionados, regressão linear e redes neurais. O apresentador explica como os dados são processados...

---
```

---

Desenvolvido por Caio Carvalho 🚀
