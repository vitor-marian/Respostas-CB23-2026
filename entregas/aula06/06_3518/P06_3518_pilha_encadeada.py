class _No:
    def __init__(self, valor, proximo):
        self.valor = valor
        self.proximo = proximo


class PilhaEncadeada:
    def __init__(self):
        self._topo = None
        self._tamanho = 0

    def push(self, item):
        """
        Adiciona um elemento ao topo da pilha.

        Complexidade: O(1)
        """
        self._tamanho += 1
        self._topo = _No(
            item, self._topo
        )  # apos isso, o _topo recebe o novo No, e ele deve apontar para o valor antigo de _topo, que aqui e lido como o no para o qual ele aponta

    def pop(self):
        """
        Remove o elemento do topo da pilha e o retorna.

        Complexidade: O(1)
        """
        if self._tamanho == 0:
            raise IndexError("A pilha esta vazia.")
        aux = self._topo
        self._topo = self._topo.proximo
        self._tamanho -= 1
        return aux.valor

    def topo(self):
        """
        Retorna o elemento do topo da pilha.

        Complexidade: O(1)
        """
        if self._tamanho == 0:
            raise IndexError("A pilha esta vazia.")
        return self._topo.valor

    def esta_vazia(self):
        """
        Retorna True caso a pilha não possua elementos e False caso contrário.

        Complexidade: O(1)
        """
        return self._tamanho == 0

    def __len__(self):
        """
        Retorna a quantidade de elmentos da pilha.

        Complexidade: O(1)
        """
        return self._tamanho

    def __repr__(self):
        """
        Retorna uma string contendo todos os elementos da pilha, começando do topo e terminando na base.

        Complexidade: O(N)
        """
        saida = ""
        no = self._topo
        for _ in range(self._tamanho):
            saida += f"{no.valor} -> "
            no = no.proximo
        saida += "None"
        return saida
