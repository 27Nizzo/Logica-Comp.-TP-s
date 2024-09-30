'''
1.  Pretende-se construir um horário semanal para o plano de reuniões de projeto de uma “StartUp” de acordo com as seguintes condições:
    1. Cada reunião ocupa uma sala (enumeradas $$1...S\,$$) durante um 
    “slot” $$(\text{tempo},\text{dia})$$.  Assume-se os dias enumerados $$1..D$$ e, em 
    cada dia, os tempos enumerados $$1..T$$.
    2.  Cada reunião tem associado um projeto (enumerados $$1..P$$) e um conjunto de
     participantes. Os diferentes colaboradores são enumerados $$1..C$$.
    3. Cada projeto tem associado um conjunto de colaboradores, dos quais um  é o 
    líder. Cada projeto realiza um dado número de reuniões semanais. São “inputs” do
     problema o conjunto de colaboradores de cada projeto, o seu líder e o número de reuniões semanais.
    4. O líder do projeto participa em todas as reuniões do seu projeto; os restantes 
    colaboradores podem ou não participar consoante a sua disponibilidade, num mínimo (“quorum”) de 
     $$50\%$$ do total de colaboradores do projeto.  A disponibilidade de cada participante, 
     incluindo o lider,  é um conjunto de “slots” (“inputs” do problema). 
'''

