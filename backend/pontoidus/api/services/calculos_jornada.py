
from datetime import timedelta


class CalculadoraJornada:

    @staticmethod
    def duracao_trabalhada(registro):
        if not registro.hora_entrada or not registro.hora_saida:
            return timedelta(0)

        total_trabalhado = registro.hora_saida - registro.hora_entrada
        if registro.hora_pausa:
            total_trabalhado -= registro.hora_pausa

        return total_trabalhado

    @staticmethod
    def calcular_debitos(registro):
        jornada = registro.jornada
        if jornada.tipo_jornada.pausa_obrigatoria:
            total_horas_previstas = jornada.total_horas + 1
        else:
            total_horas_previstas = jornada.total_horas

        horas_trabalhadas = CalculadoraJornada.duracao_trabalhada(registro).total_seconds() / 3600.0
        saldo_horas = total_horas_previstas - horas_trabalhadas

        if saldo_horas < 0:
            registro.horas_devidas = timedelta(hours=abs(saldo_horas))
        else:
            registro.horas_devidas = timedelta(0)

        registro.save()

    @staticmethod
    def atualizar_jornada(registro):
        CalculadoraJornada.calcular_debitos(registro)
