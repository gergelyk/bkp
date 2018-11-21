from plumbum import local as sh


def test_restore_file_from_backup():
    with sh.tempdir() as tmp:
        with sh.cwd(tmp):
            (sh['echo']['abc'] > 'myfile.txt')()
            sh['bkp']('myfile.txt')

            (sh['echo']['def'] > 'myfile.txt')()
            sh['bkp']('myfile.txt')

            sh['bkp']('-ry', 'myfile.txt.b01')
            sh['grep']('abc', 'myfile.txt')

            sh['bkp']('-ry', 'myfile.txt.b02')
            sh['grep']('def', 'myfile.txt')

def test_restore_dir_from_backup():
    with sh.tempdir() as tmp:
        with sh.cwd(tmp):
            sh['mkdir']('mydir')
            sh['touch']('mydir/abc')
            sh['touch']('mydir/def')
            sh['touch']('mydir/ghi')

            sh['bkp']('mydir')

            (sh['ls']['-1', 'mydir'] | sh['grep']['abc'] )()
            (sh['ls']['-1', 'mydir'] | sh['grep']['def'] )()
            (sh['ls']['-1', 'mydir'] | sh['grep']['ghi'] )()

            sh['rm']('mydir/abc')
            sh['rm']('mydir/def')
            sh['rm']('mydir/ghi')

            sh['bkp']('-ry', 'mydir.b01')

            (sh['ls']['-1', 'mydir'] | sh['grep']['abc'] )()
            (sh['ls']['-1', 'mydir'] | sh['grep']['def'] )()
            (sh['ls']['-1', 'mydir'] | sh['grep']['ghi'] )()

def test_restore_file_from_archive():
    with sh.tempdir() as tmp:
        with sh.cwd(tmp):
            (sh['echo']['abc'] > 'myfile.txt')()
            sh['bkp']('-a', 'myfile.txt')

            (sh['echo']['def'] > 'myfile.txt')()
            sh['bkp']('-a', 'myfile.txt')

            sh['bkp']('-ry', 'myfile.txt.b01')
            sh['grep']('abc', 'myfile.txt')

            sh['bkp']('-ry', 'myfile.txt.b02')
            sh['grep']('def', 'myfile.txt')

def test_restore_dir_from_archive():
    with sh.tempdir() as tmp:
        with sh.cwd(tmp):
            sh['mkdir']('mydir')
            sh['touch']('mydir/abc')
            sh['touch']('mydir/def')
            sh['touch']('mydir/ghi')

            sh['bkp']('-a', 'mydir')

            (sh['ls']['-1', 'mydir'] | sh['grep']['abc'] )()
            (sh['ls']['-1', 'mydir'] | sh['grep']['def'] )()
            (sh['ls']['-1', 'mydir'] | sh['grep']['ghi'] )()

            sh['rm']('mydir/abc')
            sh['rm']('mydir/def')
            sh['rm']('mydir/ghi')

            sh['bkp']('-ry', 'mydir.b01')

            (sh['ls']['-1', 'mydir'] | sh['grep']['abc'] )()
            (sh['ls']['-1', 'mydir'] | sh['grep']['def'] )()
            (sh['ls']['-1', 'mydir'] | sh['grep']['ghi'] )()
