from time import sleep
from rich.console import Console

console = Console()
tasks = [f"Успешно запущено!" for n in range(1, 2)]

with console.status("[bold green]Запуск DDoS, пожалуйста, подождите несколько секунд...[/bold green]") as status:
    while tasks:
        task = tasks.pop(0)
        sleep(5)
        console.log(f"{task} DDoS")
