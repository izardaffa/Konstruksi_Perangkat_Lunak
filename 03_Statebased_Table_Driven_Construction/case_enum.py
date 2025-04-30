from enum import Enum

class JenisKelamin(Enum):
    LAKI_LAKI = 1
    PEREMPUAN = 2

print(JenisKelamin.LAKI_LAKI)           # output => JenisKelamin.LAKI_LAKI
print(JenisKelamin.LAKI_LAKI.value)     # output => 1
print(JenisKelamin.LAKI_LAKI.name)      # output => LAKI_LAKI
