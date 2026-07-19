# Registro de Temperatura e Umidade com ESP32

Projeto para leitura de temperatura e umidade com ESP32, exibição em interface gráfica com Tkinter e registro básico das medições em arquivo CSV.

## Funcionalidades

- Leitura de dados pela porta serial.
- Exibição de temperatura e umidade em tempo real.
- Registro de dados com data e hora em arquivo CSV.

## Arquivos do projeto

- `ui.py`: interface gráfica do sistema.
- `recepcao_dados.py`: leitura dos dados recebidos da ESP32 via serial.
- `registro_excel.py`: geração de arquivo CSV com as medições.
- `leitura_temp_umidade.py`: teste simples de execução na ESP32.
- `descricao.txt`: descrição curta do projeto para uso no Git.

## Requisitos

- Python 3
- Tkinter
- pyserial
- ESP32 conectada na porta serial configurada no código

## Como executar

1. Conecte a ESP32 ao computador.
2. Ajuste a porta serial em `recepcao_dados.py`, se necessário.
3. Execute a interface:

```bash
python3 ui.py
```

4. Para gerar um arquivo CSV de teste:

```bash
python3 registro_excel.py
```

## Observação

Atualmente, o registro em CSV usa dados simulados no arquivo `registro_excel.py`, enquanto a interface lê dados seriais em tempo real.
