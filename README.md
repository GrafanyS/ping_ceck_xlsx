# Ping check servers

Status of Last Deployment:<br>
<img src="https://github.com/GrafanyS/ping_ceck_xlsx/workflows/Python-application/badge.svg?branch=main"><br>
[![Python-application]("https://github.com/GrafanyS/ping_ceck_xlsx/workflows/python-app.yml"](https://github.com/GrafanyS/ping_ceck_xlsx/github/workflows/python-app.yml/badge.svg)
[![GitHub Sigstore Prober](https://github.com/actions/attest-build-provenance/actions/workflows/prober-github.yml/badge.svg)](https://github.com/actions/attest-build-provenance/actions/workflows/prober-github.yml)






Copyleft by Andrei Valetov 2023.

**Purpose:** Pings all the servers in a specified column in a `.xlsx` file. 

I used it to check if `500+ servers` were online/responsive. 

**Warnings:**
*I used this for one particular dataset, so I might be ignoring certain cell values for seemingly unknown reasons or 
not-error checking for seemingly obvious things. Feel free to submit a PR to make this more generally useful. 
*This ideally should be using my `ExcelColumnHeaders` project as an import but is not currently. 
*`pingExcelList.py` currently assumes there is a `.xlsx` file in the project directory. 
	    
**Requirements:** `openpyxl` module must be installed. The easiest method I have found is `pip install openpyxl`.
	    
**Usage**: Run `python pingExcelList.py`. Currently, assumes there is a `.xlsx` file in the project directory. 

----------

**Назначение:** Проверяет все серверы в указанном столбце в файле `.xlsx`.

Я использовал его, чтобы проверить, подключены ли "500+ серверов" к Сети / реагируют ли они.

**Предупреждения:**
* Я использовал это для одного конкретного набора данных, поэтому я мог игнорировать определенные значения ячеек по, 
казалось бы, неизвестным причинам или
не проверять ошибки для, казалось бы, очевидных вещей. Не стесняйтесь отправлять PR, чтобы сделать это более полезным в 
целом.
** В идеале это должно быть использование моего проекта "Заголовки столбцов Excel" в качестве импорта, но в настоящее 
время этого нет.
*`pingExcelList.py` в настоящее время предполагается, что в каталоге проекта есть файл `.xlsx`.

** Требования:** Должен быть установлен модуль openpyxl. Самый простой метод, который я нашел, - это 
`pip install openpyxl`.

**Использование**: Запустите `python pingExcelList.py`. В настоящее время предполагается, что в каталоге проекта есть 
файл `.xlsx`.

### Инструменты разработки

**Стек:**
- Python >= 3;
- Пакеты из файла requirements.txt;

### Разработка

##### 1) Клонировать репозиторий

    git clone ссылка_сгенерированная_в_вашем_репозитории

##### 2) Создать виртуальное окружение

    python -m venv venv
    
##### 3) Активировать виртуальное окружение

##### 4) Устанавливить зависимости:

    pip install -r requirements.txt

Copyright (c) 2023-present, Valetov Andrei
