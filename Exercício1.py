# Objetivo: criar um jogo de chute com um limite de tentativas.
'''
GERAR UM NÚMERO ALEATÓRIO    
    Como podemos gerar um número aleatório? Além das funções
pre-definidasdo python, podemos utilizar novos módulos providos pela 
própria organização Python, por terceiros e por uma comunidade de 
softwares.
    O módulo random do python é fornecido pelo Python, mas as suas 
funções não são automaticamente definidas pois existem muitas instala-
ções disponíveis no python que tornariam o programa incrivelmente 
pesado.
    O módulo random fornece implementações de gerações pseudo-randô-
micas de números, pois fazer uma geração verdadeiramente randômica
é algo bastante difícil. O programa usa um algorítimo para tentar
fazer o processo randômico, o que torna possível prever qual será
o próximo número. Não é recomendado para situações de segurança e 
criptogração.
    Para acessar o módulo random é necessário importá-lo. Isso torna
o módulo visível para o resto do arquivo Python, o que pode ser feito
usando import random e number_to_guess = random.randint(1,10). A 
variável number_to_guess irá agora ter um inteiro o qual o user 
deverá tentar adivinhar durante o jogo.

OBTER UM INPUT DO USER
    É preciso checar se o user acertou o chute. Poderíamos usar a 
função if para isso, todavia, a gente quer o user repita o teste até
ele acertar ou até ele ter perdido as chances.
    Vamos, portanto, usar a função while e checar a respostas do user:
guess = int(input('Please guess a number between 1 and 10:))
while number_to_guess != guess:
    O Loop acima será repetido se o número digitado não for igual ao 
número gerado. Podemos portanto imprimir uma mensagem na tela para o
user alertando que o chute dele foi errado:
guess = int(input('Please guess a number between 1 and 10:))
while number_to_guess != guess:
    print('Sorry wrong number')
    Agora é necessário que o user faça um outro palpite caso contrário
o looping rodará indefinidamente:
guess = int(input('Please guess a number between 1 and 10:))
while number_to_guess != guess:
    print('Sorry wrong number')
    # To be detailed
    guess = int(input('Please guess again:))

CHECAR QUE O USER NÃO TENHA EXCEDIDO SEU NÚMERO DE TENTATIVAS
    O user tem que acerta o número em 4 tentativas. Necessário incre-
mentar algum tipo de lógica que irá interromper o jogo uma vez que o 
número de tentativas for excedido.
    Necessário ter uma variável para traçar o número de tentativas
realizadas pelo user. Podemos chamá-la de number_of_tries e iniciar
com o valor 1:
count_number_of_tries = 1
    Isso precisa acontecer antes de entrarmos no loop e dentro do 
while loop é necessário checar se o número de tentativas foi expirado
e acrescentar o número de tentativas caso o user ainda esteja jogando.
    Nós vamos usar a função if para ver se o número de tentativas foi
atingido. Se o tiver, nós vamos encerrar o loop. O jeito mais fácil de
fazer isso é usando a função break:
if count_number_of_tries == 4:
    break  
    Se a gente não quebrar o loop nós podemos acrescentar a contagem
usando o operado +=. Ou seja:
count_number_of_tries = 1
guess = int(input('Please guess a number between 1 and 10: '))
while number_of_guess != guess:
    print('Sorry wrong number')
    if count_number_of_tries == 4:
        break
    # To be detailed
    guess = int(input('Please guess again: '))
    count_number_of_tries += 1

AVISAR O USER QUANDO MAIOR OU MENOR
    Necessário indicar quando o chute é maior ou menor que o valor
aleatório gerado. Podemos usar a função if. Se o chute for menor impri-
mimos uma mensagem, se for maior, imprimimos outra.
    Podemos ou usar uma nova condição if àquela usada sobre o número
máximo de tentativas ter sido atingido ou extendê-la usando a função
elif. No caso da elif, isso significa que ambas as condições são rela-
cionadas entre si, por isso usaremos ela. O While loop será:
count_number_of_tries = 1
guess = int(input('Please guess a number between 1 and 10: '))
while number_to_guess != guess:
    print('Sorry wrong number')
    if count_number_of_tries == 4:
        break
    elif guess < number_to_guess:
        print('Your guess was lower than the number')
    else:
        print('Your guess was higher than the number')
    guess = int(input('Please guess again: '))
    count_number_of_tries += 1

FINAL DO JOGO
    Cobrimos todas as situações que podem ocorrer no jogo. Resta agora
definir as mensagens de final do jogo. Se o user vencer, vamos parabe-
nizá-lo, se ele perder, vamos falar para ele qual foi o número. Vamos
lidar com isso usando a função if:
if number_to_guess == guess:
    print('Well done you won!')
    print('You took', count_number_of_tries, 'goes to complete the game')
else: 
    print('Sorry - you loose')
    print('The number you needed to guess was ', number_to_guess)
print('Game over')

LISTAGEM


import random

print('Welcome to the number guess game')

# Inicie o número a ser adivinhado
number_to_guess = random.randint(1,10)

# Inicie o número de tentativas que o jogador fará
count_number_of_tries = 1

# Obtenha seu palpite inicial
guess = int(input('Please guess a number between 1 and 10: '))
while number_to_guess != guess:
    print('Sorry wrong number')
    if count_number_of_tries == 4:
        break
    elif guess < number_to_guess:
        print('Your guess was lower than the number')
    else:
        print('Your guess was higher than the number')
if number_to_guess == guess:
    print('Well done you won!')
    print('You took', count_number_of_tries , 'goes to complete the game')
else:
    print('Sorry - you loose')
    print('The number you needed to guess was', number_to_guess)

print('Game over')
'''
import random
import time


class Adivinhe_número:
    def __init__(self):
        self.valor_min = 0
        self.valor_max = 10
        self.valor_chute = 0
        self.valor_gerado = 0
        self.tentativas = 0

    def Iniciar(self):
        self.Apresentação()
        self.valor_gerado = self.Gerar_número()
        self.Chutar_número()
        self.Trapaça()
        self.QuaseLá()
        self.Fim_de_jogo()
        self.Perguntar()
        
    def Gerar_número(self):
        return random.randint(self.valor_min,self.valor_max)
    
    def Chutar_número(self):
        try:
            self.valor_chute = int(input('Por favor digite um número: '))
        except ValueError:
            print('Por favor digite um número inteiro.')
            self.Chutar_número()
           
    def Fim_de_jogo(self):
        if self.valor_chute == self.valor_gerado:
            print('Parabéns! Você acertou.')
            print('Você levou', self.tentativas ,'tentativas ao todo.')
        else:
            print('Lamento - você perdeu.')
            print(f'O número correto era {self.valor_gerado}.')
            print(f'Você só tinha {self.tentativas} tentativas')
        
    def Perguntar(self):
        rejogar = input('Deseja jogar novamente?(s/n)')
        if rejogar == 's':
            self.Iniciar()
        elif rejogar == 'n':
            print('Obrigado e volte sempre.')
        else:
            print('Por favor digite ou \'s\' ou \'n\'.')
            self.Perguntar()

    def QuaseLá(self):
        while self.valor_chute - self.valor_gerado == -1 or self.valor_chute - self.valor_gerado == 1:
            print('O número inserido é 1 unidade maior ou menor que o número gerado.')
            self.Chutar_número()
        else:
            while self.valor_gerado != self.valor_chute:
                print('Ops, você errou.')
                self.tentativas += 1
                if self.tentativas == 4:
                    break
                elif self.valor_gerado > self.valor_chute:
                    print('O número inserido é menor que o número gerado.')
                    self.Chutar_número()
                else:
                    print('O número inserido é maior que o número gerado.')
                    self.Chutar_número()

    def Trapaça(self):
        while self.valor_chute == -1:
            print(f'O número gerado é: {self.valor_gerado}')
            self.Chutar_número()
        else:
            while self.valor_gerado != self.valor_chute:
                print('Ops, você errou.')
                self.tentativas += 1
                if self.tentativas == 4:
                    break
                elif self.valor_gerado > self.valor_chute:
                    print('O número inserido é menor que o número gerado.')
                    self.Chutar_número()
                else:
                    print('O número inserido é maior que o número gerado.')
                    self.Chutar_número()

    def Apresentação(self):
         print('Carregando...')
         time.sleep(5)
         print('Carregamento concluído. Iniciando o jogo agora.')
         time.sleep(2)
         print(
             'Instruções: Esse é um jogo onde o computador irá gerar aleatoriamente um número de 0 a 10.',
             'Cabe ao user(esse é você!) descobrir qual número foi gerado pela máquina.',
             'Você terá um total de 4 tentativas, boa sorte!',
         )
           
user1 = Adivinhe_número()
user1.Iniciar()            





    

