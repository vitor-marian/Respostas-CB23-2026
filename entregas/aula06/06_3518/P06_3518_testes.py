import unittest

from P06_3518_fila_encadeada import FilaEncadeada
from P06_3518_pilha_encadeada import PilhaEncadeada


class TestPilhaEncadeada(unittest.TestCase):
    def setUp(self):
        self.pilha = PilhaEncadeada()

    def test_ordem_LIFO(self):
        self.pilha.push(1)
        self.pilha.push(2)
        self.pilha.push(3)
        self.assertEqual(self.pilha.pop(), 3)
        self.assertEqual(self.pilha.pop(), 2)
        self.assertEqual(self.pilha.pop(), 1)

    def test_pop_topo_pilha_vazia(self):
        with self.assertRaises(IndexError):
            self.pilha.pop()
        with self.assertRaises(IndexError):
            self.pilha.topo()

    def test_coerencia_len(self):
        self.assertEqual(len(self.pilha), 0)
        self.pilha.push(1)
        self.pilha.push(2)
        self.pilha.pop()
        self.pilha.push(3)
        self.pilha.pop()
        self.assertEqual(len(self.pilha), 1)

    def test_alternancia_operacoes(self):
        self.pilha.push(10)
        self.assertEqual(self.pilha.pop(), 10)
        self.pilha.push(20)
        self.pilha.push(30)
        self.assertEqual(self.pilha.topo(), 30)
        self.assertEqual(self.pilha.pop(), 30)
        self.assertEqual(len(self.pilha), 1)

    def test_armazenamento_itens_tipos_diferentes(self):
        itens = [1, str, "Hello World", str, str, None, [1, 2, 3.4]]
        for item in itens:
            self.pilha.push(item)
        for item in reversed(itens):
            self.assertEqual(self.pilha.pop(), item)


class TestFilaEncadeada(unittest.TestCase):
    def setUp(self):
        self.fila = FilaEncadeada()

    def test_ordem_FIFO(self):
        self.fila.enfileirar(1)
        self.fila.enfileirar(2)
        self.fila.enfileirar(3)
        self.assertEqual(self.fila.desenfileirar(), 1)
        self.assertEqual(self.fila.desenfileirar(), 2)
        self.assertEqual(self.fila.desenfileirar(), 3)

    def test_intercalacao_enfileirar_desenfileirar(self):
        self.fila.enfileirar(1)
        self.assertEqual(self.fila.desenfileirar(), 1)
        self.assertTrue(self.fila.esta_vazia())
        self.fila.enfileirar(2)
        self.fila.enfileirar(3)
        self.assertEqual(self.fila.desenfileirar(), 2)
        self.assertFalse(self.fila.esta_vazia())

    def test_esvaziar_usar_mesma_instancia(self):
        self.fila.enfileirar(1)
        self.fila.enfileirar(2)
        self.fila.desenfileirar()
        self.fila.desenfileirar()
        self.assertTrue(self.fila.esta_vazia())

        self.fila.enfileirar(10)
        self.assertEqual(len(self.fila), 1)
        self.assertEqual(self.fila.frente(), 10)

    def test_desenfileirar_frente_fila_vazia(self):
        with self.assertRaises(IndexError):
            self.fila.desenfileirar()
        with self.assertRaises(IndexError):
            self.fila.frente()

    def test_coerencia_len(self):
        self.assertEqual(len(self.fila), 0)
        self.fila.enfileirar(1)
        self.fila.desenfileirar()
        self.fila.enfileirar(2)
        self.fila.enfileirar(3)
        self.fila.desenfileirar()
        self.fila.desenfileirar()
        self.fila.enfileirar(1)
        self.fila.desenfileirar()
        self.assertEqual(len(self.fila), 0)


if __name__ == "__main__":
    unittest.main()
