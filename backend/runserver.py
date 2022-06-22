import socket, subprocess
from setup.env import get_ip_address

PORT = '8000'

def put_ip_in_env_file(folder: str, file_name='.env', file_pattern='API_URL'):
    '''Put ip address in .env'''
    file_path = fr'../{ folder }/{ file_name }'

    with open(file_path, 'r+') as f:
        lines = f.readlines()
        f.seek(0)

        for line in lines:
            if not line.startswith(file_pattern):
                f.write(line)
            else:
                f.write(f'{ file_pattern }=http://{ get_ip_address() }:{ PORT }\n')
        f.truncate()


def main():
    '''Run'''
    # subprocess.call(f'python manage.py runserver { get_ip_address() }:{ PORT }', shell=True)
    subprocess.call(f'python manage.py runserver { PORT }', shell=True)


if __name__ == '__main__':
    # put_ip_in_env_file('web', file_pattern='REACT_APP_API_URL')
    main()