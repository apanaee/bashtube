from bashtube import create_app
from bashtube.models import db,Users
import sys
app = create_app()


def database():
    arg = sys.argv[1]

    if arg == '--help' or arg == '-h':
        print('Help:')
        print('init --> To create tables to your database ')
        print('drop --> To remove tables to your database ')
        print('create_superuser --> create superuser')
    elif arg == 'init':
        print('Creating database....')
        with app.app_context():
            db.create_all()

    elif arg == 'drop':
        print('Dropping database...')
        with app.app_context():
            db.drop_all()

    elif arg == 'create_superuser':
        print('This should create super user .....')
        username = str(input('Username :')).lower()
        while not username:
            username = str(input('Username (Please Fill This):'))

        password = str(input('Password :'))
        while not password:
            password = str(input('Password (Please Fill This):'))

        email = str(input('Email Address:'))
        print(f'----> Information <-----\n Username -> {username} '
              f'\n Password -> {password} \n Email Address -> {email}')

        confirm = str(input('Do you want to save this information (y/n) :'))

        if confirm.lower() == 'y':
            print('Committing User Information ...')
            user = Users(username=username,password=password,email=email,role='A')
            db.session.add(user)
            db.session.commit()
            print('Commit Complete ...')
        else:
            print('Cancelling action ....')

    else:
        print('--------------> invalid command <--------------- ')


if __name__ == "__main__":
    database()