from plumbum import local as sh


def test_backup_file():
    with sh.tempdir() as tmp:
        with sh.cwd(tmp):
            (sh['echo']['abc'] >> 'myfile.txt')()

            dir_content = sh['ls']('-1').splitlines()
            assert dir_content == ['myfile.txt']

            sh['bkp']('myfile.txt')
            sh['bkp']('myfile.txt')
            sh['bkp']('myfile.txt')

            (sh['echo']['cba'] >> 'myfile.txt')()
            sh['bkp']('myfile.txt')

            sh['rm']('myfile.txt.b02')
            sh['bkp']('myfile.txt')

            dir_content = sh['ls']('-1').splitlines()
            assert set(dir_content) == {'myfile.txt',
                                        'myfile.txt.b01',
                                        'myfile.txt.b03',
                                        'myfile.txt.b04',
                                        'myfile.txt.b05'}

            sh['diff']('myfile.txt.b01', 'myfile.txt.b03')
            sh['diff']('myfile.txt', 'myfile.txt.b04')
            sh['diff']('myfile.txt', 'myfile.txt.b05')


def test_backup_multiple_files():
    with sh.tempdir() as tmp:
        with sh.cwd(tmp):
            (sh['echo']['abc'] >> 'myfile1.txt')()
            (sh['echo']['abc'] >> 'myfile2.txt')()

            dir_content = sh['ls']('-1').splitlines()
            assert dir_content == ['myfile1.txt',
                                   'myfile2.txt']

            sh['bkp']('myfile1.txt', 'myfile2.txt')

            dir_content = sh['ls']('-1').splitlines()
            assert set(dir_content) == {'myfile1.txt',
                                        'myfile2.txt',
                                        'myfile1.txt.b01',
                                        'myfile2.txt.b01'}

def test_backup_dir():
    with sh.tempdir() as tmp:
        with sh.cwd(tmp):
            sh['mkdir']('mydir')
            sh['touch']('mydir/abc')
            sh['touch']('mydir/def')
            sh['touch']('mydir/ghi')

            dir_content = sh['ls']('-1').splitlines()
            assert set(dir_content) == {'mydir'}

            dir_content = sh['ls']('-1', 'mydir').splitlines()
            assert set(dir_content) == {'abc', 'def', 'ghi'}

            sh['bkp']('mydir')

            dir_content = sh['ls']('-1').splitlines()
            assert set(dir_content) == {'mydir', 'mydir.b01'}

            dir_content = sh['ls']('-1', 'mydir.b01').splitlines()
            assert set(dir_content) == {'abc', 'def', 'ghi'}


def test_archive_file():
    with sh.tempdir() as tmp:
        with sh.cwd(tmp):
            (sh['echo']['abc'] >> 'myfile.txt')()
            sh['bkp']('-a', 'myfile.txt')
            tar_content = sh['tar']('-t', '-f', 'myfile.txt.b01').splitlines()
            assert set(tar_content) == {'DATA', 'INFO', 'META'}
            sh['tar']('xf', 'myfile.txt.b01')
            assert sh['cat']('DATA') == 'abc\n'
            assert eval(sh['cat']('META')) == {'file_type': 'backup', 'file_version': '1.0.0'}


def test_archive_dir():
    with sh.tempdir() as tmp:
        with sh.cwd(tmp):
            sh['mkdir']('mydir')
            sh['touch']('mydir/abc')
            sh['touch']('mydir/def')
            sh['touch']('mydir/ghi')
            sh['bkp']('-a', 'mydir')
            tar_content = sh['tar']('-t', '-f', 'mydir.b01').splitlines()
            assert set(tar_content) == {'DATA/', 'INFO', 'META',
                                        'DATA/abc', 'DATA/def', 'DATA/ghi'}
