# VitalFlow 💚

**VitalFlow** é um aplicativo mobile de rastreamento de saúde e bem-estar desenvolvido em Python com Flet.

## 🎯 Funcionalidades

✅ **Registrar Atividades**
- 💧 Consumo de água
- 🚶 Passos caminhados
- 🔥 Calorias consumidas
- 😴 Horas de sono

✅ **Acompanhar Progresso**
- Visualizar estatísticas diárias
- Gráficos de evolução
- Metas personalizadas

✅ **Lembretes**
- Notificações para beber água
- Lembrete de exercícios
- Alerta de sono

## 🚀 Instalação

### Pré-requisitos
- Python 3.8+
- pip (gerenciador de pacotes)

### Passo a passo

1. **Clone o repositório:**
```bash
git clone https://github.com/ericojc1976/VitalFlow.git
cd VitalFlow
```

2. **Instale as dependências:**
```bash
pip install -r requirements.txt
```

3. **Execute a aplicação (Windows/Mac/Linux):**
```bash
flet run main.py
```

## 📱 Compilar para Android/iOS

### Android
```bash
flet build apk
```

O arquivo `.apk` será gerado na pasta `build/`.

### iOS
```bash
flet build ipa
```

## 📖 Como Usar

1. **Abra o app**
2. **Registre suas atividades:**
   - Digite a quantidade de água (em litros)
   - Insira seus passos
   - Registre calorias consumidas
   - Anote horas de sono
3. **Clique em "Salvar Dados"**
4. **Acompanhe seu progresso** na aba de estatísticas

## 🏗️ Estrutura do Projeto

```
VitalFlow/
├── main.py              # Arquivo principal
├── requirements.txt     # Dependências
├── README.md           # Documentação
└── vitalflow_data.json # Dados salvos (gerado automaticamente)
```

## 🔧 Tecnologias

- **Python 3.8+**
- **Flet** - Framework para UI multiplataforma
- **JSON** - Armazenamento de dados local

## 📝 Roadmap Futuro

- [ ] Banco de dados SQLite
- [ ] Notificações push
- [ ] Gráficos avançados
- [ ] Sincronização na nuvem
- [ ] Compartilhamento de progresso
- [ ] Modo offline melhorado
- [ ] Integração com wearables

## 🤝 Contribuir

Contribuições são bem-vindas! Por favor:

1. Fork o repositório
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 📄 Licença

Este projeto está sob a licença MIT.

## 👨‍💻 Autor

**ericojc1976** - VitalFlow Developer

## 💬 Suporte

Tem dúvidas? Abra uma [Issue](https://github.com/ericojc1976/VitalFlow/issues) no GitHub!

---

**Desenvolvido com ❤️ para sua saúde**
