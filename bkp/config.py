class Config:
    index_from = 1
    suffix_format = '.b{i:02}'
    suffix_regexp = '\.b(\d+)$'
    time_format = '{t.Y}-{t.m}-{t.d} {t.H}:{t.M}:{t.S} {t.Z_}'

cfg = Config()
