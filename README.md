## LibCLI

Система управления библиотекой.

### Установка

```bash
py -m venv venv
source venv/bin/activate
pip install git+https://github.com/bqio/libcli.git
```

### Команды

Показать список всех книг

```bash
libcli show
```

Добавить новую книгу

```bash
libcli add [title] [author] [year]
```

Удалить книгу по её ID

```bash
libcli delete [ID]
```

Изменить статус книги

```bash
libcli change [ID] [status(выдана,в наличии)]
```

Поиск книги

```bash
libcli search [query]
```

### Тесты

```bash
py tests.py -v
```
