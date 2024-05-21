from professor import Professor
from aluno import Aluno
from turma import Turma

segundoBLogica = Turma('2ºB - Lógica', '2024')
segundoBIA = Turma('2ºB - IA', '2024')

gabriel = Professor('Sérgio Gabriel', 'PAEET')
gabriel.show_info()

turmasOsinal = [segundoBLogica, segundoBIA]
# osinaldo = Professor('Osinaldo Gomes', 'Professor', turmasOsinal)
# osinaldo.show_info()

felipe = Aluno('Felipe Klein', [segundoBLogica, segundoBIA])
juliano = Aluno('Juliano Fagundes', [segundoBLogica, segundoBIA])
geraldo = Aluno('Geraldo M. Velho', [segundoBLogica, segundoBIA])

# aluno.show_info()