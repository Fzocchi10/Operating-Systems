from operating_system.memory_algoritmos.memory import Memory

class WorstFitAlgorithm(Memory):
    
    def __init__(self, kernel):
        super().__init__(kernel)


    
    def load(self, data):
        mejor_hueco = None
        maximo_desperdicio = 0

        for h in super().todosLosHuecos():
            if len(data) <= h.memorySize():
                desperdicio = h.memorySize() - len(data)
            
                if desperdicio > maximo_desperdicio:
                    maximo_desperdicio = desperdicio
                    mejor_hueco = h

        if mejor_hueco is not None:
            for i in range(len(data)):
                super().hardware.mmu.place(mejor_hueco.baseDir() + 1, data[i])
                return mejor_hueco

 
            else:
                raise ValueError("No hay espacio")

    

    def unload(self, pcb):
        for i in range(pcb.memory_start, pcb.memory_end):
            super().hardware.mmu.place(i,'')