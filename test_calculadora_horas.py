import unittest
from calculadora_horas import validar_horario, calcular_horas_trabalhadas, descontar_intervalo

class TestCalculadoraHoras(unittest.TestCase):
    
    def test_validar_horario_formato_correto(self):
        self.assertTrue(validar_horario("08:30"))
        self.assertTrue(validar_horario("1730"))  # Sem dois pontos
        self.assertTrue(validar_horario("8:30"))  # Formato H:mm
    
    def test_validar_horario_formato_incorreto(self):
        self.assertFalse(validar_horario("830"))  # Falta um zero
        self.assertFalse(validar_horario("8:70"))  # Minutos inválidos
        self.assertFalse(validar_horario("25:00"))  # Hora inválida
    
    def test_calculo_horarios_normais(self):
        total_horas = calcular_horas_trabalhadas("08:00", "17:00")
        self.assertEqual(total_horas.total_seconds(), 9 * 3600)  # Deve retornar 9 horas

    
    def test_calculo_horarios_invertidos(self):
        total_horas = calcular_horas_trabalhadas("17:00", "08:00")
        self.assertEqual(total_horas.total_seconds(), 15 * 3600)  # Deve retornar 15 horas

    
    def test_desconto_intervalo(self):
        total_horas = calcular_horas_trabalhadas("08:00", "17:00")
        intervalo = "01:00"
        total_com_intervalo = descontar_intervalo(total_horas, intervalo)
        self.assertEqual(total_com_intervalo.total_seconds(), 8 * 3600)  # 9 horas menos 1 hora de intervalo
    
    def test_desconto_intervalo_formato_sem_pontos(self):
        total_horas = calcular_horas_trabalhadas("0800", "1700")
        intervalo = "0100"
        total_com_intervalo = descontar_intervalo(total_horas, intervalo)
        self.assertEqual(total_com_intervalo.total_seconds(), 8 * 3600)  # 9 horas menos 1 hora de intervalo

if __name__ == '__main__':
   unittest.main()
