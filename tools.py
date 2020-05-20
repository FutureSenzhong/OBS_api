# coding=utf-8
'''
# Author: shikanon (shikanon@tensorbytes.com)
# File Created Time: 2020-03-31 5:12:50
# 
# Project: FastAPI-Project-Template
# File: tools.py
# Description: 
# 
'''

import click

from settings.config import Config
from model.database import Database


@click.group()
def cli():
    pass

@click.command()
@click.option('--path', default="config.ini", help='path of config')
def initdb(path):
    conf = Config()
    conf.parse(path)
    db = Database(conf.mysqldb)
    db.create_table()
    click.echo('Initialized the database')


@click.command()
@click.option('--path', default="config.ini", help='path of config')
def dropdb(path):
    conf = Config()
    conf.parse(path)
    db = Database(conf.mysqldb)
    db.drop_table()
    click.echo('Dropped the database')

cli.add_command(initdb)
cli.add_command(dropdb)

if __name__ == '__main__':
    cli()