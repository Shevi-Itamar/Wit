import os

from Modul import Create_a_new_folder
from Repository import repository
import click

repository = repository()

@click.group()

def cli():
    pass

@click.command()
def init():
    if not os.path.exists(os.path.join(os.getcwd(),'.wit')):
        Create_a_new_folder(os.getcwd(),'.wit')

@click.command()
@click.argument('path')
def add(path):
    repository.add(path)

@click.command()
@click.argument('message')
def commit(message):
    repository.commit(message)

@click.command()
def log():
    repository.log()

@click.command()
def status():
    repository.status()


@click.command()
@click.argument('commit_id')
def check_out(commit_id):
    repository.check_out(commit_id)


cli.add_command(init)
cli.add_command(add)
cli.add_command(check_out)
cli.add_command(status)
cli.add_command(log)
cli.add_command(commit)

if __name__=='__main__':
    cli()
    init()
    repository.add(r'C:\Users\Yoga\Desktop\Node.js\lesson7\app.js')
    repository.commit("e")





