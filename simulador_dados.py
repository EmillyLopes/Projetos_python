import random
import PySimpleGui

class SimuladoDeDado:
    def __init__(self):
        self.valor_minimo = 1
        self.valor_maximo = 6
        self.mensagem = "Vooê gostaria de gerar um novo valor para o dado?"
        #layout
        layout = [
            [sg.Text ("Jpgar o dado?")],
            [sg.Button("Sim")], sg.Button("Não")]
        ]
        #janela
        janela = [

        ]


    def Iniciar(self):
        resposta = input(self.mensagem)
        try:
            if resposta == "sim" or resposta =="s":
                self.GerarValorDoDado()
            elif resposta == "não" or resposta == "n":
                print("Agradecemos sua participação")
            else:
                print("Favor digitar um valor")
        except:
            print("O programa está sendo encerrado")
            exit()

    def GerarValorDoDado(self):
        print(random.randint(self.valor_minimo,self.valor_maximo))

simulador = SimuladoDeDado()
simulador.Iniciar()