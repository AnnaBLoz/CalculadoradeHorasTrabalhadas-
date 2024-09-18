from datetime import datetime, timedelta

def validar_horario(hora: str) -> bool:
    """Valida se o horário está no formato HH:mm, H:mm, ou HHmm."""
    try:
        if len(hora) == 5 and ':' in hora:
            datetime.strptime(hora, '%H:%M')
        elif len(hora) == 4 and ':' not in hora:
            datetime.strptime(hora, '%H%M')
        elif len(hora) == 4 and ':' in hora:
            datetime.strptime(hora, '%H:%M')
        else:
            return False
        return True
    except ValueError:
        return False

def converter_para_datetime(hora: str) -> datetime:
    """Converte a string de hora em um objeto datetime, aceitando diferentes formatos."""
    if len(hora) == 4 and ':' not in hora:
        return datetime.strptime(hora, '%H%M')
    else:
        return datetime.strptime(hora, '%H:%M')

def calcular_horas_trabalhadas(inicio: str, fim: str) -> timedelta:
    """Calcula a diferença entre os horários de início e fim, aceitando inversão de horários."""
    if not (validar_horario(inicio) and validar_horario(fim)):
        raise ValueError("Horários inválidos")
    
    inicio_dt = converter_para_datetime(inicio)
    fim_dt = converter_para_datetime(fim)
    
    if fim_dt < inicio_dt:
        fim_dt += timedelta(days=1)
    
    return fim_dt - inicio_dt

def descontar_intervalo(total_horas: timedelta, intervalo: str) -> timedelta:
    """Desconta o intervalo do total de horas trabalhadas."""
    if not validar_horario(intervalo):
        raise ValueError("Intervalo inválido")
    
    intervalo_dt = converter_para_datetime(intervalo)
    intervalo_delta = timedelta(hours=intervalo_dt.hour, minutes=intervalo_dt.minute)
    
    return total_horas - intervalo_delta