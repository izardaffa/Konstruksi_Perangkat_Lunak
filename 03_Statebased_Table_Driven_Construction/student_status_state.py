from enum import Enum

class StudentStatusState(Enum):
    TERDAFTAR = "Terdaftar"
    CUTI = "Cuti"
    AKTIF = "Aktif"
    LULUS = "Lulus"

class TriggerInputState(Enum):
    CETAK_KSM = "Cetak KSM"
    MENYELESAIKAN_CUTI = "Menyelesaikan Cuti"
    LULUS = "Lulus"
    MENGAJUKAN_CUTI = "Mengajukan Cuti"

state_transitions = {
    StudentStatusState.TERDAFTAR: {
        TriggerInputState.CETAK_KSM: StudentStatusState.AKTIF,
        TriggerInputState.MENGAJUKAN_CUTI: StudentStatusState.CUTI,
    },
    StudentStatusState.CUTI: {
        TriggerInputState.MENYELESAIKAN_CUTI: StudentStatusState.TERDAFTAR,
    },
    StudentStatusState.AKTIF: {
        TriggerInputState.LULUS: StudentStatusState.LULUS,
        TriggerInputState.MENGAJUKAN_CUTI: StudentStatusState.CUTI,
    },
}

def change_state(current_state, trigger_input):
    cond_1 = current_state in state_transitions
    cond_2 = trigger_input in state_transitions[current_state]
    
    if cond_1 and cond_2:
        return state_transitions[current_state][trigger_input]
    return "Transisi tidak valid"

current_state = StudentStatusState.AKTIF
triger_input = TriggerInputState.CETAK_KSM

next_state = change_state(current_state, triger_input)
print(next_state) # Aktif
