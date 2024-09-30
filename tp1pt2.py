'''
2.  Um sistema de tráfego  é representado por um grafo orientado ligado. Os nodos denotam 
pontos de acesso e  os arcos denotam vias de comunicação só com um sentido .  O grafo tem de 
ser ligado: entre cada par de nodos $$\langle n_1,n_2 \rangle$$ tem de existir um caminho 
$$n_1 \leadsto n_2$$ e um caminho $$n_2\leadsto n_1$$.
    a) Gerar aleatoriamente o grafo com  $$N \in\{6..10\}$$  nodos e com ramos verificando:
        i. Cada nodo tem um número aleatório de descendentes $$d\in\{1 .. 3\}\,$$ cujos destinos
         são também gerados aleatoriamente. 
        ii. Se  existirem “loops”  ou destinos repetidos, deve-se gerar outro grafo.
    b) Pretende-se fazer  manutenção interrompendo  determinadas vias. Determinar o maior
     número de vias que é possível remover mantendo o grafo ligado.

'''