from enum import Enum
import time

class TrafficLightState(Enum):
    MERAH = "Merah"
    KUNING = "Kuning"
    HIJAU = "Hijau"

state_duration = {
    TrafficLightState.MERAH: 6,
    TrafficLightState.HIJAU: 3,
    TrafficLightState.KUNING: 1,
}

state_transition = {
    TrafficLightState.MERAH: TrafficLightState.HIJAU,
    TrafficLightState.HIJAU: TrafficLightState.KUNING,
    TrafficLightState.KUNING: TrafficLightState.MERAH,
}

current_state = TrafficLightState.KUNING
next_state = state_transition[current_state]
print(next_state)

current_state = TrafficLightState.MERAH
while True:
    print(f"Traffic Light: {current_state.value}")
    time.sleep(state_duration[current_state])
    current_state = state_transition[current_state]
