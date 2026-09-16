# VitalFlow Installation Guide - Guia Completo de Instalação

## 📱 Para Instalar no Seu Celular

### Opção 1: Android (Recomendado)

#### Passo 1: Instale o Python e Ferramentas
```bash
# Windows - use PowerShell como administrador
python --version  # Verifique se Python 3.8+ está instalado

# Mac/Linux
python3 --version
```

#### Passo 2: Clone o Projeto
```bash
git clone https://github.com/ericojc1976/VitalFlow.git
cd VitalFlow
```

#### Passo 3: Instale Dependências
```bash
pip install -r requirements.txt
pip install buildozer cython
```

#### Passo 4: Crie o APK
```bash
# Configure o buildozer (primeira vez)
buildozer android debug

# Espere o processo completar (pode levar 10-15 minutos)
```

#### Passo 5: Instale no Celular
- O arquivo `.apk` estará em: `bin/vitalflow-0.1-debug.apk`
- Envie para seu celular via Bluetooth, Email ou USB
- Abra o arquivo e clique em "Instalar"
- Permita instalação de fontes desconhecidas

---

### Opção 2: iOS (Mac apenas)

```bash
# Instale ferramentas
pip install buildozer cython

# Compile para iOS
buildozer ios debug

# O arquivo `.ipa` será criado em `bin/`
```

---

### Opção 3: Executar no PC/Mac (Teste antes de compilar)

```bash
# Clone o repositório
git clone https://github.com/ericojc1976/VitalFlow.git
cd VitalFlow

# Instale dependências
pip install -r requirements.txt

# Execute
flet run main.py
```

---

## 🔧 Configuração do Buildozer (Android)

Se encontrar problemas, crie um arquivo `buildozer.spec`:

```bash
buildozer init
```

Edite o arquivo e procure por:
- `package.name = vitalflow`
- `package.domain = org.vitalflow`
- `source.dir = .`
- `requirements = python3,kivy,flet`

---

## ⚠️ Solução de Problemas

### Erro: "Python não encontrado"
- Windows: Reinstale Python marcando "Add Python to PATH"
- Mac/Linux: Use `python3` em vez de `python`

### Erro ao compilar Android
```bash
# Limpe cache e compile novamente
buildozer android debug --clean
```

### Porta ocupada
```bash
# Windows
netstat -ano | findstr :8000

# Mac/Linux
lsof -i :8000
```

---

## 📲 Requisitos do Celular

- **Android:** 5.0+ (API 21+)
- **iOS:** 12.0+
- **Espaço:** ~50MB

---

## 🎯 Próximos Passos

1. ✅ Instale o app
2. 📊 Comece a registrar suas atividades
3. 📈 Acompanhe seu progresso
4. 🎉 Alcance suas metas!

---

## 💡 Dicas

- Use o app todos os dias para melhores resultados
- Configure lembretes para não esquecer
- Compartilhe seu progresso com amigos

**Desenvolvido com ❤️ para sua saúde!**
