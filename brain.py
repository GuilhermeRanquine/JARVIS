import ollama

class JarvisBrain:
    def __init__(self, model_name="nemotron-3-nano"):
        self.model_name = model_name
        self.histoty = [
            {"role": 'system', 'content': 'Você é o JARVIS. Respostas curtas técnicas e eficientes.'}
        ]
        
    def ask(self, message):
        self.histoty.append({'role': 'user', 'content': message})
        
        try:
            response = ollama.chat(
                model=self.model_name,
                messages=self.histoty
            )
            reply = response['message']['content']
            self.histoty.append({'role': 'assistant', 'content': reply})
            return reply
        except Exception as e:
            return f"Erro no processamento: {str(e)}"