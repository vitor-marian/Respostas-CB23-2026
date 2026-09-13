A complexidade do método desenfileirar pode ser O(1) amortizada devido ao seguinte funcionamento do método:

* Quando um elemento é enfileirado, ele vai para pilha_entrada que segue ordem LIFO. 
* Então, se quisermos o primeiro a entrar, ele será o último a ser retirado dessa pilha.
* Portanto, a primeira vez que precisamos desenfileirar, colocamos todos os elementos da pilha_entrada em ordem invertida na pilha_saida, e então o topo dessa nova pilha terá o valor que queremos.
* A partir desse momento, pilha_entrada está vazia, mas vai receber os novos elementos inseridos, enquanto pilha_saida continuará ordenada na forma FIFO, pois o primeiro a ser referenciado por ela é o primeiro que chegou na fila.
* Como pilha_saida já fica com todos os elementos que estavam na fila naquele momento, as próximas chamadas do método desenfileirar não precisaram percorrer a fila novamente, pois basta pegar o primeiro elemento da pilha.
* Apenas quando pilha_saida for esvaziada após diversas chamadas do método, será necessário novamente percorrer a fila novamente, dessa vez com todos os novos elementos que foram adicionados depois que isso ocorreu da última vez.

Portanto, a complexidade O(N) é válida, pois é a complexidade do algoritmo quando precisa percorrer uma pilha inteira para gerar a outra. No entanto, se a pilha_entrada possuía N elementos nesse momento, haverá N iterações no método. Porém, pelas próximas N chamadas do método, a complexidade será sempre constante, O(1), já que agora o método opera em uma pilha de N elementos devidamente ordenados para seu propósito, então basta pegar o elemento final de uma pilha, o que tem essa complexidade.