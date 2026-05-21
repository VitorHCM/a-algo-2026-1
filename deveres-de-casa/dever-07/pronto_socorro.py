# ==========================================
# Sistema de Triagem Hospitalar com Max-Heap
# ==========================================

class Paciente:
    """
    Representa um paciente na fila.
    nome -> identificação do paciente
    dor  -> nível de dor (1 a 10)
    """

    def __init__(self, nome, dor):
        self.nome = nome
        self.dor = dor

    def __str__(self):
        return f"{self.nome} (Dor: {self.dor})"


class MaxHeap:
    def __init__(self):
        # Lista que armazenará os pacientes
        self.heap = []

    # -------------------------
    # Funções auxiliares
    # -------------------------

    def pai(self, i):
        return (i - 1) // 2

    def filho_esquerdo(self, i):
        return 2 * i + 1

    def filho_direito(self, i):
        return 2 * i + 2

    def trocar(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    # -------------------------
    # Inserção
    # -------------------------

    def inserir(self, paciente):
        """
        Insere um paciente no heap e
        reposiciona para manter a propriedade do Max-Heap.
        """

        self.heap.append(paciente)

        indice = len(self.heap) - 1

        # Sobe enquanto possuir prioridade maior que o pai
        while (
            indice > 0
            and self.heap[indice].dor >
            self.heap[self.pai(indice)].dor
        ):
            self.trocar(indice, self.pai(indice))
            indice = self.pai(indice)

    # -------------------------
    # Heapify para baixo
    # -------------------------

    def heapify(self, i):
        """
        Reorganiza a árvore para baixo.
        """

        maior = i

        esquerdo = self.filho_esquerdo(i)
        direito = self.filho_direito(i)

        if (
            esquerdo < len(self.heap)
            and self.heap[esquerdo].dor >
            self.heap[maior].dor
        ):
            maior = esquerdo

        if (
            direito < len(self.heap)
            and self.heap[direito].dor >
            self.heap[maior].dor
        ):
            maior = direito

        if maior != i:
            self.trocar(i, maior)
            self.heapify(maior)

    # -------------------------
    # Atendimento
    # -------------------------

    def atender_paciente(self):
        """
        Remove e retorna o paciente com maior dor.
        Complexidade: O(log n)
        """

        if not self.heap:
            return None

        if len(self.heap) == 1:
            return self.heap.pop()

        raiz = self.heap[0]

        # Move o último elemento para a raiz
        self.heap[0] = self.heap.pop()

        # Reorganiza o heap
        self.heapify(0)

        return raiz

    # -------------------------
    # Alteração de prioridade
    # -------------------------

    def atualizar_prioridade(self, nome, nova_dor):
        """
        Atualiza a prioridade de um paciente.

        Increase Key:
            nova_dor > dor atual

        Decrease Key:
            nova_dor < dor atual
        """

        indice = -1

        # Procura o paciente pelo nome
        for i, paciente in enumerate(self.heap):
            if paciente.nome == nome:
                indice = i
                break

        if indice == -1:
            print("Paciente não encontrado.")
            return

        dor_antiga = self.heap[indice].dor
        self.heap[indice].dor = nova_dor

        # Increase Key
        if nova_dor > dor_antiga:

            # Faz o elemento subir
            while (
                indice > 0
                and self.heap[indice].dor >
                self.heap[self.pai(indice)].dor
            ):
                self.trocar(indice, self.pai(indice))
                indice = self.pai(indice)

        # Decrease Key
        elif nova_dor < dor_antiga:

            # Faz o elemento descer
            self.heapify(indice)

    # -------------------------
    # Exibição
    # -------------------------

    def mostrar_fila(self):
        print("\nFila atual:")
        for paciente in self.heap:
            print(paciente)


# ==========================================
# Exemplo de utilização
# ==========================================

fila = MaxHeap()

# Inserção dos pacientes
fila.inserir(Paciente("João", 4))
fila.inserir(Paciente("Maria", 9))
fila.inserir(Paciente("Carlos", 6))
fila.inserir(Paciente("Ana", 2))
fila.inserir(Paciente("Pedro", 8))

fila.mostrar_fila()

# Increase Key
print("\nAna piorou e sua dor aumentou para 10")
fila.atualizar_prioridade("Ana", 10)

fila.mostrar_fila()

# Decrease Key
print("\nMaria recebeu medicação e sua dor caiu para 3")
fila.atualizar_prioridade("Maria", 3)

fila.mostrar_fila()

# Atendimento dos pacientes
print("\nAtendimentos:")

while fila.heap:
    paciente = fila.atender_paciente()
    print("Atendido:", paciente)