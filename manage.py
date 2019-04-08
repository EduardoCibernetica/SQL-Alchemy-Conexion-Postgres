#!/usr/bin/env python
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
import application


db = application.db
ap = application.app

migrate = Migrate(ap, db)

manager = Manager(ap)
manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()
