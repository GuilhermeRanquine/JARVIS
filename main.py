from brain import JarvisBrain

def main():
    jarvis = JarvisBrain()
    print("--- JARVIS: Sistema Inicializado ---")
    
    while True:
        entrada = input("Sr. Ranquine: ")
        
        if entrada.lower() in [
            'sair', 'exit', 'shutdown', 
            'deligar sistemas', 'encerrar', 'quit', 
            'terminar conversa', 'parar', 
            'finalizar', 'adeus', 'tchau', 
            'até logo', 'até mais', 'nos vemos',
            'até breve', 'fechar', 'desligar', 
            'bye', 'goodbye', 'see you later'
            ]:
            print("JARVIS: Encerrando sistemas. Até breve!")
            break
        
        reposta = jarvis.ask(entrada)
        print(f"JARVIS: {reposta}")
if __name__ == "__main__":
            main()