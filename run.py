import click
from app import app, db


@click.command(name='create-db')
def create_db():
    """Create database tables"""
    from app.models import User
    db.create_all()
    click.echo('Tables created')


app.cli.add_command(create_db)


@click.command(name='clear-db')
def clear_db():
    """Drop database tables"""
    from app.models import User
    db.drop_all()
    click.echo('Database cleared')


app.cli.add_command(clear_db)


if __name__ == '__main__':
    app.run(debug=True)
