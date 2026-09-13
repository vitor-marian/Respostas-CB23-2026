from P06_3518_pilha_encadeada import PilhaEncadeada


class FilaEncadeada:
    def __init__(self):
        self.pilha_entrada = PilhaEncadeada()
        self.pilha_saida = PilhaEncadeada()
        self._tamanho = 0

    def enfileirar(self, item):
        """
        Adiciona um elemento ao fim da fila.

        Complexidade: O(1)
        """
        self.pilha_entrada.push(item)
        self._tamanho += 1

    def desenfileirar(self):
        """
        Remove o elemento da frente da fila e o retorna.

        Complexidade: O(1) amortizado (caso médio)
        """
        if self._tamanho == 0:
            raise IndexError("A fila esta vazia.")
        self._tamanho -= 1
        if self.pilha_saida.esta_vazia():
            while not self.pilha_entrada.esta_vazia():
                self.pilha_saida.push(self.pilha_entrada.pop())
        return self.pilha_saida.pop()

    def frente(self):
        """
        Retorna o elemento da frente da fila.

        Complexidade: O(1) amortizado (caso médio)
        """
        if self._tamanho == 0:
            raise IndexError("A fila esta vazia.")
        if self.pilha_saida.esta_vazia():
            while not self.pilha_entrada.esta_vazia():
                self.pilha_saida.push(self.pilha_entrada.pop())
        return self.pilha_saida.topo()

    def esta_vazia(self):
        """
        Retorna True caso a fila não possua elementos e False caso contrário.

        Complexidade: O(1)
        """
        return self._tamanho == 0

    def __len__(self):
        """
        Retorna a quantidade de elmentos da fila.

        Complexidade: O(1)
        """
        return self._tamanho

    def __repr__(self):
        """
        Retorna uma string contendo todos os elementos da fila, começando da frente e terminando no fim.

        Complexidade: O(N)
        """
        saida = ""
        aux_saida = PilhaEncadeada()
        while not self.pilha_saida.esta_vazia(): #Adiciona a pilha_saida na string
            item = self.pilha_saida.pop()
            saida += f"{item} -> "
            aux_saida.push(item)
        while not aux_saida.esta_vazia(): #Reorganiza pilha_saida
            self.pilha_saida.push(aux_saida.pop())
        aux_entrada = PilhaEncadeada()
        while not self.pilha_entrada.esta_vazia(): #Inverte a pilha_entrada, pois o fim da fila e o seu topo
            aux_entrada.push(self.pilha_entrada.pop())
        while not aux_entrada.esta_vazia(): #Monta a saida e reorganiza pilha_entrada
            item = aux_entrada.pop()
            saida += f"{item} -> "
            self.pilha_entrada.push(item)
        saida += "None"
        return saida
