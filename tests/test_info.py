from plumbum import local as sh


def test_read_message():
    with sh.tempdir() as tmp:
        with sh.cwd(tmp):
            (sh['echo']['abc'] >> 'myfile.txt')()

            sh['bkp']('-am', 'Foo', 'myfile.txt')
            sh['bkp']('-am', 'Bar', 'myfile.txt')
            sh['bkp']('-am', 'Baz', 'myfile.txt')

            (sh['bkp']['-i', 'myfile.txt.b01'] | sh['grep']['Foo'] )()
            (sh['bkp']['-i', 'myfile.txt.b02'] | sh['grep']['Bar'] )()
            (sh['bkp']['-i', 'myfile.txt.b03'] | sh['grep']['Baz'] )()
