import os
import re
import random
import datetime
from sys import argv


def write_log(filename='log_file.log'):
    file = open(filename, 'w')

    count_peoples = random.randint(0, 10)

    volume = random.randint(100, 500) # объем бочки
    current_volume = random.randint(0, 500) #текущий объем
    file.writelines(f'{volume} (Объем бочки)\n')
    file.writelines(f'{current_volume} (Текущий объем)\n')

    while os.path.getsize(filename) < 1024*1024:

        action = ''
        result = ''
        probability = random.random()
        need_volume = random.randint(0, 500)
        if probability > 0.5:
            action = 'top up'
            if need_volume + current_volume > volume:
                result = 'fail'
            else:
                result = 'success'
                current_volume += need_volume
        else:
            action = 'scoop'
            if current_volume - need_volume < 0:
                result = 'fail'
            else:
                result = 'success'
                current_volume -= need_volume

        current_time = datetime.datetime.now().strftime('%Y-%m-%dT%H:%M:%S')

        user = random.randint(1, count_peoples)

        file.writelines(f'{current_time}-[username{user}]-wanna {action} {need_volume}L ({result}) {current_volume}L\n')

    file.close()
    print (f'file {filename} is recorded')


def read_log(file_name, start_time, end_time):

    # перевод в формат timestamp
    format_start_time = datetime.datetime.strptime(start_time, '%Y-%m-%dT%H:%M').timestamp()
    format_end_time = datetime.datetime.strptime(end_time, '%Y-%m-%dT%H:%M').timestamp()

    try:
        file = open(file_name, 'r')
    except:
        print('[ERROR] File is not found')
        return 0

    count_attempt = 0
    success_attempt = 0
    success_topUp = 0
    fail_topUp = 0
    success_scoop = 0
    fail_scoop = 0
    current_volume_begin = 0
    current_volume_end = 0

    pattern_log = re.compile('^(\d+-\d+-\d+T\d+:\d+:\d+)-\[\w+\d+\]-wanna (\w+|\w+ \w+) (\d+)L \((\w+)\) (\d+)L$')

    for line in file:

        line = line.replace('\n', '')

        result = re.match(pattern_log, line)

        if result:
            current_volume_end = result.group(5)
            format_current_time = datetime.datetime.strptime(result.group(1), '%Y-%m-%dT%H:%M:%S').timestamp()
            if format_current_time <= format_start_time:
                continue
            if format_current_time >= format_end_time:
                break

            if count_attempt == 0:
                current_volume_begin = result.group(5)

            count_attempt += 1
            if result.group(4) == 'success':
                success_attempt += 1
                if result.group(2) == 'top up':
                    success_topUp += int(result.group(3))
                else:
                    success_scoop += int(result.group(3))
            else:
                if result.group(2) == 'top up':
                    fail_topUp += int(result.group(3))
                else:
                    fail_scoop += int(result.group(3))

    if count_attempt > 0:
        print(f'Объем на начало времени: {current_volume_begin}')
        print(f'Объем на конец времени: {current_volume_end}')
        print(f'Процент успешных попыток: {success_attempt*100/count_attempt} %')
        print(f'Успешный налитый объем: {success_topUp} литров')
        print(f'Успешные зачерпывания: {success_scoop} литров')
        print(f'Неуспешные наливы: {fail_topUp} литров')
        print(f'Неуспешные зачерпывания: {fail_scoop} литров')
    else:
        print('За указанный период записей не найдено')

    file.close()


if __name__ == '__main__':
    time_pattern = re.compile('\d+-\d+-\d+T\d+:\d+')
    usage = """
   [ERROR] please enter: python3 script.py filename start time end time.
   Example: read log: python3 task3.py ./log_file.log 2021-07-13T00:00 2021-07-15T00:00
            write log: python3 task.py write filename
            filename not required
    """

    if len(argv) > 1:

        #try:
        if 2>1:
            if argv[1] == 'write':
                if len(argv) == 3:
                    write_log(argv[2])
                else:
                    write_log()
            else:
                if not re.match(time_pattern, argv[2]) or not re.match(time_pattern, argv[3]):
                    print(usage)
                else:
                    read_log(argv[1], argv[2], argv[3])
        #except:
        #    print(usage)
    else:
        print(usage)
