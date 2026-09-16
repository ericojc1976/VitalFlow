# VitalFlow 💚

**VitalFlow** é um aplicativo mobile de rastreamento de saúde e bem-estar desenvolvido em Python com Flet.

![VitalFlow](https://img.shields.io/badge/VitalFlow-Health%20App-teal)
![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)

---

## 🎯 Funcionalidades

✅ **Registrar Atividades**
- 💧 Consumo de água
- 🚶 Passos caminhados
- 🔥 Calorias consumidas
- 😴 Horas de sono

✅ **Acompanhar Progresso**
- Visualizar estatísticas diárias
- Dados salvos automaticamente
- Interface amigável e intuitiva

✅ **Lembretes**
- Notificações para beber água
- Lembrete de exercícios
- Alerta de sono

---

## 📥 Download e Instalação Rápida

### ⚡ Opção 1: Baixar APK Pronto (Recomendado)

1. **Acesse:** [Releases](https://github.com/ericojc1976/VitalFlow/releases)
2. **Baixe:** `vitalflow-*.apk`
3. **Abra no celular** e clique em "Instalar"

> ⚠️ Se aparecer "Fontes desconhecidas", vá em:
> `Configurações > Segurança > Fontes desconhecidas` ✅

---

### 🔨 Opção 2: Compilar Você Mesmo

**Pré-requisitos:**
- Python 3.8+
- Git
- 5GB espaço livre

#### Windows (PowerShell):
```powershell
git clone https://github.com/ericojc1976/VitalFlow.git
cd VitalFlow
.\build.bat
```

#### Mac/Linux (Terminal):
```bash
git clone https://github.com/ericojc1976/VitalFlow.git
cd VitalFlow
chmod +x build.sh
./build.sh
```

O arquivo APK será criado em `bin/`

---

### 🖥️ Opção 3: Testar no PC Primeiro

```bash
git clone https://github.com/ericojc1976/VitalFlow.git
cd VitalFlow
pip install -r requirements.txt
flet run main.py
```

---

## 📱 Como Usar o App

1. **Abra VitalFlow** no seu celular
2. **Registre suas atividades:**
   - Clique em **+250ml** para adicionar água
   - Clique em **+100** para adicionar passos
   - Clique em **+100** para registrar calorias
   - Clique em **+30min** para anotar sono

3. **Visualize seu progresso:**
   - Seus dados são salvos automaticamente
   - Verifique as metas diárias
   - Acompanhe sua evolução

---

## 📁 Estrutura do Projeto

```
VitalFlow/
├── main.py                 # Código principal
├── requirements.txt        # Dependências
├── buildozer.spec         # Config de build
├── build.sh               # Script Linux/Mac
├── build.bat              # Script Windows
├── README.md              # Este arquivo
├── DOWNLOAD.md            # Guia de download
├── INSTALLATION.md        # Guia de instalação
└── vitalflow_data.json    # Dados salvos (auto)
```

---

## 🔧 Tecnologias

- **Python 3.8+** - Linguagem de programação
- **Flet** - Framework UI multiplataforma
- **JSON** - Armazenamento de dados local
- **Buildozer** - Compilador para Android/iOS

---

## 📊 Requisitos do Celular

| Requisito | Valor |
|-----------|-------|
| Android | 5.0+ |
| iOS | 12.0+ |
| Espaço | ~50MB |
| RAM | 100MB mín |

---

## 🚀 Roadmap Futuro

- [ ] Banco de dados SQLite
- [ ] Gráficos avançados
- [ ] Notificações push
- [ ] Sincronização na nuvem
- [ ] Compartilhamento de progresso
- [ ] Integração com wearables
- [ ] Modo offline completo
- [ ] Múltiplos usuários

---

## 🤝 Como Contribuir

1. **Fork** o repositório
2. **Crie uma branch:** `git checkout -b feature/NovaFuncao`
3. **Commit:** `git commit -m 'Add NovaFuncao'`
4. **Push:** `git push origin feature/NovaFuncao`
5. **Pull Request:** Abra um PR

---

## 📝 Licença

MIT License - veja [LICENSE](LICENSE) para detalhes

---

## 👨‍💻 Autor

**ericojc1976** - VitalFlow Developer

---

## 💬 Suporte

Tem dúvidas? Abra uma [Issue](https://github.com/ericojc1976/VitalFlow/issues) no GitHub!

### Perguntas Frequentes:

**P: O app funciona offline?**
R: Sim! Todos os dados são salvos localmente.

**P: Meus dados são sincronizados?**
R: Não, mas em versões futuras teremos sincronização na nuvem.

**P: É seguro?**
R: Sim! Os dados ficam apenas no seu celular.

**P: Quanto custa?**
R: Totalmente gratuito e open-source!

---

## 🎉 Comece Agora!

```bash
# Clone e execute em 3 passos
git clone https://github.com/ericojc1976/VitalFlow.git
cd VitalFlow
pip install -r requirements.txt && flet run main.py
```

Ou [baixe o APK](https://github.com/ericojc1976/VitalFlow/releases) pronto!

---

**Desenvolvido com ❤️ para sua saúde e bem-estar**

⭐ Se você gostou, deixe uma estrela! ⭐
