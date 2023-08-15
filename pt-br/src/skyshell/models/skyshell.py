import nltk
from nltk.chat.util import Chat, reflections

def init():
    pairs = [
        [
            r"oi|olá",
            ["Olá!", "Oi!", "Como posso ajudar você?"]
            ],
        [
            r"como você está?",
            ["Estou apenas sendo um programa de computador, mas estou aqui para ajudar!", "Não tenho sentimentos, mas obrigado por perguntar!"]
            ],
        [
            r"qual é o seu nome?",
            ["Eu sou um chatbot construído usando o NLTK.", "Pode me chamar de SkyBOT."]
            ],
        [
            r"adeus|tchau|até logo",
            ["Até logo!", "Tchau! Tenha um ótimo dia!"]
            ],
        [
            r"",
            ["Desculpe, eu não entendi.  Por favor especifique a pergunta."," Especifique a pergunta por favor."]
            ],
        [
            r"bom dia|buenos dias",
            ["Bom Dia, Como posso ajuda-lo?","Bom Dia, Como posso ajudar o senhor?"]
            ],
        ]
    def chatbot():
        print("Olá! Sou um chatbot simples. Digite 'sair' para encerrar.")
        chat = Chat(pairs, reflections)
        chat.converse()
        if __name__ == "__main__":
            chatbot()
