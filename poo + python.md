### **POO**

- dados e código lado a lado, divididos por classes

#### **Classe**

- receita usada para criar um objeto útil (conjunto de objetos), modelo de uma parte da realidade  
- pode criar quantos objetos quiser, pode ser vazia  
- pode ser modificada para um propósito – nova classe criada (herda propriedades e métodos do original e novos)  
- uma classe bem feita protege os dados sensíveis e esconde de modificações não autorizadas – **encapsulamento**  
  - *`__nome-componente`* (privado, AttributeError se tenta acessar)  
- **método** – função declarada dentro da classe que pode ser acessada pelos componentes da classe  
  - todos os métodos/funções devem receber o parâmetro ***self*** (objeto, 1o par) – permite ao método acessar entidades executadas pelo objeto em si  
- **construtor** `__init__` – criar novo objeto  
- `__nome` – componente privado  
  - acessível por *\_ClassName\_\_PrivatePropertyName*

```
\#keyword \+ nome  
class TheSimplestClass:  
    pass \#vazia

my\_first\_object \= TheSimplestClass()  
\#nome da classe finge ser uma função que retorna um objeto com todas as caracteristicas da classe (no caso, vazia)
```

**hierarquia** 

- definição embasada de única de uma classe, ex: veículo \= entidade criada artificialmente para transporte e dirigidos por humanos  
  - veículo (superclasse) → de terra (subclasse) → tracionado  
  - subclasse aponta para superclasse

**Objeto**

- encarnação de ideia (requisitos, características) da classe  
- tem um conjunto de características (propriedades/atributos) e podem realizar atividades (métodos)  
- interagem uns com os outros, trocando de dados ou chamando os métodos  
- quando criado recebe um conjunto de propriedades e métodos pré definidos, um deles é **`__dict__`** (conjunto com nomes e valores de todas as propriedades)  
- não necessariamente são iguais  
- **atributos**  
  - nome (substantivo)  
  - conjunto de propriedades individuais (adjetivo)  
  - conjunto de habilidades para realizar atividades específicas (verbo)  
  - ex: O Cadillac (nome, classe: carro com roda) rosa (propriedade: cor) saiu (ação) cedo

**Variável de instância**

- criada explicitamente e adicionada a um objeto (no construtor, depois e/ou removida) – ligada ao objeto, não a classe (modificada não afeta outros objetos)  
- checar de maneira segura se um objeto tem uma propriedade (objetos da mesma classe podem ter propriedades diferentes)  
- se adiciona uma variável de instância privada fora do código da classe, ela funciona como uma propriedade comum  
- não existe se não tem objetos da classe  
- negar propriedade: `prop = not prop`

```class ExampleClass:  
    def \_\_init\_\_(self, val \= 1):  
        self.\_\_first \= val  
        *\#instancia (objeto) vai ter variavel 'first' com valor definido (se passado ao criar) ou 1 (default)*

    def *set\_second*(self, val):  
        self.\_\_second \= val  
        *\# cria outra variavel de instancia (se o metodo for chamado)*

example\_object\_1 \= ExampleClass() *\#first \= 1 (default)*  
example\_object\_2 \= ExampleClass(2) *\#first \= 2 (passado)*

example\_object\_2.set\_second(3) *\#first \= 2, second \= 3*

example\_object\_3 \= ExampleClass(4) *\#first \= 4*  
example\_object\_3.\_\_third \= 5 *\# cria variavel de instancia 'third' diretamente no objeto*

*\# python bota nome da classe \+ \_\_ \+ nome da variavel para evitar acesso direto*  
print(example\_object\_1.\_\_dict\_\_)  
print(example\_object\_1.\_ExampleClass\_\_first)  
print(example\_object\_2.\_\_dict\_\_)  
print(example\_object\_3.\_\_dict\_\_)

*\#SAÍDA \- nome acessavel fora da classe*  
*\# {'\_ExampleClass\_\_first': 1}*  
*\# 1*  
*\# {'\_ExampleClass\_\_first': 2, '\_ExampleClass\_\_second': 3}*  
*\# {'\_ExampleClass\_\_first': 4, '\_\_third': 5}*
```

**Variável de classe**

- propriedade que existe em uma cópia e é armazenada fora dos objetos (existe mesmo se não tiver objetos criados)  
- sempre o mesmo valor em todos os objetos  
- não são mostradas no **`__dict__`** dos objetos (não são partes dos objetos né) 

```class ExampleClass:  
    \_\_counter \= 0 *\#inicializa a varivale dentro da classe mas fora dos metodos \-- variavel de classe*  
    def \_\_init\_\_(self, val \= 1):  
        self.\_\_first \= val  
        ExampleClass.\_\_counter \+= 1 *\#acessivel como qualquer atributo*

example\_object\_1 \= ExampleClass()  
example\_object\_2 \= ExampleClass(2)  
example\_object\_3 \= ExampleClass(4)

print(example\_object\_1.\_\_dict\_\_, example\_object\_1.\_\_counter)  
print(example\_object\_2.\_\_dict\_\_, example\_object\_2.\_\_counter)  
print(example\_object\_3.\_\_dict\_\_, example\_object\_3.\_\_counter)

*\# SAÍDA*  
*\# {'\_ExampleClass\_\_first': 1} 3*  
*\# {'\_ExampleClass\_\_first': 2} 3*  
*\# {'\_ExampleClass\_\_first': 4} 3*

*\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#*

*class ExampleClass:*  
    *varia \= 1 \#variavel de classe*  
    *def \_\_init\_\_(self, val):*  
        *ExampleClass.varia \= val*  
        *\# self.varia \= val \-- criaria uma variavel de instancia com o mesmo nome*  
        *\# varia \= val \-- criaria uma variavel local ao metodo*

*print(f"CLASS:\\n{ExampleClass.\_\_dict\_\_}")*  
*example\_object \= ExampleClass(2)*

*print(f"CLASS:\\n{ExampleClass.\_\_dict\_\_}")*  
*print(f"\\nOBJECT:\\n{example\_object.\_\_dict\_\_}")*  
     
*\# SAÍDA*  
*\# CLASS:*  
*\# {'\_\_module\_\_': '\_\_main\_\_', '\_\_firstlineno\_\_': 1, 'varia': 1, '\_\_init\_\_': \<function ExampleClass.\_\_init\_\_ at 0x000001F2D88DCE00\>, ...}*  
*\# CLASS:*  
*\# {'\_\_module\_\_': '\_\_main\_\_', '\_\_firstlineno\_\_': 1, 'varia': 2, '\_\_init\_\_': \<function ExampleClass.\_\_init\_\_ at 0x000001F2D88DCE00\>, ...}*  
*\# OBJECT:*  
*\# {}*
```
##### **Métodos**

- função embutida em uma classe  
- declarado com 1+ parâmetros (1o \= **self** – acesso ao objeto e variáveis da classe, ou para invocar outros métodos da classe)  
- pode ser chamado sem parâmetros (python passa automaticamente o self, se tiver outro parâmetro passa)
```
class Classy:  
    varia \= 2  
    def *method*(self):  
        print(self.varia, self.var)  
        self.other()

    def *other*(self):  
        print("other")  
   
obj \= Classy()  
obj.var \= 3  
obj.method()

*\# 2 3*  
*\# other*

*\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#*  
class Classy:  
    def *visible*(self):  
        print("visible")

    def *\_\_hidden*(self):  
        print("hidden")

obj \= Classy()  
obj.visible() *\# visible*

*try*:  
    obj.\_\_hidden()  
*except*:  
    print("failed") *\# failed*

obj.\_Classy\_\_hidden() *\# hidden*

(obj.\_\_module\_\_)
```
- **`__name__`** (string) – nome da classe  
  - type(obj).\_\_name\_\_


- **`__module__`** (string) – nome do módulo da classe  
  - “módulo” chamado \_\_main\_\_ na verdade é o arquivo atual


- **`__subclasses__`** – lista de subclasses da classe atual (útil para exceções)  
    
- quando python tenta imprimir uma classe como string, chama o método **`__str__`** (pode sobrescrever)  
    
- **`__mro__`** `/ mro()` – caminho que o python busca métodos/variáveis nas superclasses  
    
- **`__bases__`** (tupla) – superclasses (não nomes, classes em si) diretas da classe atual, objetos não tem isso  
  - uma classe sem superclasses explícitas aponta para seu objeto como “superclasse”

```
class SuperOne:  
    *pass*

class SuperTwo:  
    *pass*

class Sub(SuperOne, SuperTwo):  
    *pass*

def *printBases*(cls):  
    print('( ', end\='')  
    *for* x *in* cls.\_\_bases\_\_:  
        print(x.\_\_name\_\_, end\=' ')  
    print(')')

printBases(SuperOne) *\# ( object )*  
printBases(SuperTwo) *\# ( object )*  
printBases(Sub) *\# ( SuperOne SuperTwo )*

*\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#*  
class Sample:  
    def \_\_init\_\_(self):  
        self.name \= Sample.\_\_name\_\_  
    def *myself*(self):  
        print("My name is " \+ self.name \+ " living in a " \+ Sample.\_\_module\_\_)

obj \= Sample()  
obj.myself()  
*\# My name is Sample living in a \_\_main\_\_*
```
- **`args`** (tupla) – propriedade da classe BaseException, todos os argumentos passados ao construtor  
    
- `issubclass(Sub, Super)` – checar se uma classe é subclasse de outra – cada classe é uma subclasse de si mesma  
  ![][image1]  
    
- `isinstance(obj, tipo)` – verifica se um objeto é uma instância de “tipo”  
  ![][image2]  
    
- `obj1 is obj2`  – verifica se 2 variáveis se referem ao mesmo objeto (variável é um ponteiro para o objeto), não compara o conteúdo  
```
  object\_1 \= SampleClass(0)  
  object\_2 \= SampleClass(2)  
  object\_3 \= object\_1  
  object\_3.val \+= 1  
    
  print(object\_1 *is* object\_2) *\# False (1 \!= 2\)*  
  print(object\_2 *is* object\_3) *\# False (2 \!= 1\)*  
  print(object\_3 *is* object\_1) *\# True (1 \== 1\)*  
    
  string\_1 \= "Mary had a little "  
  string\_2 \= "Mary had a little lamb"  
  string\_1 \+= "lamb"  
    
  print(string\_1 \== string\_2, string\_1 *is* string\_2)  
  *\# True False (texto igual mas são guardados em objetos diferentes na memória)*  
```
- `super()` – acessa a superclasse mais próxima sem precisar do nome nem passar self (objetos de subclasses podem acessar a super apenas chamando os métodos/variáveis – tanto de superclasse quanto superobjeto)


##### **reflexão e introspecção**

- não precisa conhecer a definição completa de uma classe/objeto para manipular o objeto – o objeto/classe contém os metadados para reconhecer as características durante a execução do programa  
- **introspecção** – programa examinar o tipo ou propriedades de um objeto no tempo de execução  
- **reflexão** – programa manipular os valores, propriedades e/ou funções do objeto no tempo de execução  
- incIntsI() – pega um objeto, encontra todos os atributos inteiros que começam com “i” e incrementa em 1
```
class MyClass:  
    *pass*

obj \= MyClass()  
obj.a \= 1  
obj.b \= 2  
obj.i \= 3  
obj.ireal \= 3.5  
obj.integer \= 4  
obj.z \= 5

def *incIntsI*(obj):  
    *for* name *in* obj.\_\_dict\_\_.keys(): *\#busca nomes dos atributos*  
        *if* name.startswith('i'):  
            val \= getattr(obj, name) *\#pega valor atual*  
            *if* isinstance(val, int): *\#verifica se é do tipo integer*  
                setattr(obj, name, val \+ 1) *\#(objeto, atributo, novo valor)*

print(obj.\_\_dict\_\_)  
*\# {'a': 1, 'integer': 4, 'b': 2, 'i': 3, 'z': 5, 'ireal': 3.5}*  
incIntsI(obj)  
print(obj.\_\_dict\_\_)  
*\# {'a': 1, 'integer': 5, 'b': 2, 'i': 4, 'z': 5, 'ireal': 3.5}*
```
##### 

##### **composição**

- classe é feita/tem objetos de outra classe (não é herança), acessa métodos, etc – montada tipo lego
```
*import* math

class Point:  
    def \_\_init\_\_(self, x \= 0.0, y \= 0.0):  
        self.\_\_x \= float(x)  
        self.\_\_y \= float(y)  
     
    def *getx*(self):  
        *return* self.\_\_x  
     
    def *gety*(self):  
        *return* self.\_\_y  
     
    def *distance\_from\_xy*(self, x, y):  
        *return* math.hypot(abs(self.\_\_x \- x), abs(self.\_\_y \- y))

    def *distance\_from\_point*(self, point):  
        *return* self.distance\_from\_xy(point.getx(), point.gety())

class Triangle:  
    def \_\_init\_\_(self, vertice1, vertice2, vertice3): *\#recebe 3 instancias de Point, mas nao herda a classe*  
        *\# armazena em um atributo privado \- Triangle pode usar as funcionalidades de Point sem herdar as propriedades*  
        self.\_\_vertices \= \[vertice1, vertice2, vertice3\]  
     
    def *perimeter*(self): *\#soma das 3 distâncias*  
        *\# print(getattr(self.\_\_vertices\[1\], '\_Point\_\_x'))*  
        *\# Triangle acessa os métodos de Point pelos objetos da lista*  
        *\# o 'self' do método Point é o objeto da lista Triangle*  
        *\# Triangle acessa os dados pelos métodos públicos (gets) \- mantém encapsulamento*  
        *return* (self.\_\_vertices\[0\].distance\_from\_point(self.\_\_vertices\[1\]) \+  
                self.\_\_vertices\[1\].distance\_from\_point(self.\_\_vertices\[2\]) \+  
                self.\_\_vertices\[2\].distance\_from\_point(self.\_\_vertices\[0\]))

triangle \= Triangle(Point(0, 0), Point(1, 0), Point(0, 1))  
print(triangle.perimeter())

- pode mudar o comportamento da classe depois de criada

*import* time

class Tracks: *\#sabe apenas mudar de direção*  
    def *change\_direction*(self, left, on):  
        print("tracks: ", left, on)

class Wheels: *\#sabe apenas mudar de direção*  
    def *change\_direction*(self, left, on):  
        print("wheels: ", left, on)

*\# capacidade do veiculo virar é composta usando objetos externos*  
class Vehicle: *\#sabe apenas pedir para mudar de direção*  
    *\# pode mudar o comportamento/tipo de veículo depois de criado (flexícel)*  
    def \_\_init\_\_(self, controller):  
        self.controller \= controller *\#objeto externo*

    def *turn*(self, left):  
        self.controller.change\_direction(left, True)  
        time.sleep(0.25)  
        self.controller.change\_direction(left, False)

wheeled \= Vehicle(Wheels()) *\#Vehicle se comporta como carro (Wheels)*  
tracked \= Vehicle(Tracks()) *\#Vehicle se comporta como tanque (Tracks)*

wheeled.turn(True)  
*\# chama metodo turn de Vehicle*  
*\# Vehicle chama change\_direction do controller (Wheels)*  
*\# objeto delega a execução para o objeto Wheels*  
tracked.turn(False)
```
###### ***hasattr** – verificar se um atributo existe em objeto/classe*

- jeito feio
```
class ExampleClass:  
    def \_\_init\_\_(self, val):  
        *if* val % 2 \!= 0:  
            self.a \= 1  
        *else*:  
            self.b \= 1

example\_object \= ExampleClass(1)  
print(example\_object.a)

*try*:  
    print(example\_object.b)  
*except* AttributeError:  
    *pass*  
```   

- jeito bonito: função **`hasattr(classe/objeto, ‘nome_atributo’)`**
```
class ExampleClass:  
    a \= 1  
    def \_\_init\_\_(self):  
        self.b \= 2  
   
example\_object \= ExampleClass()  
   
print(hasattr(example\_object, 'b')) *\#True*  
print(hasattr(example\_object, 'a')) *\#True*  
print(hasattr(ExampleClass, 'b')) *\#False*  
print(hasattr(ExampleClass, 'a')) *\#False*
```
##### **Herança**

- *sumário*  
  - \_\_str\_\_()  
  - issubclass(sub, sup)  
  - isinstance(o, c)  
  - a is b  
  - super()  
- um objeto de uma classe herda todas as características (atributos, métodos) da/s superclasse/s – funcionalidades criadas são herdadas também  
- **método abstrato** – vazio, implementado nas subclasses  
- `Super.construtor(self)` (precisa botar explícito)  
  class Sub(Super):  
      def \_\_init\_\_(self, name):          
    *\# Super.\_\_init\_\_(self, name)*  
          **super()**.\_\_init\_\_(name)  
- quando python tenta imprimir uma classe como string, chama o método **`__str__`** (pode sobrescrever, tipo return [`self.name`](http://self.name))  
- python procura na **ordem**  
  - no objeto atual  
  - em todas as superclasses (subindo) – se não achar, da AttributeError  
  - se tiver \+1 classe no mesmo nível, vê da esquerda para direita (se achar na da esquerda, já para de procurar)
```
class Level1:  
    variable\_1 \= 100  
    def \_\_init\_\_(self):  
        self.var\_1 \= 101

    def *fun\_1*(self):  
        *return* 102

class Level2(Level1):  
    variable\_2 \= 200  
    def \_\_init\_\_(self):  
        super().\_\_init\_\_()  
        self.var\_2 \= 201  
     
    def *fun\_2*(self):  
        *return* 202

class Level3(Level2):  
    variable\_3 \= 300  
    def \_\_init\_\_(self):  
        super().\_\_init\_\_()  
        self.var\_3 \= 301

    def *fun\_3*(self):  
        *return* 302

obj \= Level3()  
print(obj.variable\_1, obj.var\_1, obj.fun\_1()) *\# 100 101 102*  
print(obj.variable\_2, obj.var\_2, obj.fun\_2()) *\# 200 201 202*  
print(obj.variable\_3, obj.var\_3, obj.fun\_3()) *\# 300 301 302*
```
###### ***polimorfismo – override***

- mais de uma superclasse tem entidades do mesmo nome (pega sempre o que foi definido por último)  
- **polimorfismo** – subclasse modifica o comportamento da superclasse  
  - **virtual** – método redefinido por uma subclasse
```
class Left:  
    var \= "L"  
    var\_left \= "LL"  
    def *fun*(self):  
        *return* "Left"

class Right:  
    var \= "R"  
    var\_right \= "RR"  
    def *fun*(self):  
        *return* "Right"

*\# left aparece 1o (esquerda) na lista de heranças então se achar método/variável em Left, para por ali*  
class Sub(Left, Right):  
    *pass*

obj \= Sub()

print(obj.var, obj.var\_left, obj.var\_right, obj.fun())  
*\# L LL RR Left*  
print(Sub.\_\_mro\_\_) *\#mostra ordem (classes) que o python procura, em forma de tupla*  
print(Sub.mro()) *\#mesma coisa mas em forma de lista*
```
- puxar de uma superclasse superior
```
class Dog:  
    kennel \= 0  
    def \_\_init\_\_(self, breed):  
        self.breed \= breed  
        Dog.kennel \+= 1  
    def \_\_str\_\_(self):  
        *return* self.breed \+ " says: Woof\!"

class SheepDog(Dog):  
    def \_\_str\_\_(self):  
        *return* super().\_\_str\_\_() \+ " Don't run away, Little Lamb\!"

class GuardDog(Dog):  
    def \_\_str\_\_(self):  
        *return* super().\_\_str\_\_() \+ " Stay where you are, Mister Intruder\!"

class LowlandDog(SheepDog):  
    def \_\_str\_\_(self):  
        *return* **Dog.**\_\_str\_\_(self) \+ " I don't like montains\!"
```
- **`__mro__`** `/ mro()` – caminho que o python busca métodos/variáveis nas superclasses

###### ***hierarquia de classes***

- dividir um problema entre classes e fazer a hierarquia

```
class Top:  
    def *m\_top*(self):  
        print("top")

class Middle(Top):  
    def *m\_middle*(self):  
        print("middle")

*\# 1\. regra da subclasse*  
*\# \- superclasse deve sempre vir depois na subclasse (subclasses são mais especializadas) \- como Middle herda de Top, Middle deve vir antes*  
*\# 2\. regra da esquerda para direita*  
*\# \- é ordenado explicitamente para procurar 1o em Top depois em Middle*  
class Bottom(Top, Middle): *\#CORRETO: (sub, super)*  
    def *m\_bottom*(self):  
        print("bottom")

object \= Bottom()  
object.m\_bottom()  
object.m\_middle()  
object.m\_top()  
*\# ERRO: TypeError: Cannot create a consistent method resolution order (MRO) for bases Top, Middle*
```

###### ***problema do diamante***

- python permite heranças múltiplas

![][image3]

- D herda de B e C e ambas herdam de A  
- python vai chamar sempre a classe do meio que foi declada 1o na herança

```
class Top:  
    def *m\_top*(self):  
        print("top")

class Middle\_Left(Top):  
    def *m\_middle*(self):  
        print("middle\_left")

class Middle\_Right(Top):  
    def *m\_middle*(self):  
        print("middle\_right")

class Bottom(Middle\_Left, Middle\_Right):  
    def *m\_bottom*(self):  
        print("bottom")

object \= Bottom()  
object.m\_bottom()  
object.m\_middle() *\# sempre Left (declarada 1o)*  
object.m\_top()
```

#### pilha – LIFO

- objeto com 2 operações: push (novo elemento no topo) e pop (elemento removido do topo)  
- exemplo: lista (último é o topo)

```
class Stack:  
    *\# implementa uma lista em cada objeto, escondida dos usuários da classe*  
    *\# propriedades adcionadas nas classes manualmente*

    *\# função construtor \- construir um novo objeto, chamada automaticamente*  
    def \_\_init\_\_(self): *\#1+ parametros (objeto)*  
        *\# self.stack\_list \= \[\] \#nova propriedade de objeto: lista vazia para pilha*  
        self.\_\_stack\_list \= \[\] *\#nova propriedade 'privada' do objeto*

    def *push*(self, val): *\#1+ parametros (objeto, valor)*  
        self.\_\_stack\_list.append(val)  
     
    def *pop*(self):  
        val \= self.\_\_stack\_list\[\-1\]  
        *del* self.\_\_stack\_list\[\-1\]  
        *return* val

stack\_object1 \= Stack()  *\# cria objeto*  
stack\_object2 \= Stack()  
*\# nome\_objeto.propriedade \- sem () pq não é um método/função*  
*\# print(len(stack\_obj.stack\_list))  \# 0*  
*\# print(len(stack\_obj.\_\_stack\_list))  \# AttributeError: 'Stack' object has no attribute 'stack\_list'*  
stack\_object1.push(3)  
stack\_object2.push(stack\_object1.pop())  
stack\_object1.push(1)

print(stack\_object1.pop()) *\#1*  
print(stack\_object2.pop()) *\#2*

*\# nova SUB CLASSE: soma dos elementos armazenados na pilha*  
class AddingStack(Stack): *\#herda de Stack*  
    def \_\_init\_\_(self):  
        *\#Super.construtor(self) \- para invocar metodo dentro da classe precisa do self*  
        Stack.\_\_init\_\_(self) *\#chama o construtor da super classe*  
        self.\_\_sum \= 0 *\#privada*  
     
    def *push*(self, val):  
        self.\_\_sum \+= val *\#incrementa 'sum' da classe atual (sub)*  
        Stack.push(self, val) *\#chama o metodo push da super classe*

    def *pop*(self):  
        val \= Stack.pop(self) *\#metodo da super classe*  
        self.\_\_sum \-= val *\#tira valor recebido (val)*  
        *return* val  
     
    *\#mostrar valor de soma mesmo protegido*  
    def *get\_sum*(self):  
        *return* self.\_\_sum

stack\_add \= AddingStack()  
*for* i *in* range(5):  
    stack\_add.push(i)  *\#0,1,2,3,4*  
print(stack\_add.get\_sum())  *\#10*

*for* i *in* range(5):  
    print(stack\_add.pop())  *\#4,3,2,1,0*
```

## **PYTHON3 – aula 6**

- programação procedural e orientada a objeto

**Teoria**

- fácil de tudo  
- concorrentes: Perl, Ruby  
- implementação: serviços de internet (pesquisa, nuvem, mídias, ferramentas), componentes do SO Linux  
- não faz: aplicativos, driver e mecanismos gráficos (linguagem de baixo nível)  
- Python2 (antigo) e Python3 (atual), incompatíveis  
- Python Software Foundation: estabelece padrões, referência; escritos em C – CPython (implementação tradicional)  
- implementações alternativas  
  - Cython (eficiência) – código python executado em C, ex: cálculos matemáticos  
  - Jython – se comunica com infraestrutura Java, segue Python2, ex: sistemas complexos  
  - PyPy (RPython) – subconjunto do Python (reescrito), código executado traduzido para C, ex: testar recursos Python  
  - MicroPython – Pyhton3 otimixado para microcontroladores, prompt interativo, números de precisão arbitrária, módulos  
- **função**: causa efeito (envia texto, gera imagem), avalia um valor e retorna como resultado  
  - do Python, ex: print  
  - dos módulos (complementos)  
  - do código

**Instalar e configurar**

- [https://www.python.org/downloads/](https://www.python.org/downloads/)  
- marcar “adicionar python 3 ao PATH”  
- precisa de: editor, console, debugger

- rodar no vs code: shift enter  
- rodar: python [nome.py](http://nome.py)   
- módulos, pacotes \= bibliotecas (c)  
  - importar módulo – import cs50  
  - importar 1 coisa do pacote – from cs50 import get\_string  
- documentação: [docs.python.org/3/library/functions.html](http://docs.python.org/3/library/functions.html)   
- && \= and; || \= or  
  - if s in \["y", "Y"\]:


- struct \= object  
  - se a função está associada a uma estrutura de dado → método  
- mode mudar string: input(“...”).lower().again() …  
- se bibliotecas tem conflito de nomes de função – biblioteca.função

**Literal**

- notações para representar valores fixos do código (número, string)  
- dados cujos valores são determinados pelo próprio literal, python escolhe a forma mais econômica de representar um número  
- pode escrever números grandes com \_  
  - 11\_111\_111 \= 11111111  
  - ex: 123  
  - não ex: c

- **octais**: prefixo 0o (zero o)  
  - 0o123 \= decimal 83

- **hexa**: prefixo 0x (zero x)  
  - 0x123 \= decimal 291


- **float**: pode ocultar 0s do início ou final  
  - .4 \= 0.4  
  - 4\. \= 4.0 \!= 4  
- **potência**  
  - 3E8 \= 3 \* 10^8  
  - 6.62607E \= 6,62607 \* 10^-34

   

- **string**  
  - aspas dentro de string; /” (/ indica caractere especial)  
    print("Eu gosto \\"Monty Python\\"")  
    print(‘string “dentro” de string’)  
    print(‘I/’m nicole’)

- **booleano**  
  - True (1) ou False (0)  
- None  
  - objeto NoneType, ausência de valor


*Voltando*

- \\ no fim de uma linha \= continuar o código na linha abaixo (para linhas longas)  
- **sequência**   
  - tipo de dado que pode guardar mais de um valor, que podem ser sequencialmente navegados (por um for)  
  - mutável: lista  
  - imutável: tupla

- **estruturas de dados**  
  - range  
  - list (lista encadeada) – \[\]  
  - tuple  
  - dict (dictionary)  
  - set


- **problemas**  
  - ponto flutuante

#### **caracteres**

- PCs armazenam caracteres por números   
- whitespaces – código/par que indica fim de linha em arquivos de texto   
- control characteres – controlar dispositivos E/S  
- **ASCII** (american standart code for information interchange) – padrão de codificação do alfabeto latim   
  - 8 bits \= 256 caracteres (128 letras, 128 resto) – não tanka  
  - 128 code points  
- **I18N** – cada programa deve ser escrito de um modo que pode ser usado em todo o mundo  
  - python3 é I18Ned  
- code point – número de um caractere (ex: espaço \= 32\)  
- code page – padrão de usar os 128 code points mais altos para armazenar caracteres nacionais  
  - um code point traduz caracteres diferentes em diferentes code pages  
- **Unicode** – atribui caracteres únicos para \+1M code points, não explica como codar/armazenar os caracteres na memória/arquivos  
  - 0 \- 128 – ASCII  
  - 0 \- 256 – linguagens do oeste europeu  
- **UCS-4** (universal character set) – técnicas para implementar Unicode nos PCs, 32 bits por caractere (número único Unicode)  
  - arquivo UCS-4 começa com um BOM (byte order mark) – combinação de bits não printável da natureza do conteúdo dos arquivos (ex: UTF-8)  
  - tamanho do texto 4x maior que ASCII  
- **UTF-8** (unicode transformation format) – utiliza quantos bit forem necessários para cada code point  
  - latim (8 bits), não-latim (16 bits), asiáticos (24 bits)  
  - não precisa de BOM

##### **string**

- sequências imutáveis, pode ser vazia  
- as vezes é melhor guardar e processar grandes valores numéricos como strings   
- métodos: [https://docs.python.org/3.4/library/stdtypes.html\#string-methods](https://docs.python.org/3.4/library/stdtypes.html#string-methods)   
- pode ser tratada como **lista** em alguns casos  
  - ex: espaçar letras – `for`  
    ```strin \= 'silly walks'  
    for i in range(len(strin)):  
        print(strin\[i\], end\=' ')  
    \#OU  
    for crct in strin:  
        print(crct, end\=' ')  
      
  - ex: fatias – `[:]`  
    print(strin\[1:3\])```  
      
- `in` & `not in`

  ```
  alphabet \= "abcdefghijklmnopqrstuvwxyz"

  print("f" in alphabet)

  print("F" in alphabet)

  print("1" in alphabet)

  print("ghi" in alphabet)

  print("Xyz" in alphabet)
  ```


- adicionar elementos – cria uma cópia da string a cada alteração, mas não é um problema

  ```
  alphabet \= "bcdefghijklmnopqrstuvwxy"

  alphabet \= "a" \+ alphabet

  alphabet \+= "z"


  print(alphabet)```

- não funciona (de string):  
  - delete\[indice\] (apenas para a string inteira)  
  - append  
  - insert  
      
- pode ser concatenada (+, nova string, ordem importa) e replicada (\*)  
- \\ – caractere de escape, não conta no lenght (mas o `n` do `\n` conta)  
  - ex: \\’ \== ‘  
- string de várias linhas  
  ```
  multiline\_string \= '''linha \#1  
  linha \#2  
  linha \#3'''  
    
  print(len(multiline\_string)) \#26 ``` 
- whitespace (invisível, contado) entre cada 2 linhas (\\n)  
- conjunto de 6 aspas conta 1 em lenght

###### ***métodos string***

- `ord()` – retorna código ASCII/Unicode de um valor code point (string de 1 caractere)  
- `chr()` – retorna caractere de um valor code point  
- `min()` – retorna elemento mínimo (valor menor) passado como argumento (não pode ser vazio)  
  ```
  print(min("aAbByYzZ")) \# A  
    
  t \= 'The Knights Who Say "Ni\!"'  
  print('\[' \+ min(t) \+ '\]') \# \[ \]  
    
  t \= \[0, 1, 2\]  
  print(min(t)) \# 0  ```
    
- `max()` – retorna elemento máximo (valor maior) passado como argumento (não pode ser vazio)  
  ```
  print(max("aAbByYzZ")) \# z  
    
  t \= 'The Knights Who Say "Ni\!"'  
  print('\[' \+ max(t) \+ '\]') \# \[y\]  
    
  t \= \[0, 1, 2\]  
  print(max(t)) \# 2  ```
    
- `index()` – retorna index da 1a ocorrência do argumento (0 \- len-1)  
  ```
  print("aAbByYzZaA".index("b")) \#2  
  print("aAbByYzZaA".index("Z")) \#7  
  print("aAbByYzZaA".index("A")) \#1 ``` 
    
- `list()` – pega o argumento e cria uma lista com os caracteres da string  
  `print(list("abcabc")) \#\['a', 'b', 'c', 'a', 'b', 'c'\]  `
    
- `count()` – conta as ocorrências do elemento na sequência  
  `print("abcabc".count("b")) \#2  
  print('abcabc'.count("d")) \#0 ` 
    
- `title()` – muda a 1a letra de cada palavra para maiúscula e o resto minúsculo  
`  print(" I know that 1.".title()) \# I Know That 1\.  
`    
- **`map`** `+ title()` – deixar 1a letra maiúscula de cada item de uma **lista** com MAP  
  ```short\_list \= \['mython', 'python', 'fell', 'on', 'the', 'floor'\]  
  new\_list \= list(map(lambda s: s.title(), short\_list))  
  print(new\_list) \# \['Mython', 'Python', 'Fell', 'On', 'The', 'Floor'\]  ```
    
- `capitalize()` – retorna uma nova string com os caracteres, se o 1o caractere for letra, deixa maiúscula e o resto minúsculo (se não for, não muda nada)  
  ```
  print('aBcD'.capitalize()) \#Abcd  
  print(' Alpha'.capitalize()) \# alpha  
  print('123'.capitalize()) \#123 ``` 
    
- `lower()` – copia a string e deixa tudo em letras minúsculas e retorna o resultado   
  print(" SiGmA=60".lower()) \# sigma=60  
    
- `upper()` – copia a string e deixa tudo em letras maiúsculas e retorna o resultado   
  print(" SiGmA=60".upper()) \# SIGMA=60  
    
- `swapcase()` – nova string trocando minúscula por maiúscula e vice versa  
  print("I am 6t@$hfO.".swapcase()) \#i AM 6T@$HFo.  
    
- `center()` – copia a string e tenta centralizar em uma largura especificada (adicionando espaços/caractere antes e depois), se a largura for pequena, retorna a string original  
  print('\[' \+ 'oii'.center(8) \+ '\]') \#\[  oii   \]  
  print('\[' \+ 'oii'.center(8, '\*') \+ '\]') \#\[\*\*oii\*\*\*\]  
    
- `endswith()` – checa se termina com caractere (True ou False)  
  t \= "zeta"  
  print(t.endswith("a")) \#True  
  print(t.endswith("A")) \#False  
    
- `isdigit()` – checa se começa com caractere (True ou False)  
  print("omega".startswith("meg")) \#False  
  print("omega".startswith("om")) \#True

- `find()` – parecido com *index* (retorna index da 1a ocorrência da substring) mas não dá erro e é só para strings (para 1 caracter, usar *in*)  
  - 2o argumento começa a contar a partir daquele index  
  - 3o argumento é o limite (1o index a não ser contado)

```
  print("Eta".find("ta")) \#1

  print("Eta".find("mma")) \#-1

  print('kappa'.find('a', 2)) \#4

  print('kappa'.find('a', 1, 4)) \#1


  \#ENCONTRAR TODAS AS OCORRÊNCIAS DE UMA SUBSTRING

  the\_text \= """A variation of the ordinary lorem ipsum

  text has been used in typesetting since the 1960s

  or earlier, when it was popularized by advertisements

  for Letraset transfer sheets."""


  fnd \= the\_text.find('the')

  while fnd \!= \-1:

      print(fnd)

      fnd \= the\_text.find('the', fnd \+ 1) \#15 80 198
```

- `rfind()` – find mas começa a buscar do final  
  print("tau tau tau".rfind("ta")) \#8  
  print("tau tau tau".rfind("ta", 9)) \#-1  
  print("tau tau tau".rfind("ta", 3, 9)) \#4  
    
- `isalnum()` – checa se tem apenas números ou letras, retorna True ou False  
  print('lambda30'.isalnum()) \#True  
  print('lambda\_30'.isalnum()) \#False  
  print(''.isalnum()) \#False  
  print(' '.isalnum()) \#False  
    
- `isalpha()` – checa se tem apenas letras  
  print("Moooo".isalpha()) \#True  
  print('Mu40'.isalpha()) \#False  
    
- `normalize(‘NFD’, dic)` – separa acentos e etc e retorna texto pelado (import unicode)  
  stream \= unicodedata.normalize('NFD', stream)  
    
- `isdigit()` – checa se tem apenas dígitos  
  print("123".isdigit()) \#True  
  print('Mu40'.isdigit()) \#False  
    
- `islower()` – variante do isalpha, apenas letras minúsculas  
  print("Hi".islower()) \#True  
  print('mooo'.islower()) \#False  
    
- `IN string.ascii_lowercase` – apenas letras minúsculas peladas  
  *if* c in string.ascii\_lowercase:  
    
- `isupper()` – variante do isalpha, apenas letras maiúsculas  
  print("Hi".isupper()) \#False  
  print('MOOOO'.isupper()) \#True  
    
- `isspace()` – checa se é espaço (\\n conta)  
  print(' \\n '.isspace()) \#True  
  print(" ".isspace()) \#True  
  print('mooo '.isspace()) \#False  
    
- `join()` – recebe uma lista (todos os elementos strings), junta tudo em uma lista, a string da qual o método foi invocado é usada como separador  
  print(",".join(\["omicron", "pi", "rho"\]))  
  \# omicron,pi,rho  
    
- `split()` – corta a string (por espaço) e retorna uma lista das substrings (reverso de join)  
  print("phi       chi\\npsi".split()) \# \['phi', 'chi', 'psi'\]  

```    
  \#varios espaços conta como 1 so  
    
  def mysplit(strng):  
      lista \= \[\]  
      first \= end \= 0  
        
      for i in range(len(strng)):  
          if strng\[i\].isspace():  
              \# space \= strng\[i\]  
              continue  
            
          if strng\[i\].isalpha():  
              first \= strng\[i\] \#guarda inicio  
              end \= strng.find(' ', i)  
            
              lista.append(strng\[i:end\])  
            
          \#se for espaço ultimo eh posicao do el \+1?  
      return lista  
    
    
  print(mysplit("To be or not to be, that is the question"))  
  print(mysplit("To be or not to be,that is the question"))  
  print(mysplit("   "))  
  print(mysplit(" abc "))  
  print(mysplit(""))  
```  
        
    
    
- `lstrip()` – remove os espaços, \\t e \\n (default) a esquerda e retorna uma nova string   
  - `lstrip(“abc”)` – remove caracteres da string (parametro) até achar um diferente (aí para)
```
  print("\[" \+ " tau ".lstrip() \+ "\]") \# \[tau \]

  print("www.cisco.com".lstrip("w.")) \#cisco.com

  print("http://pythoninstitute.org".lstrip("http://")) \# pythoninstitute.org
```

- `rstrip()` – remove os espaços, \\t e \\n (ou argumento) a direita e retorna uma nova string   
```
  print("\[" \+ " aaa ".rstrip() \+ "\]") \#\[ aaa\]  
  print("cisco.com".rstrip(".com")) \#cis  
    
- `strip()` – remove os espaços/argumentos da esquerda e direita  
  print("\[" \+ "   oi   ".strip() \+ "\]") \#\[oi\] 
```

- `replace(a, b, c)` – retorna cópia da string original com todas as ocorrências substituídas  
  - 3o parâmetro limita as ocorrências 
```

  print("This is it".replace("is", "are")) \#Thare are it

  print("This is it".replace("is", "are", 1)) \#Thare is it

  print("Apple Juice".replace("juice", "")) \#Apple Juice 
```

- `sorted(lista)` – retorna nova lista com os argumentos ordenados pela ordem ASCII (maiúsculas vem 1o)  
``` 
  first \= \['o', 'a', 'p', 'g'\]  
  scnd \= sorted(first) \#\['a', 'g', 'o', 'p'\]  
    
  s1 \= 'Where are the snows of yesteryear?'  
  s2 \= s1.split() \# \['Where', 'are', 'the', 'snows', 'of', 'yesteryear?'\]  
  s3 \= sorted(s2) \# \['Where', 'are', 'of', 'snows', 'the', 'yesteryear?'\] 
```

- `sort(lista)` – altera a lista original (ordena)   
```
  first \= \['o', 'a', 'p', 'g'\]  
  first.sort() \#\['a', 'g', 'o', 'p'\] 
```

- `str(numero)` – converte número para string

- `int/float(strng)` – converte string para número (se a string não for apenas números, da ValueError)  
- 

###### 

**comparar string**

- compara valor do código ASCII/Unicode caractere por caractere (1o)  
- mesmo se a string só contém números, é interpretada como string  
``` 
  print('10' \== '010') \#False  
  print('10' \> '010') \#True  
  print('10' \> '8') \#False  
  print('20' \< '8') \#True  
  print('20' \< '80') \#True  
  print('Sao' \< '1000') \#True – ‘S’ (83) \> ‘1’ (49)  
```  
- se compara 2 strings de diferentes tamanhos e a menor é idêntica ao início da maior, menor \< maior \= True  
  'alpha' \< 'alphabet'  
- é case sensitive (upper \< lower)  
  'beta' \> 'Beta'  
- se compara string com inteiros: \== (False) e \!= (True), outros  símbolos (\>, \<) dá TypeError exception   
```
  print('10' \== 1) \#False  
  print('10' \!= 1) \#True  
  print('10' \> 10) \#TypeError   
```
    
- similaridade entre strings: Hamming distance e Levenshtein distance  
  - algoritmo Soundex (1918)

###### *Cifra de Caesar (encriptação)*
 
```
\# Caesar cipher \- apenas letras em latim, tudo maiusculo  
text \= input("Enter your message: ")  
cipher \= '' \#string vazia  
for char in text:  
    if not char.isalpha():  
        continue  
    char \= char.upper() \#sempre converte para maiusculo  
    code \= ord(char) \+ 1 \#pega o codigo ascii \+ 1 (proxima)  
        \#DES \= ord(char) \- 1  
    if code \> ord('Z'): \#se passar de Z, volta para A  
        \#DES \= if code \< ord('A'):  
        code \= ord('A')  
            \#DES \= ord('Z)  
    cipher \+= chr(code) \#converte de volta para char e adiciona na string

print(cipher)   
```
   

#### Variáveis & operadores

- tipagem dinâmica, não declara na variável  
- guarda nome e valor, é case sentitive  
- retorna valor como string (default)  
- declarar várias  
  **a, b, c \= 1, 2, 3**  
- keywords:   
```
  \['False', 'None', 'True', 'and', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield'\]
```
- self commenting: nome da variável explica o que guarda  
    
- int, float, str (‘’ ou “”), bool (True ou False)  
  - 2 \== 2.0 (True, 1\)  
  - False \== 0
 
```
  nome \= "Ana"

  nota \= 8.5

  aprovado \= nota \>= 7 \#true ou false

  print(f"nome: {nome}, aprovado: {aprovado}")

- inicializar várias variáveis na mesma linha  
      a, b, c \= 0, 0, 0 
```


- ###### *variável global (dentro de função)*

  - se alterar o valor dentro da função, sobrescreve a variável

  global nome1, nome2

- ###### *verificar se é de um tipo de dado*

  type(value) is int

- ###### ***divide** os números por espaço*

- ###### ***\[map\] converte** para inteiros* 
 
```
  x, y \= map(int, input("números separados por espaço: ").split())  
    \# OU  
  entrada\_str \= input("números separados por espaço: ") \# "10 25 30 15"  
  lista\_de\_strings \= entrada\_str.split() \# \["10", "25", "30", "15"\]  
  \# para inteiros  
  lista\_de\_numeros \= list(map(int, lista\_de\_strings)) 
```

- ###### *input do tipo **int***

  n \= int(input("digite o valor: "))

#### 

- print(f “...”) – imprime  
    
  **Operadores**  
- \+ – adição  
  - concatena strings em 1 só
 
```
  a \+ a \= aa

- / – divisão (sempre float)  
  - o resultado da divisão do número inteiro é sempre arredondado para o valor inteiro mais próximo que é menor que o resultado real (não arredondado)  
- // – divisão inteira ou de piso  
  –2 // 4 \= \-1  
- % – resto ou módulo: esquerda → direita  
  2 % –4 \= \-2  
- \* – multiplicação  
  - replica strings

  5 \* “2” \= “22222”

- \*\* potenciação: direita → esquerda  
  print(2 \*\* 2 \*\* 3\) \= 256  
  2 \*\* 3 \= 8 → 2 \*\* 8 \= 256 
```

#### 

#### **Lógica – bits**

- 0 \= False  
  - \> 0 \= True  
  - not → and → or  
  - não vão a nível de bit, veem apenas o valor inteiro final
 
```
  not (p and q) \== (not p) or (not q)

  not (p or q) \== (not p) and (not q)


  z \= 10

  y \= 0

  x \= y \< z and z \> y or y \> z and z \< y

  \# x \= 0 \< 10 and 10 \> 0 or 0 \> 10 and 10 \< 0

  \# x \= True and True or False and False

  \# x \= (True and True) or (False and False)

  \# x \= True or False

  \# x \= True 
```


- ###### ***operadores bit a bit (0s e 1s)***

  - lida com cada bit: se a variável ocupa 64 bits, avalia cada par de bits  
  - & conjunção bit a bit  
  - | disjunção bit a bit  
  - \~ negação bit a bit  
    - complemento de 2: \~n \= –(n \+ 1\)  
  - ^ bit a bit exclusivo (xor)

| A | B | A & B | A | B | A ^ B | \~A | \~B |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| 0 | 0 | 0 | 0 | 0 | 1 | 1 |
| 0 | 1 | 0 | 1 | 1 | 1 | 0 |
| 1 | 0 | 0 | 1 | 1 | 0 | 1 |
| 1 | 1 | 1 | 1 | 0 | 0 | 0 |

- ###### ***flag\_register***

- variável com valor 0x1234 (32 bits) que armazena vários aspectos do SO  
- manipular apenas o 3o bit (0000000000000000000000000000x000)  
- **máscara de bit**: para manipular apenas 1 bit  
  - para acessar o bit x: the\_mask \= 8 (2^x)  
  - **verificar estado** do bit 3 (&): res \= flag\_register & the\_mask  
    - se for 1, res \= 8 (...001000)  
    - se for 0, res \= 0 (...000000)  
    - bit & 0 \= 0 (desliga)  
    - bit & 1 \= bit (mantém estado)

     

  - **definir o bit 3 para 1** (|): flag\_register \= flag\_register | the\_mask  
    - bit é comparado com o 1 da máscara, se for 0 passa a ser 1

     

  - **redefinir o bit 3 para 0** (&\~): inverte a máscara  
    - flag\_register \= flag\_register & \~the\_mask  
    - outros bits são comparados com a máscara invertida (& 1\) e mantêm estado, bit 3 passa a ser 0

     

  - **negar o bit 3** (inverter, ^ xor): é 1 se os bits forem diferentes  
    - bit ^ 1 \= \~bit  
    - bit ^ 0 \= bit (mantém)  
    - flag\_register \= flag\_register ^ the\_mask – bit 3 é invertido

     

  - resumo


| objetivo | operador | máscara | o que faz |
| :---- | :---- | :---- | :---- |
| verificar bit 3 | & | the\_mask …001000 | isola o bit 3 (zera os outros) res é 8 ou 0 |
| definir (ligar) bit 3 | | | the\_mask …001000 | força o bit 3 para 1 (mantém os outros) |
| redefinir (desligar) bit 3 | & | \~the\_mask …110111 | força o bit 3 para 0 (mantém os outros) |
| negar (inverter) bit 3 | ^ | the\_mask …001000 | inverte o bit 3 (mantém os outros) |

###### ***deslocamento binário (bits)***

- para valores inteiros, 1 bit \=2  
- deslocar um bit para a esquerda \= \*2^bits  
  - valor \<\< bits  
- deslocar um bit para a direita \= //2^bits  
  - valor \>\> bits

var \= 17  
var\_right \= var \>\> 1 \# 17 // 2^1 \= 8  
var\_left \= var \<\< 2 \# 17 \* 2^2 \= 68  
print (var, var\_left, var\_right)  
\# 17 68 8

- exemplos

x \= 15 \# 0000 1111  
y \= 16 \# 0001 0000

a \= x & y \# é 1 se os dois bits forem 1 → x & y \= 0000 0000 \= 0

b \= x | y \# é 1 se pelo menos um bit for 1 → x | y \= 0001 1111 \= 31

c \= \~x \# \~15 \= –(15 \+ 1\) \= –16

d \= x ^ 5 \# é 1 se os dois bits forem diferentes → 0000 1111 ^ 0000 0101 \= 0000 1010 \= 10

e \= x \>\> 2 \# x // 2^2 \= 3 \= 0000 0011

f \= x \<\< 2 \# x \* 2^2 \= 60 \= 0011 1100

print(a, b, c, d, e, f) \# 0 31 –16 10 3 60

#### **Tabela de prioridades**

| Prioridade | Operador |  |
| :---- | ----- | :---- |
| 0 | **()** | sub expressões |
| 1 | **\+   –   \~   not** | unário (1 operador): operadores unários localizados próximos à direita do operador de potência são mais fortes, ex: 4 \*\* –1 \= 0.25 ex: –1, \+3 \~: negação bitwise not: negação lógica (inverte true e false) |
| 2 | **\*\*** | direita → esquerda ex: 2 \*\* 2 \*\* 3 \= 256 |
| 3 | **\*   /   //   %** |  |
| 4 | **\+    –** | binário (2 operadores) ex: 4 \+ 5, 12 % 5 |
| 5 | **\<\<   \>\>** | deslocamento de bits (bitwise shift) |
| 6 | **&** | AND (bitwise) |
| 7 | **^** | XOR (bitwise) |
| 8 | **|** | OR (bitwise) |
| 9 | **\<   \>   \<=   \>=** | comparação de ordem |
| 10 | **\==   \!=** | comparação de igualdade |
| 11 | **and** | E lógico |
| 12 | **or** | OU lógico |
| 13 | **\=   \+=   –=   \*=   /=   %=   &=   ^=   |=   \>\>=   \<\<=** |  |

#### Condicionais & loops

- pode usar ELSE como exceção (se não executou o brake no laço)  
  - for …  
    else: …  
- elif – else if  
  while number \!= 0  \==  while number  
  if number % 2 \== 1  \==  if number % 2                            

- ###### break – quebra o loop

- continue – próxima iteração

- ###### ***for (int i \= 0; i \< 5; i \+= 2\)***

  for i in range(5):  
      print({i})  
  \# 0 1 2 3 4  
    
  for i in range(2, 8):  
      print({i})  
  \# 2 3 4 5 6 7  
    
  \#for (int i \= 0; i \< 100; i \+= 2\)  
  for i in range(0, 100, 2):  
      print(i)  
  \# 0 2 4 5 8 …  
    
  \# FOR – ELSE: se o loop terminou por brak, nao executa o else  
  i \= 111  
  for i in range(2, 1):  
      print(i)  
  else:  
      print(“else: ”i)  
  \# else: 111  
    
  for i in range(5):  
      print(i)  
  else:  
      print(“else: ”i)  
  \# 1 2 3 4 else: 4  
    
  n \= range(4)  
  for num in n:  
      print(num \- 1\)  
  else:  
      print(num)  
  \# \-1 0 1 2 3 

- ###### ***posição & valor***

  \# i \= posição, number\_char \= caractere \-\> https://realpython.com/python-enumerate/  
  for i, number\_char in enumerate(reversed(number)):  
      n \= int(number\_char)  \# each number to int  
      if i % 2 \== 1:  
          n \*= 2  
    
- while (condição)  
  count \= 0*;*  
  while count \< 5:  
      print({count})  
      count \+= 1 \#count++ não funciona  
  \#saída:  
  \# {0} {1} {2} {3} {4}   

- ###### ***se é /contém palavra/nome***

  only\_letters \= True if input().isalpha() else False  
    
  if "joao" in row\["name"\]:  
  if letter in ‘AEIOU’:


#### 

#### **Funções**

- blocos de código reutilizáveis para uma tarefa – assinatura, parâmetros opcionais, parâmetros variáveis   
- funções python: [https://docs.python.org/3/library/functions.html](https://docs.python.org/3/library/functions.html)   
- decomposição: cada parte do código pode ser codificada e testada separadamente, dividir projeto em partes menores → módulos  
- por default retorna *None*  
- de onde vêm: python, módulos pré instalados, próprio código  
- *parâmetro*: dentro da função  
- *argumento*: fora da função  
- função recebe o valor, não a variável – se mudar o valor dentro da função, não muda a variável  
```
  \#Recebe nome como parâmetro  
  def saudar(nome):  
      """sei la"""  
      print(f"Ola {nome}\!")  
    
  \#Calcula e retorna valor  
  def somar(x, y):  
      return x \+ y  
    
  \#chamar  
  saudar("Ana")  
  a \= 5  
  b \= 1  
  print(f"{a} \+ {b} \= {somar(a, b)}") \#saída: 5 \+ 1 \= 6  
```  
    
- **print** (default): print(objetos, sep=‘ ’, end=‘\\n’, …)  
  - recebe argumento, converte para human friendly, mostra resultado no output

   print("?" \* 4, end=" ") \# ????

   print("aaaaaaaaa") \# ????aaaaaaaaa

  \# matriz 3x3

  for i in range(3):

      print("?" \* 3)

- imprimir várias linhas  
- print(  
- """  
- \+================================+  
- | Welcome to my game, muggle\!    |  
- | So, what is the secret number? |  
- \+================================+  
- """  
- )

- var (string) \= **input** (“Digite: ”)  
  - var \= float ou int(input(“valor: ”))

   

- **keyword argument passing**  
  - passar 1o argumentos de posição – tanto ao chamar quanto na função em si  
- def introduction(first\_name, last\_name):  
-     print("Hello, my name is", first\_name, last\_name)  
-   
- introduction(first\_name \= "James", last\_name \= "Bond")  
- introduction(last\_name \= "Skywalker", first\_name \= "Luke")  
- introduction("James", last\_name \= "Bond")  
- \# ERRO  
- introduction("Skywalker", first\_name \= "Luke")


  - argumentos definidos na função – default: pode sobrescrever ou não  
  - def introduction(first\_name="John", last\_name="Smith"):  
  -      print("Hello, my name is", first\_name, last\_name)  
  -   
  - introduction("Henry") \# My name is Henry Smith  
  - introduction(first\_name="William") \# My name is William Smith  
  - introduction() \# My name is John Smith

- passar **resultado de função como parâmetro** de função direto  
- print(bmi(weight \= lb\_to\_kg(176), height \= ft\_and\_inch\_to\_m(5, 7)))


- str(float ou int)  
  - passar o resultado de uma conta em 1 variável (string)  
  - leg\_a \= float(input("Input first leg length: "))  
  - leg\_b \= float(input("Input second leg length: "))  
  - print("Hypotenuse length is " \+ str((leg\_a\*\*2 \+ leg\_b\*\*2) \*\* .5))


  - substituir caractere por outro (ex: espaço por nada)

  replace(" ", "")

  - separar cada argumento do print por um caractere – sep

   print("a", "b", "c", "d", sep=" \- ") \# a \- b \- c \- d


- scanf (default \= string) – var \= input(“text: “)  
  - n \= int(input("number: ")) \# scanf(“%d”)  
    

- ###### ***compactar** função*

  - def is\_a\_triangle(a, b, c):  
  -     \# original  
  -     if a \+ b \<= c or b \+ c \<= a or c \+ a \<= b:  
  -         return False  
  -     return True  
  -     \# compacta  
  -     return a \+ b \> c and b \+ c \> a and c \+ a \> b  
  -   
  - print(is\_a\_triangle(1, 1, 1))  
  - print(is\_a\_triangle(1, 1, 3))


- ###### ***Main***

  - default – cima para baixo  
  - especificar main (última função do código) – definir ordem de execução das funções  
    if \_\_name\_\_ \== "\_\_main\_\_":  
        main()

    
- `capitalize()` – 1a letra para maiúscula  
- `lower()` – tudo para minúsculas  
- `upper()` – tudo para maiúsculas  
- `range(fim)` – um valor por vez até ‘fim’  
- `isnumeric()` – se uma string tem apenas números (True/False)  
- `isalpha()` – se uma string tem apenas letras (True/False)  
- `items()` – dicionário para lista  
- `sum(array)` – soma valores de um array  
- `next(lista)` – próxima iteração / elemento  
- `type(var/obj)` – tipo da variável / classe do objeto  
  - type(obj).\_\_name\_\_ *\# (obj.\_\_name\_\_) \= ERRO*  
- `len(array)` – quantidade de elementos do array  
- `max(a, b, c)` – maior valor  
- `min(a, b, c)` – menor valor

##### 

##### **Geradores (iterador)**

- pedaço de código que produz valores e controla o processo de iteração  
- retorna uma série de valores (enquanto funções só retornam um)  
- um objeto pode ser usado de iterador se responde positivamente a invocação do *\_\_iter\_\_* – dá um objeto que pode ser usado como iterador  
- **protocolo iterador** – modo de um objeto se comportar conforme regras impostas pelo contexto do *for* / *if*  
  - **iterador** – objeto conforme o protocolo  
- **`__iter__(self)`** – chamado quando o loop for começa, retorna o próprio objeto iterador (uma vez) – permite que um objeto seja iterado  
- **`__next__(self)`** – chamado a cada volta do loop para próximo valor (ou exceção para parar)

```
class I:  
    def \_\_init\_\_*(self)*:  
        self.s \= 'abc'  
        self.i \= 0

    \# chamado quando o for começa, retorna o objeto iterador  
    def \_\_iter\_\_*(self)*:  
        return self

    \# chamado a cada iteração para obter o próximo valor  
    def \_\_next\_\_*(self)*:  
        \# verifica se ja foi todos os caracteres  
        if self.i \== len(self.s):  
            raise StopIteration \# acabou o for  
        v \= self.s\[self.i\] \# aumenta contador  
        self.i \+= 1  
        return v

for x in I():  
    print(x,end\='') \# abc  
    \# I() cria instancia da classe com s \= 'abc' e i \= 0  
    \# for chama I.\_\_iter\_\_() para obter o iterador (self)  
    \# for chama I.\_\_next\_\_() para atualizar o indice  
    \# termina o loop com StopIteration quando i \== len(s)
```

- ex fibonacci

```
\# classe iterador \- calcula os numeros conforme solicitados  
class Fib:  
    def \_\_init\_\_*(self, nn)*:  
        self.\_\_n \= nn \# limite  
        self.\_\_i \= 0 \# contador (atual)  
        self.\_\_p1 \= self.\_\_p2 \= 1 \# define os 1os 2 numeros

    def \_\_iter\_\_*(self)*: \# permite que o objeto seja iterado  
        print("Fib iter")  
        return self

    def \_\_next\_\_*(self)*: \# gera o proximo valor  
        self.\_\_i \+= 1 \# incrementa contador  
        if self.\_\_i \> self.\_\_n: \# se chegou ao fim  
            raise StopIteration \# para  
        if self.\_\_i in \[1, 2\]: \# se for 1o ou 2o numero  
            return 1  
        \# atualiza: 2o vira 1o e novo vira 2o  
        ret \= self.\_\_p1 \+ self.\_\_p2  
        self.\_\_p1, self.\_\_p2 \= self.\_\_p2, ret  
        return ret
```

\# objeto iteravel que usa o iterador Fib  
class Class:  
    def \_\_init\_\_*(self, n)*: \# recebe tamanho n  
        self.\_\_iter \= Fib(n) \# cria uma instancia de Fib (delega os calculos)

    def \_\_iter\_\_*(self)*: \# metodo chamado pelo for  
        print("Class iter")  
        return self.\_\_iter \# retorna o objeto (iterador) Fib

object \= Class(8)

for i in object:  
    print(i)

\# Class iter \-- for recebe objeto Fib  
\# 1 \-- Fib.\_\_next\_\_  
\# 1  
\# 2  
\# 3  
\# 5  
\# 8  
\# 13  
\# 21

##### 

###### ***yield \+ list comprehension***

- primo do *return*  
- transforma a função em um gerador – providencia o valor da expressão, mas não perde o estado da função  
  - variáveis pausadas até a próxima chamada (não recomeça como seria com *return*)  
- comprehension \= \[...\] → len() funciona  
- generator \= (...) → len() causa TypeError

```
def powers\_of\_2*(n)*:  
    power \= 1  
    for i in range(n):  
        yield power  
        power \*= 2

for v in powers\_of\_2(8):  
    print(v) \# 1 2 4 8 16 32 64 128
```

**\# LIST COMPREHENSION – \# \[expression for element in lista if conditional else expression\_2\]**  
\# pares \= \[n **for** n **in** numeros **if** n % 2 \== 0 **else** 0\]  
\# the\_list \= \[1 **if** x % 2 \== 0 **else** 0 **for** x **in** range(10)\]  
**\# for v in** **\[**1 **if** x % 2 \== 0 **else** 0 **for** x **in** range(10)**\]**: – lista criada (existe)  
**\# for v in** **(**1 **if** x % 2 \== 0 **else** 0 **for** x **in** range(10)**)**: – não existe lista (apenas gera)  
t \= \[x for x in powers\_of\_2(5)\]  
print(t) \# \[1, 2, 4, 8, 16\]

\# **RESULTADOS PARA UMA LISTA** real  
t \= list(powers\_of\_2(4))  
print(t) \# \[1, 2, 4, 8\]

\# com **OPERADOR IN**  
for i in range(20):  
    if i in powers\_of\_2(4):  
        print(i) \# 1 2 4 8

\# **fibonacci**  
```
def fibonacci*(n)*:  
    p \= pp \= 1  
    for i in range(n):  
        if i in \[0, 1\]:  
            yield 1  
        else:  
            n \= p \+ pp  
            pp, p \= p, n  
            yield n
```

fibs \= list(fibonacci(10))  
print(fibs) \# \[1, 1, 2, 3, 5, 8, 13, 21, 34, 55\]

###### ***lambda*** 

- função anônima, retorna valor da expressão levando em conta o valor atual do argumento lambda

\# função anonima (não mais \- variavel 'two') sem parametros que sempre retorna 2  
two \= lambda: 2  
\# função anonima com 1 parametro que retorna o quadrado do parametro  
sqr \= lambda x: x \* x  
\# função anonima com 2 parametros que retorna o 1o elevado ao 2o  
pwr \= lambda x, y: x \*\* y

for a in range(\-2, 3):  
    print(sqr(a), end\=" ")  
    print(pwr(a, two()))

\# 4 4  
\# 1 1  
\# 0 0  
\# 1 1  
\# 4 4

\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#  
def print\_function*(args, fun)*: \# lista de argumentos e função chamada (quantidade de valores do 1o parametro) vezes  
    for x in args:  
        print('f(', x,')= ', fun(x), sep\='')

\# def poly(x):  
\#     return 2 \* x\*\*2 \- 4 \* x \+ 2 \#f(x) \= 2x^2 \- 4x \+ 2

\# print\_function(\[x for x in range(-2, 3)\], poly)  
print\_function(\[x for x in range(\-2, 3)\], lambda x: 2 \* x\*\*2 \- 4 \* x \+ 2)

\# f(-2)= 18  
\# f(-1)= 8  
\# f(0)= 2  
\# f(1)= 0  
\# f(2)= 2

###### *lambda \+ map()*

- aplica a função passada no 1o argumento em todos os elementos do 2o argumento e retorna um iterador com todos os resultados  
  \# map(function, list)  
  list\_1 \= \[x for x in range(5)\] \# \[0, 1, 2, 3, 4\]  
  list\_2 \= list(map(lambda x: 2 \*\* x, list\_1)) \# \[1, 2, 4, 8, 16\]  
  print(list\_2) \# \[1, 2, 4, 8, 16\]  
    
  for x in map(lambda x: x \* x, list\_2):  
      print(x, end\=' ') \# 1 4 16 64 256  
  print()

  ###### *lambda \+ filter()*

- filtra o 2o argumento de acordo com a função de 1o argumento (True)  
  from random import seed, randint  
    
  seed()  
  data \= \[randint(\-10,10) for x in range(5)\]  
  filtered \= list(filter(lambda x: x \> 0 and x % 2 \== 0, data))  
    
  print(data) \# todos  
  print(filtered) \# positivos pares  
    
  \# passar **só strings para nova lista**  
  short\_list \= \[1, "Python", \-1, "Monty"\]  
  new\_list \= list(filter(lambda s: isinstance(s, str), short\_list))  
  print(new\_list)

##### 

##### **Closure**

- técnica que permite guardar valores quando o contexto não existe mais (ex: guardar valor de variável de função após terminar execução, fora da função)  
- pode modificar comportamento com valores de fora  
- é a função retornada na execução de *outer()*  
- condições  
  - ter uma função dentro de outra  
  - função interna usa uma variável externa (loc)  
  - função externa retorna a interna sem executar – ex: retorna *power*, não *power()*

  ###### ***outer()***

- retorna uma cópia da função *inner()* em si no momento que *outer()* foi chamada – com o estado de todas as variáveis

  ###### ***inner()***

- “ferramenta” do *outer()*, só pode ser chamada dentro da função *outer()*  
- retorna o valor da variável acessível dentro do seu escopo, pode usar todas as entidades disponíveis para *outer()*

```
def outer*(par)*:  
    loc \= par

    def inner*()*:  
        return loc  
    return inner
```

var \= 1  
fun \= outer(var)  
print(fun())

\# com argumentos  
```
def make\_closure*(par)*:  
    loc \= par \# variavel privada da closure

    def power*(p)*:  
        return p \*\* loc  
    return power  
    \# retorna um 'pacote' com a função power e o valor loc
```

fsqr \= make\_closure(2) \# 'pacote' com power e loc \= 2 (^2)  
fcub \= make\_closure(3) \# outro 'pacote' com power e loc \= 3 (^3)

for i in range(5):  
    print(i, fsqr(i), fcub(i))

\# 0 0 0  
\# 1 1 1  
\# 2 4 8  
\# 3 9 27  
\# 4 16 64

\#\#\#\#\#\#\#\#\#  
```
def tag*(tg)*:  
    tg2 \= tg  
    tg2 \= tg\[0\] \+ '/' \+ tg\[1:\]

    def inner*(str)*:  
        return tg \+ str \+ tg2  
    return inner
```

b\_tag \= tag('\<b\>')  
print(b\_tag('Monty Python')) \# \<b\>Monty Python\</b\>

- ###### ***média** de valores*

  score \= \[1, 9, 6, 4\]  
  print(f"average: {sum(score) / len(score)}")

- ###### ***valor ignorando sinal***

  abs(v1 \- v2)

- ###### ***map***

- ex: converte para inteiros  
  x, y \= map(int, input("números separados por espaço: ").split())  
      \# OU  
  entrada\_str \= input("números separados por espaço: ") \# "10 25 30 15"  
  lista\_de\_strings \= entrada\_str.split() \# \["10", "25", "30", "15"\]  
  \# para inteiros  
  lista\_de\_numeros \= list(map(int, lista\_de\_strings))

- ###### ***filter***

- retorna apenas os True  
- ex: números pares  
```
  numeros \= \[1, 2, 3, 4, 5, 6, 7, 8\]  
    
  def eh\_par(n): \# filtrar apenas os números pares  
      return n % 2 \== 0 \#True / False  
    
  numeros\_pares \= list(filter(eh\_par, numeros))  
  print(f"Números pares: {numeros\_pares}") \# Saída: \[2, 4, 6, 8\]
```

- ###### ***\[map, filter\] list comprehension***

  - lista criada na execução do programa

\[expression for element in lista if conditional\]  
\#mesma coisa que  
for element in list:  
    if conditional:  
        expression

```
my\_list \= \[1, 2, 3\]  
for v in range(len(my\_list)): \#for v in 0, 1, 2  
    my\_list.insert(1, my\_list\[v\])  
        \# my\_list\[0\] \= 1 \-\> (1, 1\) \-\> \[1, 1, 2, 3\]  
        \# my\_list\[1\] da lista modificada \= 1 \-\> (1, 1\) \-\> \[1, 1, 1, 2, 3\]  
        \# my\_list\[2\] da lista modificada \= 1 \-\> (1, 1\) \-\> \[1, 1, 1, 1, 2, 3\]  
        \# inserções empurram os valores originais (2, 3\) para a direita  
print(my\_list)
```

```
lista\_strings \= \["10", "25", "30", "15"\]  
numeros \= \[1, 2, 3, 4, 5, 6, 7, 8\]

\# MAP  
lista\_de\_numeros \= \[int(s) for s in lista\_strings\]

\# lista de quadrados a partir de 0  
squares \= \[x \*\* 2 for x in range(10)\] \# (0, 1, 4, 9, 16, 25, 36, 49, 64, 81\)

\# lista dos quadrados ímpares   
odds \= \[x for x in squares if x % 2 \!= 0 \] \# (1, 9, 25, 49, 81\)

\# lista de potências de 2  
twos \= \[2 \*\* i for i in range(8)\] \# (1, 2, 4, 8, 16, 32, 64, 128\)

\# FILTER  
numeros\_pares \= \[n for n in numeros if n % 2 \== 0\]

print(f"Comprehension (map): {lista\_de\_numeros}")  
print(f"Comprehension (filter): {numeros\_pares}")
```

- ###### ***reduce** – externa*

```
  \#importar  
  from functools import reduce  
    
  numeros \= \[1, 8, 5, 1, 6, 15\]  
  """ reduce(funcao 2 argumentos, lista)  
  acumulador: resultado ate o momento """  
    
    
  \# Multiplicando todos os números da lista \- reduce é melhor  
  produto \= reduce(lambda x, y: x \* y, numeros)  
  print(produto) \# Saída: 3600  
  """ x: acumulador, y: elemento atual  
      2 1os itens \-\> x \= 1, y \= 8  
      x \* y retorna 8 \-\> acumulador \= 8  
    
      acc \* próximo item \-\> x \= 8, y \= 5  
      x \* y retorna 40 \-\> acc \= 40  
      ...  
      total acc \= 3600 """  
    
    
  \# Somando todos os números da lista \- sum(lista) é melhor  
  soma \= reduce(lambda x, y: x \+ y, numeros)  
  print(soma)  \# Saída: 36  
  """ x: acumulador, y: elemento atual  
      reduce pega os 2 1os itens \-\> x \= 1, y \= 8  
      x \+ y retorna 9 \-\> acumulador \= 9  
    
      reduce pega acc e próximo item \-\> x \= 9, y \= 5  
      x \+ y retorna 14 \-\> acc \= 14  
    
      reduce pega acc e próximo item \-\> x \= 14, y \= 1  
      x \+ y retorna 15 \-\> acc \= 15  
      ...  
      total acc \= 36 """  
    
    
  \# Maior número da lista \- max(lista) é melhor  
  maior \= reduce(lambda x, y: x if x \> y else y, numeros)  
  print(maior) \# Saída: 15  
  """ lambda: se x \> y retorna x, se não retorna y  
      2 1os itens \-\> x \= 1, y \= 8  
      8 \> 1 \-\> retorna 8 \-\> acumulador \= 8  
    
      acc e próximo item \-\> x \= 8, y \= 5  
      8 \> 5 \-\> retorna 8 \-\> acumulador \= 8  
      ...  
      acc e próximo item \-\> x \= 8, y \= 15  
      8 \< 15 \-\> retorna 15 \-\> acumulador \= 15  
    
    
      total acc \= 15 """
```

  ###### 

- ###### ***recursão***

  - função chama a si mesma, tem uma condição de parada *no início*  
  - consome mais memória   
  - fibonacci  
  - def fib(n):  
  -     if n \< 1: \# condição de parada  
  -         return None  
  -     if n \< 3: \# condição de parada  
  -         return 1  
  -     return fib(n \- 1\) \+ fib(n \- 2\)  
      
  - fatorial  
  - def factorial\_function(n):  
  -     if n \< 0:  
  -         return None  
  -     if n \< 2:  
  -         return 1  
  -     return n \* factorial\_function(n \- 1\)  
    \! ERRADO (sem condição de parada)  
  - def factorial(n):  
  -     return n \* factorial(n \- 1\)  
  -   
  - print(factorial(4))  
    


- ##### **método**

  - pertence a um dado, pode mudar o estado de uma entidade  
  - res \= dado.método(arg)

#### **LISTA (array)**

- coleção ordenada e mutável, permite duplicados, pode guardar vários tipos de dados juntos  
- cada elemento é um escalar  
- o nome da lista é o nome do local da memória onde a lista é armazenada  
  - lista2 \= lista1 – copia o nome da matriz (apontam para o mesmo lugar na memória, se modifica um modifica outro também)  
  - fatia – copia o conteúdo da lista  
- **string é imutável** (não dá para passar um valor da lista como string e querer alterar)  
  - transforma palavra (da lista) em nova lista (de caracteres)

- ###### *adicionar **item – fim ou posição específica***

```
  new.append(words\[i\])  
  https://www.amazon.com.br/s?k=moldura+quadro&\_\_mk\_pt\_BR=%C3%85M%C3%85%C5%BD%C3%95%C3%91\&ref=nb\_sb\_noss  
  nums\[len(nums):\] \= \[5\] \#criar nova lista com o '5' e junta com a existente (no fim)  
    
  new \= get\_int(“valor: ”)  
  lista \+= \[new\]  
    
  compras \= \["a", "b", "c"\]  
  \#print({compras}) \- assim não pode  
  print(f"inicial: {compras}")  
  print(f"1o item: {compras\[0\]}")  
  print(f"último item: {compras\[\-1\]}")  
  print(f"penúltimo item: {compras\[\-2\]}")  
    
  \#Adicionar   
  compras.insert(posição, "d")  
  \#Adicionar no final  
  compras.append("d")  
  print(f"nova compras: {compras}")  
    
  \#Remover um item  
  compras.remove("c")  
  del compras\[1\]  
  print(f"compras sem 'c': {compras}")  
    
  \#Tamanho da compras  
  print({len(compras)})
```

  - ###### ***lista \+ for (list comprehension)***

  nums \= \[i for i in range(100)\]

- ###### ***inverter** a lista*

  tam \= len(lista)  
  for i in range(tam // 2):  
      lista\[i\], lista\[tam – i \- 1\] \= lista\[tam – i \- 1\], lista\[i\]  
  print(lista)

  - ###### ***slice – manipular** parte de lista* 

  - ponto de corte: 0 (antes do 1o elemento), 1 (antes do 2o elemento)  
  - elementos que sobraram entre os 2 pontos de corte  
  - **start**: index do 1o elemento incluso na fatia  
  - **end**: index do 1o elemento não incluso na fatia  
  - tamanho da fatia (quantidade de elementos) \= end – start (3 – 1 \= 2\)  
  - se start for maior que end, a lista sai vazia

  list\_2 \= list\_1\[:\] → list\_1\[start:end\] – padrão \[0:end-1\]


  my\_list \= \[10, 8, 6, 4, 2\]

  new\_list \= my\_list\[1:3\] – pontos de corte

  \# new\_list \= \[8, 6\]

  ![][image4]

- **del** – deletar elementos ou fatias  
  my\_list \= \[10, 8, 6, 4, 2\]  
  del my\_list\[1:3\]  
  \# my\_list \= \[10, 4, 2\]  
    
  \# deleta tudo \- lista vazia  
  my\_list \= \[10, 8, 6, 4, 2\]  
  del my\_list\[:\]  
  \# my\_list \= \[\]  
    
  \# deleta a lista em si  
  my\_list \= \[10, 8, 6, 4, 2\]  
  del my\_list  
  print(my\_list)

- ###### ***identificador (copia aponta para o mesmo local)***

```
  def my\_function(my\_list\_1):  
      print("Print \#1:", my\_list\_1)  
      print("Print \#2:", my\_list\_2)  
      del my\_list\_1\[0\]  \# Pay attention to this line.  
      print("Print \#3:", my\_list\_1)  
      print("Print \#4:", my\_list\_2)  
    
    
  my\_list\_2 \= \[2, 3\]  
  my\_function(my\_list\_2)  
  print("Print \#5:", my\_list\_2)
```  
  \# SAÍDA  
  \# Print \#1: \[2, 3\] Print \#2: \[2, 3\] Print \#3: \[3\] Print \#4: \[3\] Print \#5: \[3\]  
  


  - ###### ***string para lista***

  string\_para\_lista \= list(string\_original)

- ###### ***lista para string***

  lista\_para\_string \= "".join(string\_para\_lista)  
  nome.split("caractere como referência para cortar")  
  \# ex: (",")

- ###### ***lista para conjunto***

  conjunto\_num \= set(lista\_num)

- ###### ***lista para lista de conjuntos***

  numeros \= \[1, 8, 5, 1, 6, 15\]  
    
  set\_numeros \= \[\]  
  for item in numeros:  
      set\_numeros.append(set(\[item\]))  
  print(set\_numeros)

- ###### ***várias listas para uma tupla***

  nomes \= \["Arroz", "Feijão", "Carne"\]  
  precos \= \[5.50, 8.00, 25.00\]  
    
  for nome, preco in zip(nomes, precos):  
      print(f"- Produto: {nome}, Preço: R$ {preco:.2f}")

- ###### ***lista de tuplas \+ pesquisa***

  presidents \= \[  
      ("George Washington", 1789), \# 1 tupla  
      ("John Adams", 1797),  
      ("Thomas Jefferson", 1801),  
      ("James Madison", 1809)  
  \]  
    
  \# imprimir / pesquisar  
  for prez, year in presidents: \#ordem é definida aqui  
      print("In {1}, {0} took office".format(prez, year))  
      \#        year  prez

- converter todos os valores para float  
  notas \= \[float(nota) for nota in notas\_str\]

- ###### *adicionar **conjunto no fim da lista***

  new.append({words\[i\]})

- ###### ***lista de sets** (conjuntos) – manipulação*

  \# lambda s: ... \-\> Para cada set 's' na lista...  
  \# next(iter(s)) \-\> ...pegue o primeiro (e único) item de dentro do set...  
  \# len(...) \-\> ... calcule o tamanho deste item  
  print(f"\\n\\nmaior palíndromo: {max(palindromos, key\=lambda s: len(next(iter(s))))}")

- ###### ***lista de dicionários***

  people \= \[  
      {"name": "a", "number": "1"},  
      {"name": "b", "number": "2"},  
      {"name": "c", "number": "3"},  
  \]

- ###### ***in \+ not in**: verificar se existe valor*

  n \= input("name: ")  
  for person in people:  
      if person\["name"\] \== n:  
          print(f"found {person\["number"\]}")  
          break  
  else:  
      print("not found")  
    
  \# lista  
  print(“ana” in person)  
  print(“anaaa” not in person)  
    
  \# se achou o valor (true/false)  
```
  my\_list \= \[1, 2, 3, 4, 5, 6, 7, 8, 9, 10\]  
  to\_find \= 5  
  found \= False  
    
  for i in range(len(my\_list)):  
      found \= my\_list\[i\] \== to\_find  
      if found:  
          break  
    
  if found:  
      print("Element found at index", i)  
  else:  
      print("absent")
```  
    
  \# valores em comum em 2 listas  
  drawn \= \[5, 11, 9, 42, 3, 49\]  
  bets \= \[3, 7, 11, 42, 34, 49\]  
  hits \= 0  
    
  for number in bets:  
      if number in drawn:  
          hits \+= 1  
  print(hits)  
    
  \# lista sem valores repetidos  
  my\_list \= \[1, 2, 4, 4, 1, 4, 2, 6, 2, 9\]  
  new \= \[\]  
    
  for n in my\_list:  
      if n not in new:  
          new.append(n)  
    
  print("The list with unique elements only:")  
  print(new)


- ###### ***remover duplicados:** lista \-\> conjunto \-\> lista*

  lista\_num \= \[1, 2, 2, 3, 4, 4, 4, 5, 1, 6\]  
    
  conjunto\_num \= set(lista\_num)  
  lista\_num\_unicos \= list(conjunto\_num)

- ###### ***ordenar \+ inverter** os itens da lista → nova lista (sort \+ sorted)*

  - default: ordem alfabética / crescente

  people \= \["Ana", "Carlos", "Beatriz", "Daniel"\]

  ordenados \= sorted(people) \#nova lista ordenada, em ordem alfabética

  people.sort() \#ordena (altera) a lista original, em ordem alfabética

  print(f"Original: {people}")

  print(f"Ordenada (nova lista): {ordenados}")

  inverso \= reverse(people) \# inverte a ordem dos valores


  \# pelo comprimento do nome (len)

  por\_tamanho \= sorted(people, key\=len)

  print(f"Ordenado por tamanho: {por\_tamanho}")

- ###### *se a **lista está vazia***

  if not lista:  
          return None

- verificar se é **palíndromo**

- ###### ***se item está na lista** (sem for)*

  \#Verificar se é palindromo (igual de tras pra frente)  
  txt \= input("palavra: ").lower().replace(" ", "")  
    
  \#inverter string: \[::-1\]  
  if txt \== txt\[::\-1\]:  
      print(f"{txt} é palindromo")  
  else:  
      print(f"{txt} não é palindromo")  
    
    
  \#Verificar se existe na lista  
  hoteis \= \["rouxinol", "vila germanica", "schefer", "kirst"\]  
  item \= input(f"a procurar: ")  
    
  if item in hoteis: \#melhor que for  
      print(f"{item} está na lista")  
  else:  
      print(f"{item} não está na lista")

- ###### ***palíndromo \+ maior elemento de lista*** 

- otimizado  
```
  def so\_palindromos(words):  
      new \= \[\]  
      for item in words:  
          if (item \== item\[::\-1\]):  
              new.append(item)  
      return new  
    
    
  words \= \["arara", "level", "madam", "python", "racecar", "hello"\]  
  print(f"original: {words}")  
    
  palindromos \= so\_palindromos(words)  
  print(f"palíndromos: {palindromos}")  
    
  print(f"\\n\\nmaior palíndromo: {max(palindromos)}")
```  
    
- manual  
  def inverte(original, n):  
      \#string para lista \-\> manipulação  
      list\_pal \= list(original)  
    
      for i in range(n//2): \#itera ate a metade da palavra  
          \# a, b \= b, a \--\> troca valores sem aux  
          list\_pal\[i\], list\_pal\[n\-1\-i\] \= list\_pal\[n\-1\-i\], list\_pal\[i\]  
    
    
      \#lista para string de volta, fora do laço  
      pal\_inversa \= "".join(list\_pal)  
    
      return original \== pal\_inversa \#retorna True ou False  
    
    
  def verificar(words):  
      new \= \[\] \#nova lista vazia  
    
    
      for palavra in words: \# para cada palavra da lista original  
          if(inverte(palavra, len(palavra))): \# verifica se eh igual de trás pra frente  
              \# new.append({words\[i\]}) \#adiciona conjunto  
              new.append(palavra) \#adiciona item  
    
      return new \#retorna nova lista só com os palíndromos  
    
    
```
  def maior(pal):  
      \#verificar se a lista está vazia  
      if not pal:  
          return None  
    
    
      maior\_pal \= pal\[0\] \#ok  
    
    
      for item in pal:  
          if len(item) \> len(maior\_pal):  
              maior\_pal \= item  
          print(f"\\nlen maior palavra \- {len(maior\_pal)} \- {maior\_pal}")  
    
      return maior\_pal
```  
    
    
  words \= \["arara", "level", "madam", "python", "racecar", "hello"\]  
  print(f"original: {words}")  
    
    
  palindromos \= verificar(words) \#nova lista so com palindromos  
  print(f"\\n\\nso com palindromos: {palindromos}")  
    
    
  print(f"\\n\\nmaior palindromo: {maior(palindromos)}")  
  \# print(f"\\n\\nmaior palíndromo: {max(palindromos, key=len)}")


##### **Matriz (array bi-dimensional)**

t \= \[\[3\-i for i in range (3)\] for j in range (3)\] \# t \= \[\[3, 2, 1\], \[3, 2, 1\], \[3, 2, 1\]\]

s \= 0  
for i in range(3):  
    s \+= t\[i\]\[i\] \#3 \+ 2 \+ 1 \= 6  
print(s)

**Xadrez**  
![][image5]  
```
board \= \[\]  
for i in range(8):  
    row \= \[EMPTY for i in range(8)\]  
    board.append(row)  
    \# cria uma lista 8x8 preenchida com EMPTY (campo vazio)  
\# JEITO MAIS SIMPLES  
board \= \[\[EMPTY for i in range(8)\] for j in range(8)\]  
\# mudar valor dos campos  
board\[7\]\[7\] \= ROOK  
board\[4\]\[2\] \= KNIGHT  
board\[3\]\[4\] \= PAWN
```

**Temperaturas do mês**  
temps \= \[\[0.0 for h in range(24)\] for d in range(31)\]  
\#       |-----------------------| cria uma lista (linha) com 24 colunas (horas) \-- \[0.0, 0.0, ..., 0.0\]  
\#                                 |------------------| pega o resultado da linha e repete por 31 linhas  
\# acessar: temps\[dia\]\[hora\]  \# dia 0-30, hora 0-23

- temperatura média do mês ao meio dia  
```
  total \= 0.0  
  hot\_days \= 0  
    
  for day in temps: \#lê cada uma das 31 linhas (dias) \- day \= lista de 24h  
      total \+= day\[11\] \#soma a temperatura das 12h (índice 11\) ao total  
      if day\[11\] \> 20.0: \#soma a temperatura das 12h (índice 11\) ao total  
          hot\_days \+= 1   
    
  average \= total / 31 \#faz a média  
    
  print("Average temperature at noon:", average)  
  print(hot\_days, "days were hot")
```  
    
- temperatura mais alta do mês  
  highest \= \-100.0  
     
```
  for day in temps: \#day \= linhas  
      for temp in day: \#temp \= colunas  
          if temp \> highest:  
              highest \= temp
```


##### **Matriz tri-dimensional**

Hotel: 3 prédios, 15 andares cada e 20 quartos em cada andar  
```
rooms \= \[\[\[False for r in range(20)\] for f in range(15)\] for t in range(3)\]  
\#         |------------------------| lista (linha) de 20 quartos, vazios  
\#                                   |-------------------| lista (coluna) de 15 andares  
\#                                                        |--------------| lista (profundidade) de 3 prédios  
\# rooms\[t\]\[f\]\[r\] indicates whether room r on floor f of tower t is occupied (True) or not (False)
```

- ver quantas vagas tem no 15o andar do prédio 3  
  vacancy \= 0  
    
```
  for room\_number in range(20):  
      if not rooms\[2\]\[14\]\[room\_number\]:  
          vacancy \+= 1
```

#### **Conjuntos – set**

- coleção não ordenada e mutável que não permite duplicados  
- otimizado para operações (união, interseção) e verificar existência de itens  
  \#Conjunto a partir de lista com duplicados  
```
  lista\_num \= \[1, 5, 2, 5, 4, 7, 3, 1\]  
  conjunto\_num \= set(lista\_num)  
  \#se aqui converter de volta para lista, vai ter a lista inicial sem elementos duplicados  
  \#   lista\_nova \= list(conjunto\_num)  
    
  print(f"lista original: {lista\_num}")  
  print(f"conjunto: {conjunto\_num}") \#saída: {1, 2, 3, 4, 5, 7}
```

- ###### *verificar **existência de item** no conjunto*

  print(f"\\n o número 5 existe? {5 in conjunto\_num}") \#saída: o número 5 existe? True / False

- ###### ***operações** – união, interseção, diferença*

```
  a \= {1, 2, 3, 4}  
  b \= {3, 4, 5, 6}  
  print(f"\\nUnião A | B \- {a | b}") \#saída: {1, 2, 3, 4, 5, 6}  
  print(f"\\nInterseção A & B \- {a & b}") \#saída: {3, 4}  
  print(f"\\nDiferença A \- B \- {a \- b}") \#saída: {1, 2}
```


#### **Tupla**

- coleção ordenada e imutável, mais rápidas, pode guardar vários tipos de dados juntos  
- mesma manipulação de listas \[:\]  
- tupla \= (valor, valor, valor) OU tupla \= valor, valor, valor  
  pontos \= (10, 6, \-9, "a")  
  print(f"coord: {pontos}")  
    
- tupla com 1 valor: termina com vírgula  
  tupla\_1\_valor \= (10, ) \# OU tupla\_1\_valor \= 10, 

- valores podem circular  
  var \= 123  
     
  t1 \= (1, )  
  t2 \= (2, )  
  t3 \= (3, var)  
     
  t1, t2, t3 \= t2, t3, t1  
  \# t1 \= 2,  
  \# t2 \= 3, var  
  \# t3 \= 1,

- ###### *desempacotar tupla para variáveis*

  tup \= 1, 2, 3  
  a, b, c \= tup

- ###### *quantas vezes um valor aparece na tupla* 

```
  tup \= 1, 2, 3, 2, 4, 5, 6, 2, 7, 2, 8, 9  
  duplicates \= tup.count(2) \#quantas vezes o valor 2 aparece na tupla  
  print(duplicates)    \# outputs: 4
```


  
**Funções**

- len – número de elementos da tupla  
- del – deleta a tupla  
- \+ – junta tuplas  
- \* – multiplica tuplas (não multiplica os valores, replica a tupla X vezes)  
  tupla1 \= (1, 10, 100)   
  tupla2 \= tupla1 \* 3  
   \# tupla2 \= (1, 10, 100, 1, 10, 100, 1, 10, 100\)  
- in, not in – verificar elementos, como em listas

- ###### ***tuple()** – converte iterável para tupla*

  my\_list \= \[2, 4, 6\]  
  tup \= tuple(my\_list)

#### **Objeto**

- tipo struct em C  
  - class Objeto \+ construtor

```
class Student():  
    \#construtor  
    def \_\_init\_\_(self, name, id):  
        self.name \= name  
        self.id \= id

    def changeID(self, id):  
        self.id \= id

    def print(self):  
        print("{} \- {}".format(self.name, self.id))
```

- tem métodos – funções do objeto  
  - não passa objeto para a função, e sim chama o método do objeto  
  - 1 o parâmetro: self  
  - object.method()  
  - \#criar objeto da classe  
  - jane \= Student("Jane", 10)  
  - jane.print()  
  - jane.changeID(11)  
  - jane.print()

#### **Dicionário – hash table**

- ordem aleatória (até python 3.6)  
- {“key”: “value”,}, pode guardar vários tipos de dados juntos  
- key – palavra que pesquisa \= chave (única), case sensitive  
- valor – palavra que recebe  
- coleção não ordenada e mutável de pares *chave: valor*, super rápidas a partir da chave  
- ordenado por inserção, não é uma sequência  
- acessar, adicionar, alterar  
   \# hanging indent  
```
  pessoa \= {  
      "nome": "ana", \# key: nome, value: ana  
      "idade": 20,  
      "hobbies": \["ler", "viajar"\]  
  }  
  print(f"dados: {pessoa}")
```

- ###### ***iterar** sobre as chaves \+ **verificar** se existe*

```
  dictionary \= {"cat": "chat", "dog": "chien", "horse": "cheval"}  
  words \= \['cat', 'lion', 'horse'\]  
    
    
  for word in words:  
      if word in dictionary:  
          print(word, "-\>", dictionary\[word\])  
      else:  
          print(word, "is not in dictionary")  
    
   \# SAÍDA  
   \# cat \-\> chat  
   \# lion is not in dictionary  
   \# horse \-\> cheval
```       

- ###### ***imprimir** os dados*

```
  colors \= {  
      "white": (255, 255, 255),  
      "grey": (128, 128, 128),  
      "red": (255, 0, 0),  
      "green": (0, 128, 0)  
      }  
    
  for col, rgb in colors.items():  
      print(col, ":", rgb)
```

- ###### *método **keys**()*

  - retorna um objeto iterável com todas as chaves do dicionário

```
  dictionary \= {"cat": "chat", "dog": "chien", "horse": "cheval"}


  for key in dictionary.keys():

      print(key, "-\>", dictionary\[key\])


  \# SAÍDA:

  \# cat \-\> chat

  \# dog \-\> chien

  \# horse \-\> cheval
```

- ###### *método **items**()*

  - retorna tuplas, cada uma é um par key-value

```
  dictionary \= {"cat": "chat", "dog": "chien", "horse": "cheval"}


  for english, french in dictionary.items():

      print(english, "-\>", french)


  \# SAÍDA:

  \# cat \-\> chat

  \# dog \-\> chien

  \# horse \-\> cheval
```

- ###### *método **values**()*

  - retorna valores, dicionário não encontra a chave de um valor automaticamente (limitado)

```
  dictionary \= {"cat": "chat", "dog": "chien", "horse": "cheval"}


  for french in dictionary.values():

      print(french)


  \# SAÍDA:

  \# cat \-\> chat

  \# dog \-\> chien

  \# horse \-\> cheval
```

- ###### ***acessar** os dados pela chave \+ método **get**()*

  - acessar os dados

  \# acessar valor pela chave

  print(f"hobbies de {pessoa\['nome'\]}: {pessoa\['hobbies'\]}")

  if pessoa\["idade"\] \< 20:

      \#...


  \# GET

  pol\_eng\_dictionary \= {

      "kwiat": "flower",

      "woda": "water",

      "gleba": "soil"

      }


  item\_1 \= pol\_eng\_dictionary\["gleba"\] \# soil

  item\_2 \= pol\_eng\_dictionary.get("woda") \# water

- ###### ***alterar** valor existente \+ método **update()***

- ###### *juntar 2 dicionários em um novo*

```
  \# alterar  
  pessoa\["nome"\] \= "Ana"  
    
  \# update  
  pessoa.update({"nome": "amanda"})  
  \# OU SIMPLESMENTE  
  pessoa\[chave\] \= valor  
    
  \# juntar 2 dicionários em um novo  
  d1 \= {'Adam Smith': 'A', 'Judy Paxton': 'B+'}  
  d2 \= {'Mary Louis': 'A', 'Patrick White': 'C'}  
  d3 \= {}  
    
  for item in (d1, d2): \#itera uma vez em d1 e outra em d2  
      \#pega os valores de chave-valor do dicionário item e atualiza/sobrescreve o dicionário d3  
      d3.update(item)  
    
  print(d3)
```

- ######  *método **copy()***

  dictionary \= {"cat": "chat", "dog": "chien", "horse": "cheval"}  
  copy\_dict \= dictionary.copy()

- ###### ***remover** uma chave/item \+ método **popitem()** \+ método **clear()***

  dictionary \= {"cat": "chat", "dog": "chien", "horse": "cheval"}  
    
  del dictionary\['dog'\] \# remover item específico  
  \# remover último item  
  dictionary.popitem() \# antes do python 3.6.7, popitem() remove um item aleatório  
  \#remover todos os itens  
  dictionary.clear()  
  \#remover o dicionário  
  del dictionary

- ###### *dicionário para lista*

  - não garante a mesma ordem

  for person in people:

      print(person)


  for dado, valor in people.items(): \# dicionário para lista

      print(valor)


  \# imprimir valores

  for dado, valor in people.items():

      print("a person {} is {}".format(dado, valor))

- ###### *tupla para dicionário \+ método **dict()***

  colors \= (("green", "\#008000"), ("blue", "\#0000FF"))  
    
  colors\_dictionary \= dict(colors)

- ###### ***adicionar** novo dado*

  pessoa\["cidade"\] \= "Santa Maria"  
  pessoa.update({"estado": "RS", "pais": "Brasil"})


- ###### ***dicionário de dicionários** (key: value) \+ pesquisa*

  \#key \= name, value \= number  
  people \= {  
      "aaa": "1",  
      "bbb": "2",  
      "ccc": "3",  
  }  
    
  name \= input("name: ")  
  if name in people:  
      print(f"number: {people\[name\]}")  
  else:  
      print("not found")

- ###### *função **sorted**() \+ **len**()*

  - sorted(dicionário, chave para ordenar)

```
   with open("phonebook.csv", "r") as file:

      \# para acessar pelo nome do campo

      reader \= csv.DictReader(file)

      counts \= {}


      for row in reader:

              \# if "joao" in row\["name"\]:

              \#       joao \+= 1

              \# print(row\["name"\])


          if row\["name"\] in counts: \# se esse nome ja existe no dicionario

              counts\[row\["name"\]\] \+= 1 \#usa nome como key no dicionário de contagem

          else:

              counts\[row\["name"\]\] \= 1 \#indexa nome no dicionario e inicializa como 1


   \# ORDENAR DICIONARIO

  sorted\_counts \= dict(sorted(counts.items()))


    for fav in sorted(counts, key\=counts.get): \#pega o valor do dicionario 'counts' em si e usa como chave para ordenar

          print(f"{fav}: {counts\[fav\]}")


        SAÍDA \- ordem crescente de nome que mais aparece

    diego: 1

    elisa: 1

    joao lucas: 1

    joao pedro: 2

    ana clara: 5

    gustavo: 5

    lucas: 6

    maria: 7

    joao: 9

    for fav in sorted(counts, key\=counts.get, reverse\=True): \#pega o valor do dicionario 'counts' em si e usa como chave para ordenar \-\> inverte ordenação (default: False)  
        print(f"{fav}: {counts\[fav\]}")

    SAÍDA \- ordem DEcrescente de nome que mais aparece – mais comuns 1o  
joao: 9  
maria: 7  
lucas: 6  
gustavo: 5  
ana clara: 5  
joao pedro: 2  
joao lucas: 1  
elisa: 1  
diego: 1
```

- len – retorna quantidade de chave-valor


#### **tupla \+ dicionário**

problema:

- calcular a pontuação média dos alunos  
- recebe: nome (inseridos em qualquer ordem), pontuação única  
- entrada termina quando recebe um nome vazio  
- exibe uma lista com todos os nomes \+ pontuação média

```
school\_class \= {} \#cria dicionário vazio  
\#notas vão ser armazenadas em tuplas (values do dicionário)

while True:  
    name \= input("Enter the student's name: ") \#keys  
    if name \== '':  
        break  
     
    score \= int(input("Enter the student's score (0-10): "))  
    if score not in range(0, 11):  
        break  
     
    \#se o nome já existir, adiciona a nova nota à tupla existente  
    if name in school\_class:  
        school\_class\[name\] \+= (score,)  
    else: \#novo estudante, cria nova tupla com a nota  
        school\_class\[name\] \= (score,)  
         
\#itera sobre cada estudante (ordenado)  
for name in sorted(school\_class.keys()):  
    adding \= 0  
    counter \= 0  
    for score in school\_class\[name\]: \#soma todas as notas  
        adding \+= score  
        counter \+= 1  
    \#imprime aluno: média  
    print(name, ":", adding / counter)
```

#### **try / except**

- não termina a execução, só pula para except (evita que o programa termine)  
- try: fazer algo ser pedir permissão, trecho que pode dar errado (se der certo, não executa o except)  
- except: implorar por perdão se der errado, limpar a bagunça

\# pede dados  
nome \= input("nome: ")  
ano\_str \= input("ano: ")

try:  
    \#converter string ano para inteiro  
    ano\_int \= int(ano\_str)

    \#ex: calcula idade  
    idade \= 2025 \- ano\_int

    print(f"ola {nome} voce tem {idade} anos")

except ValueError:  
    \#se int() falhar  
    print("Erro\! O que faço agora?")

try:  
    value \= int(input('Enter a natural number: '))  
    print('The reciprocal of', value, 'is', 1/value)          
except ValueError:  
    print('I do not know what to do.')      
except ZeroDivisionError:  
    print('Division by zero is not allowed in our Universe.')     
except: \# default  
    print('Something strange has happened here... Sorry\!')

 \# pedindo até usuário digitar certo  
while True:  
    try:  
        value \= int(input('Enter a integer number: '))  
        print(number/2)     
        break     
    except: \# default / último  
        print('The value is not an int\! Try again')

###### ***exceções***

- try / else / finally  
  - 63 exceções embutidas   
    - \+ perto da raiz (BaseException) \= \+ genérica   
    - folha \= específica  
    - 1o as específicas, depois as genéricas

```
    def print\_exception\_tree*(thisclass, nest \= 0)*:

        if nest \> 1:

            print("   |" \* (nest \- 1), end\="")

        if nest \> 0:

            print("   \+---", end\="")

    

        print(thisclass.\_\_name\_\_)

    

        for subclass in thisclass.\_\_subclasses\_\_():

            print\_exception\_tree(subclass, nest \+ 1)

    

    

    print\_exception\_tree(BaseException)
```

  - são objetos/classes  
  - termina o programa quando algo dá errado / não sabe o que fazer (em vez de retornar um valor) – se a exceção for tratada na hora (try), o programa pode ser retomado  
  - usar try … except só em trechos peq	uenos que podem dar erro (não no programa inteiro)  
  - pode tentar (try catch) chamar/executar uma função (se der erro na função executa o catch)  
  - **descrever** o erro

  try:

      i \= int("Hello\!")

   \# captura a instância do erro em um “pacote” (objeto) com a propriedade ***args*** com infos do erro

   \# trata o erro usando dados específicos

  **except Exception as e**:

      print(e) \#invalid literal for int() with base 10: 'Hello\!'

      print(e.\_\_str\_\_()) \#invalid literal for int() with base 10: 'Hello\!'

      \# mensagem seria mostrada se não tivesse o except

- **`args`** (tupla) – propriedade da classe BaseException, todos os argumentos passados ao construtor (não conta o *self*)

###### ***try / else***

- try, se não deu erro executa o else (depois do último except)  
  - try:  
  -     n \= int(input("number: "))  
  - except ValueError:  
  -     print("is not a number")  
  - **else**: \#não deu erro  
  -     print("is a number")

        

###### ***try / finally***

- sempre executa  
- pode coexistir com else

```
def *reciprocal*(n):  
    *try*:  
        n \= 1 / n  
    *except* ZeroDivisionError:  
        print("Division failed")  
        n \= None  
    *else*:  
        print("Everything went fine")  
    *finally*:  
        print("It's time to say goodbye")  
        *return* n

print(reciprocal(2))  
print(reciprocal(0))
```

*\# Everything went fine*  
*\# It's time to say goodbye*  
*\# 0.5*  
*\# Division failed*  
*\# It's time to say goodbye*  
*\# None*  
![][image6]

- se mudar para exceção acima da hierarquia continua a mensagem


- se tiver específica e genérica, imprime a que vem 1o  
- **`raise`** `exec` – simula/executa uma exceção real especificada (sem precisar inserir valores), trata parcialmente e delega o tratamento  
  -   
```
    def bad\_fun(n):  
        raise ZeroDivisionError  
      
    try:  
        bad\_fun(0)  
    except ArithmeticError:  
        print("What happened? An error?")  
      
    print("THE END.")
```  
- **`raise`** (sem nome) – só pode ser usada dentro do bloco *except*, relança a mesma exceção que está sendo tratada (distribuir tratamento de exceções entre partes do código)

```
  def bad\_fun(n):

      try:

          return n / 0

      except:

          print("I did it again\!")

          raise


  try:

      bad\_fun(0)

  except ArithmeticError:

      print("I see\!")


  print("THE END.")
```


  \#saída

  \# I did it again\!

  \# I see\!

  \# THE END.

- se a parte com erro não for chamada, não acusa nada  
- executadas na ordem que aparecem  
- [https://docs.python.org/3.6/library/exceptions.html](https://docs.python.org/3.6/library/exceptions.html) 

**`BaseException`** – mais genérica/abstrata, todas outras são filhas dela (`except` \== `BaseException`)

BaseException / **`KeyboardInterrupt`** – usuário força o término do programa (ctrl \+ c), não é derivada da classe `Exception`

BaseException / **`SyntaxError`** – viola a gramática do python (interpretada, checa enquanto roda) — não usar exceção para erros de sintaxe (deve evitar), não ocorre no try-except e sim antes de rodar o código  
try:  
    \# Falta de dois pontos (:) no final do 'if'  
    if 1 \== 1  
        print("Isso nunca rodará.")  
except SyntaxError: \#nem chega aqui  
    print("Um SyntaxError não pode ser tratado, ele impede a execução.")

BaseException / Exception / **`AssertionError`** – exceção concreta com argumento/valor inserido é inválido (False, None, 0, string vazia)

- **`assert`** `expression3` – protege o código de dar resultados inválidos (ex: função usada pelo usuário) e mostra a falha (não substitui exceção nem valida os dados)  
  - avalia a expressão  
  - se for um valor diferente de *None*, não faz nada  
  - se for *None*, lança AssertionError

  import math


  x \= float(input("Enter a number: "))

  assert x \>= 0.0

  assert x % 180 \!= 90


  print(math.sqrt(x))

  \#AssertionError  

BaseException / Exception / **`ValueError`** – função (int ou float) recebe um argumento de um tipo válido, com valor inválido

BaseException / Exception / **`TypeError`** – pegar um dado de um tipo inválido no contexto; ex: index\[0.5\], len(int)

BaseException / Exception / **`ArithmeticError`** – exceção abstrata de operações aritméticas

BaseException / Exception / **`AttributeError`** – acessar um atributo/método que não existe; ex: lista.depend(3), lista.len()

BaseException / Exception / ArithmeticError / **`ZeroDivisionError`** – operadores (/, //, %), tentativa de divisão por 0

BaseException / Exception / ArithmeticError / **`OverflowError`** – operação produz um número (resultado, cálculo) muito grande para ser armazenado na memória do tipo de dado  
from math import exp

ex \= 1

try:  
    while True:  
        print(exp(ex))  
        ex \*= 2  
except OverflowError:  
    print('The number is too big.')

BaseException / Exception / **`MemoryError`** – operação não pode ser completada (criar coisa) por falta de memória livre (tentou alocar mais RAM do que tem)  
string \= 'x'  
try:  
    while True:  
        string \= string \+ string  
        print(len(string))  
except MemoryError:  
    print('This is not funny\!')

BaseException / Exception / **`LookupError`** – abstrata, inclui todas exceções causadas por referências inválidas a coleções (listas, conjuntos, …)

BaseException / Exception / LookupError / **`IndexError`** – além da borda/limite (tenta acessar elemento que não existe)  
the\_list \= \[1, 2, 3, 4, 5\]  
ix \= 0  
do\_it \= True  
   
while do\_it:  
    try:  
        print(the\_list\[ix\])  
        ix \+= 1  
    except IndexError:  
        do\_it \= False  
   
print('Done')

BaseException / Exception / LookupError / **`KeyError`** – tenta acessar elemento que não existe em uma coleção (ex: dicionário)  
dictionary \= {'a': 'b', 'b': 'c', 'c': 'd'}  
ch \= 'a'

try:  
    while True:  
        ch \= dictionary\[ch\]  
        print(ch)  
except KeyError:  
    print('No such key:', ch)

BaseException / Exception / StandartError / **`ImportError`** – importação falha  
try:  
    import math  
    import time  
    import abracadabra:

except:  
    print('One of your imports has failed.') \#qual?

###### ***criar exceção***

\# geral  
```
class PizzaError(Exception):  
    \# objeto pizza \+ descrição do erro  
    def \_\_init\_\_*(self, pizza\='unknown', message\='')*:  
        Exception.\_\_init\_\_(self, message)  
        self.pizza \= pizza

class TooMuchCheeseError(PizzaError):  
    def \_\_init\_\_*(self, pizza\='unknown', cheese\='\>100', message\='')*:  
        PizzaError.\_init\_\_(self, pizza, message)  
        self.cheese \= cheese \# mais infos

def make\_pizza*(pizza, cheese)*:  
    if pizza not in \['margherita', 'capricciosa', 'calzone'\]:  
        \# raise PizzaError(pizza, "no such pizza on the menu")  
        raise PizzaError  
    if cheese \> 100:  
        \# raise TooMuchCheeseError(pizza, cheese, "too much cheese")  
        raise TooMuchCheeseError  
    print("pizza ready")

for (pizza, cheese) in \[('calzone', 0), ('margherita', 110), ('mafia', 20)\]:  
    try:  
        make\_pizza(pizza, cheese)
```  
    except TooMuchCheeseError as tmce:  
        print(tmce, ': ', tmce.cheese)  
    except PizzaError as pe:  
        print(pe, ': ', pe.pizza)

**Teste unitário**

- ao escrever uma função, também cria um conjunto de dados para os quais o comportamento do código seja previsível  
- qualquer alteração no código deve ser seguida da execução de todos os testes unitários \+ código fonte  
- módulo: unittest

**Debugger**

- pedaço de software que executa linha por linha, pode ver as mudanças de valor das variáveis, mudar os valores e parar a execução  
- print debugging: vários prints  
- falar para alguém, isolar o problema, analisar as mudanças, dar uma pausa  
- prints de exemplo: [https://www.cs.uky.edu/\~keen/help/debug-tutorial/debug.html](https://www.cs.uky.edu/~keen/help/debug-tutorial/debug.html)  
- documentação IDLE: [https://docs.python.org/3/library/idle.html](https://docs.python.org/3/library/idle.html)   
- rubber duck debugging: [https://en.wikipedia.org/wiki/Rubber\_duck\_debugging](https://en.wikipedia.org/wiki/Rubber_duck_debugging) 

#### **argumentos da linha de comando (sys)**

##### valores de saída (erro)

\# from sys import argv  
import sys

if len(sys.argv) \!= 2:  
    print("hello, world")  
    exit(1)

print(f"hello, {sys.argv\[1\]}")  
exit(0)

#### **arquivos de texto**

- python usa conjunto de objetos para acessar e processar arquivos  
- Linux é case sensitive  
- \\ é caractere de escape em python → usar \\\\  
- python não acessa os arquivos diretamente, e sim entidades/representações abstratas dos dados físicos (*handles* ou *streams*)

###### ***streams***

- objeto associado a um arquivo (funciona como um gravador: quando lê algo, uma cabeça virtual se move pelo stream de acordo com o número de bytes) transferidos do stream  
- quando escreve, a mesma cabeça se move pelo stream gravando os dados da memória   
  - *“current file position”*  
- *opening the file* – conectar o stream com o arquivo \+ maneira como o stream vai ser processado (*open mode*)  
- pode dar erro por falta de arquivo de nome específico ou se o programa não tem permissão de acesso  
- operações   
  - ler do stream – dados do arquivo para a memória, gerenciado pelo programa  
  - escrever para o stream – dados da memória transferidos ao arquivo  
- open modes  
  - *read* – apenas operações de leitura (operações inválidas causam *UnsupportedOperation, OSError e ValueError* – módulo *io*)  
  - *write* – apenas operações de escrita (operações inválidas causam *UnsupportedOperation etc*)  
  - update – permite escrita e leitura  
- tipos  
  - de texto   
  - *binários* – sequência de bytes de um valor (ex: programa executável, imagem, vídeo, database, etc), como não tem linhas, as operações de leitura/escrita se referem a porções de dados (byte a byte, bloco a bloco)  
    - *problema*: em sistemas Unix o fim de linha é `LF` (ASCII 10), ou `\n,` em outros (Windows) o fim de linha é `CR` e `LF` (ASCII 13 e 10), ou `\r\n –` (problema da não portabilidade)  
    - solução (nível de classe):   
1. quando o stream é aberto e os dados serão processados como texto (ou não avisa como) é mudado para modo texto  
2. enquanto tá lendo/escrevendo as linhas de/para o arquivo e o sistema é Windows, muda cada `\r\n` para `\n` (lendo) e vice versa (escrevendo) – *translation of newline characteres*  
3. é transparente ao programa, pode ser escrito como se fosse destinado a apenas Unix (código em Windows também funciona)  
4. quando o stream é aberto e avisado o que fazer, o conteúdo é pego como está (sem conversão)

**abrindo stream**  
stream \= open(file, mode \= 'r', encoding \= None) \# encoding: padrão de codificação de caracteres (utf-8, latin-1, etc)  
\# MODE: sequência de caracteres, cada um com um significado (default \= read in text mode)  
\# 'r' \= read (leitura), arquivo deve existir  
\# 'w' \= write (escrita), cria arquivo novo ou sobrescreve existente  
\# 'x' \= create (criar), cria arquivo novo, erro se já existir  
\# 'a' \= append (acrescentar), cria arquivo novo ou acrescenta ao final do existente  
\# 'r+' \= read and update, arquivo deve existir  
\# 'w+' \= write and update, cria arquivo novo ou acrescenta no existente  
\# '\_b' \= binary mode (modo binário), usado para arquivos não-texto (imagens, vídeos, etc)  
\# '\_t' \= text mode (modo texto), padrão, usado para arquivos de texto

**\# abrir em FOR com CLOSE implícito**  
from os import strerror

try:  
    ccnt \= lcnt \= 0  
    **for line in open('text.txt', 'rt'):**  
        lcnt \+= 1  
        for ch in line:  
            print(ch, end\='')  
            ccnt \+= 1  
    print("\\n\\nCharacters in file:", ccnt)  
    print("Lines in file:     ", lcnt)  
except IOError as e:  
    print("I/O error occurred: ", strerror(e.errno))

**abrindo stream pela 1a vez**  
try:  
    stream \= open("C:\\Users\\User\\Desktop\\file.txt", "rt") \# **objeto é uma instância de uma classe iterável** – método **\_\_next\_\_** retorna a próxima linha lida do arquivo  
    \# Processing goes here.  
    stream.close()  
except Exception as exc:  
    print("Cannot open the file:", exc)

**stream já abertos**

- quando o programa inicia, 3 streams já são abertos – módulo `sys`

import sys  
sys.stdin

- relacionado ao teclado, pré aberto para leitura, principal fonte de dados para programas em execução, função `input()`

sys.stdout

- relacionado à tela, pré aberto para escrita, alvo dos dados gerados (resultados) no programa em execução, função `print()`

sys.stderr  
sys.stderr.write("Error message")

- relacionado à tela, pré aberto para escrita, lugar onde o programa em execução manda informações de erros, função `print()`

**fechando stream**  
stream.close()

- nome.close(), sem argumentos, sem retorno (ou objeto *IOError*) – se um programa recebeu operações de escrita, pode acontecer de os dados enviados ao stream não terem sido transferidos ao dispositivo físico ainda (*caching* ou *buffering*) – fechar força a parada

**diagnosticando problemas de stream**

- IOError tem uma propriedade `errno` (*error number*) – comparar valor as constantes predefinidas do módulo

errno.EACCES \# permissão negada (ex: tentar escrever em um arquivo de leitura)  
errno.EBADF \# arquivo inválido (ex: usar um descritor de arquivo fechado)  
errno.EEXIST \# arquivo já existe (ex: tentar criar um arquivo que já existe)  
errno.EFBIG \# arquivo muito grande (ex: tentar criar um arquivo maior que o SO permite)  
errno.EISDIR \# é um diretório (ex: tentar escrever em um diretório como se fosse um arquivo)  
errno.EMFILE \# muitos arquivos abertos (ex: tentar abrir mais arquivos do que o limite do SO)  
errno.ENOENT \# arquivo ou diretório não encontrado (ex: tentar abrir um arquivo que não existe)  
errno.ENOSPC \# sem espaço em disco (ex: tentar escrever em um disco cheio)

from os import strerror

try:  
    s \= open("c:/users/user/Desktop/file.txt", "rt")  
    \# ...  
    s.close()  
except Exception as exc:  
    print("The file could not be opened: ", **strerror**(exc.errno))  
    \# **strerror**(number) \-- retorna uma string descrevendo o erro  
    \# if exc.errno \== errno.ENOENT:  
    \#     print("The file doesn't exist.")  
    \# elif exc.errno \== errno.EMFILE:  
    \#     print("You've opened too many files.")  
    \# else:  
    \#     print("The error number is:", exc.errno)

###### ***handles***

- python assume que todo arquivo está escondido atrás de um objeto de uma classe adequada – criado quando abre o arquivo e destrói ao fechar  
- objeto especifica quais operações devem ser realizadas em que ordem, pela forma como abre o arquivo  
- objeto vem de uma dessas classes  
  ![][image7]   
- não usa construtor, pega os objetos pela função *open()*   
- função analise os argumentos e cria o objeto  
- para fechar, chama método *close()* – interrompe a conexão do objeto e do arquivo e remove o objeto

###### ***ler arquivos – read()***

- read() – ler caracteres de arquivo e retornar como string (ou vazia)

from os import strerror

try:  
    c \= 0  
    stream \= open("C:\\\\Users\\\\Cliente\\\\Downloads\\\\a.txt", "rt")  
    \# char \= **stream.read(1)** \#tenta ler 1 caractere  
    \# while char \!= '':  
    content \= **stream.read()** \#tenta ler tudo  
    for char in content:  
        print(char, end\='')  
        c \+= 1  
        char \= stream.read(1)  
    stream.close()  
    print("\\n\\n characters: ", c)  
except IOError as exc:  
    print("I/O error: ", strerror(exc.errno))

###### ***ler linhas – readline/s()***

- tratar o conteúdo do arquivo como um conjunto de linhas   
- readline() – tenta ler uma linha completa de texto e retorna como uma string (ou vazia)  
- readlines(bytes) – tenta ler todo o conteúdo do arquivo e retorna uma lista de strings, pode convencer a ler apenas um número específico de bytes por vez (passa input máximo do buffer como argumento, opcional)

###### ***write()***

- argumento: string a ser transformada em um arquivo aberto → mode ‘w’ (criado do 0\)  
- não insere quebra de linha automática

##### **arquivos CSV**

- DictReader – para acessar pelo nome do campo (se mudar ordem dos dados não altera pesquisa), pula 1a linha (nome dos campos)

import csv

name \= input("name: ")  
number \= input("number: ")

\# file \= open("phonebook.csv", "a") \#append  
with open("phonebook.csv", "a") as file:  
    \#inserir no arquivo  
    \# writer \= csv.writer(file) \#abra esse arquivo e fique pronto para escrever algo

    \#escreve os dados como lista  
    \# writer.writerow(\[name, number\])

    \#escreve os dados como dicionarios  
    writer \= csv.DictWriter(file, fieldnames\=\["name", "number"\])  
    writer.writerow({"name": name, "number": number})

    \#fecha automaticamente

\# file.close() \#fecha

with open("phonebook.csv", "r") as file:  
    \# para acessar pelo nome do campo  
    reader \= csv.DictReader(file)  
    for row in reader:  
        print(row\["name"\])

#### **arquivos binários**

###### ***bitearray***

- classe especializada para guardar dados amorfos (sem formato específico \= bytes) – array de bytes amorfos, ex: gráficos bitmap  
- são mutáveis, aceitam a função *len()*, pode acessar elementos por index  
- não aceita valores não inteiros – TypeError  
- só aceita valores entre 0 e 255 (incluso) – ValueError  
- argumento `ord(‘a’)`: produz bytes de valores correspondentes a parte alfabética do ASCII

**como ler os bytes de um stream**

- método **`readinto()`** – não cria um novo objeto array de bytes, mas completa um já criado com os valores do arquivo binário  
  - retorna o número de bytes lidos  
  - tenta completar o espaço do argumento – se dados \> espaço interrompe a leitura, se não o resultado pode indicar que o array foi preenchido parcialmente 

data \= bytearray(10) \# 10 bytes '0'  
image \= bytearray(stream.read())

for i in range(len(data)):  
    data\[i\] \= 10 \- i

try:  
    bf \= open('files/file.bin', 'wb') \#'wb' \= write binary  
    bf.write(data)  
    bf.close()

    bf \= open('files/file.bin', 'rb') \#'rb' \= read binary  
    bf.readinto(data) \# le o conteudo para o byteaaray 'data'  
    bf.close()

    for b in data:  
        print(hex(b), end\=' ') \# 0xa 0x9 0x8 0x7 0x6 0x5 0x4 0x3 0x2 0x1  
except IOError as e:  
    print("I/O error occurred:", strerror(e.errno))

- ou método **`read()`** – tenta ler todo o conteúdo para a memória (parte de um novo objeto da classe *bytes* – imutável)  
- pode criar um bytearray e pegar o valor inicial diretor do objeto bytes – só se tiver certeza que o arquivo cabe na memória, ou delimita leitura (arg)

data \= bytearray(10) \# 10 bytes '0'

for i in range(len(data)):  
    data\[i\] \= 10 \- i

try:  
    bf \= open('files/file.bin', 'wb') \#'wb' \= write binary  
    bf.write(data)  
    bf.close()

    bf \= open('files/file.bin', 'rb') \#'rb' \= read binary  
    bf.readinto(data) \# le o conteudo para o byteaaray 'data'  
    bf.close()

    for b in data:  
        print(hex(b), end\=' ') \# 0xa 0x9 0x8 0x7 0x6 0x5 0x4 0x3 0x2 0x1  
except IOError as e:  
    print("I/O error occurred:", strerror(e.errno))

\# OU READ() \-- se tiver certeza que o arquivo cabe na memória, ou delimita bytes para ler (argumento)  
from os import strerror

try:  
    bf \= open('files/file.bin', 'rb')  
    data \= bytearray(bf.read(5)) \# 0xa 0x9 0x8 0x7 0x6  
    bf.close()

    for b in data:  
        print(hex(b), end\=' ')  
except IOError as e:  
    print("I/O error occurred:", strerror(e.errno))

**copiar arquivos**

- criar uma ferramenta tipo Windows *copy*

from os import strerror

srcname \= input("Enter the source file name: ")  
try:  
    src \= open(srcname, 'rb') \# leitura  
except IOError as e:  
    print("Cannot open the source file: ", strerror(e.errno))  
    exit(e.errno) \# termina execuçao com mensagem de codigo de erro

dstname \= input("Enter the destination file name: ")  
try:  
    dst \= open(dstname, 'wb')  
except Exception as e:  
    print("Cannot create the destination file: ", strerror(e.errno))  
    src.close()  
    exit(e.errno)  

\# area de transferencia \= BUFFER  
buffer \= bytearray(65536) \# prepara uma parte da memoria (64kb) para transferir os dados da origem para o destino  
\# maior \= mais rapido copiando e menos operações I/O

total  \= 0 \# contar bytes copiados  
try:  
    readin \= src.readinto(buffer) \# tenta encher o buffer pela 1a vez

    \# enquanto recebe um valor \> 0 de bytes, repete  
    while readin \> 0:  
        written \= dst.write(buffer\[:readin\]) \# escreve o conteudo do buffer no destino (bytes limitados)  
        total \+= written \# atualiza contador  
        readin \= src.readinto(buffer) \# le o proximo bloco do arquivo

except IOError as e:  
    print("Cannot create the destination file: ", strerror(e.errno))  
    exit(e.errno)    
     
print(total,'byte(s) succesfully written')  
src.close()  
dst.close()

##### **Módulo**

- tipo um container de funções  
- quando um módulo é importado (conteúdo executado pelo python) ele inicializa alguns aspectos internos  
- se importar o mesmo módulo \+\! vezes, python só inicializa 1 vez  
- user (usa) e supplier (cria), usa as entidades do módulo  
- cada módulo tem sua variável \_\_name\_\_  
- [https://docs.python.org/3/library/index.html](https://docs.python.org/3/library/index.html)  
- namespace: sistema que mapeia nomes para objetos, organiza e gerencia para que cada objeto tenha um nome único num escopo  
- são criados todos os dias para fins específicos (genética, psicologia, astronomia, …), todos: [https://docs.python.org/3/py-modindex.html](https://docs.python.org/3/py-modindex.html) 

import math, sys \#para acessar variáveis precisa usar "nome.variável"  
print(math.pi)  \#melhor jeito

\# OU (não recomendado)  
from math import \* \#acessa sem math. mas não é seguro (pode sobrescrever)

\# OU

from math import pi \#acessa o valor pi do módulo apenas por "pi"  
print(pi) \#não recomendado

pi \= 4  
print(pi) \#sobrescreve a variável pi

from math import pi  
print(pi) \#sobrescreve de novo

- mudar apelido de módulo (alias) – as

import math as m \#nome original fica inacessível  
print(m.pi)

 \# mudar nome específico para não conflitar com código ou facilitar  
from math import first as a, second as b, third as c, pi as PI

###### *m math*

trigonometria

- `sin(x), cos(x), tan(x)` – seno, cosseno, tangente de x  
- `asin(x), acos(x), atan(x)` – arco seno, arco cosseno, arco tangente de x  
- `pi` – constante de pi  
- `radians(x)` – converte de grau para radiano  
- `degrees(x)` – converte de radiano para grau 

hiperbólicos

- `sinh(x), cosh(x), tanh(x), asinh(x), acosh(x), atanh(x)` – hiperbólicos

exponenciação

- `e` – constante de número Euler  
- `exp(x)` – e^x  
- `log(x)` – logaritmo natural de x  
- `log(x, b)` – logaritmo de x em base b  
- `log10(x)` – logaritmo decimal de x \= log(x, 10\)  
- `log2(x)` – logaritmo binário de x \= log(x, 2\)  
- `pow(x, y)` – x^y

geral

- `ceil(x)` – arredonda para cima  
- `floor(x)` – arredonda para baixo  
- `trunc(x)` – parte inteira do número  
- `factorial(x)` – x\! (inteiro positivo)  
- `hypot(x)` – hipotenusa de um triângulo de catetos x e y \= `sqrt(pow(x, 2) + pow(y, 2))`

###### *m random*

- `random()` – float entre 0 e 1  
  - números pseudo aleatórios (algorítmos determinísticos)  
  - gerador pega um valor (seed) como input, usa um método e gera uma nova seed  
  - quando voltar para a seed inicial vai repetir tudo  
  - argumentar a seed como um número da hora atual (em python basta importar)


- `seed()`: default (hora) ou definir int como argumento (se definir int, sempre vai gerar igual)  
    
- `randrange(begin, end, step)` – valores inteiros “aleatórios”, pode usar 1-3 argumentos  
  - default(arg): fim  
  - `randrange(len(lista))` – sorteia índice de lista


- `rangeint(esq, dir)` – números inteiros, limite incluso \= randrange(left, right+1)  
    
- `choice(sequence)` – pega um elemento “aleatório” de uma lista e retorna  
    
- `sample(sequence, qtd)` – retorna uma lista com qtd elementos “aleatórios” da lista

import random

\# \--- randrange (o limite final NÃO entra) \---  
print(random.randrange(5))        \# Saída: 0, 1, 2, 3 ou 4  
print(random.randrange(1, 4))     \# Saída: 1, 2 ou 3  
print(random.randrange(0, 10, 3)) \# Saída: 0, 3, 6 ou 9

\# \--- randint (o limite final ENTRA) \---  
print(random.randint(1, 3))       \# Saída: 1, 2 ou 3

![][image8]

###### *m platform*

- código quer criar um arquivo → chama função python  
- python aceita e arruma de acordo com os requisitos do SO  
- SO checa se o pedido é válido e tenta criar  
- hardware ativa os dispositivos (disco, etc)   
- módulo platform: dados ocultos de hardware, sistema, interpretador   
- `platform(aliased = False, terse = False)` – default  
  - aliased \> 0 apresenta nomes alternativos das camadas em vez de nomes comuns  
  - terse \> 0 apresenta uma forma mais concisa do resultado   
  - ex: Linux-3.18.62-g6-x86\_64-Intel-R-\_Core-TM-\_i3-2330M\_CPU\_@\_2.20GHz-with-gentoo-2.3


- `machine()` – nome genérico (string) do processador que roda o SO \+ python \+ código  
  - ex: x86\_64


- `processor()` – nome real do processador/CPU, se possível  
  - ex: Intel(R) Core(TM) i3-2330M CPU @ 2.20GHz


- `system()` – nome genérico do SO  
  - ex: Linux


- `version()` – string da função version  
  - ex: \#1 SMP PREEMPT Fri Jul 21 22:44:37 CEST 2017

- `python_implementation()` – retorna uma string com a implementação python usada  
  - ex: CPython

- `python_version_tuple()` – tupla de 3 elementos: parte principal da versão python, parte secundária e número do patch  
  - ex: for atr in python\_version\_tuple():  
        print(atr) \# 3 7 7

- ###### *dir(module / function)* 

  - import module  
  - mostra todas as funções/entidades daquele módulo/função  
  - executa no console da IDE

###### ***criar módulo** (módulo e main mesma pasta)*

- arquivo [module.py](http://module.py): vazio  
- arquivo [main.py](http://main.py): import module (na mesma pasta) → rodar  
- nova subpasta `__pycache__`: arquivo `module.cpython-xy` (código semi compilado, roda só se alterar)  
- colocar um print em [module.py](http://module.py) \+ `print(__name__)`  
- roda [module.py](http://module.py): imprime o print \+ “`__main__`”  
  - quando roda um arquivo a variável `__name__` vira `__main__`  
- roda [main.py](http://main.py): imprime o print \+ “`module`”  
  - quando um arquivo é importado como módulo, sua variável `__name__` vira o nome do arquivo sem .py  
- usar `__main__` para ver o contexto que o código foi ativado  
  counter \= 0  
       
  if \_\_name\_\_ \== "\_\_main\_\_":  
     print("I prefer to be a module.")  
  else:  
     print("I like to be a module.")  
    
- `module.counter` – não é seguro, permite acessar variáveis privadas (não tem como esconder variáveis, como no java)  
  - pode informar que os usuários não devem modificar usando \_\_ antes do nome

   

- `#!/usr/bin/env python3` – para SOs Unix (mac, linux) essa linha informa onde está o interpretador Python (como executar o conteúdo), em SOs Windows essa linha é ignorada   
- **doc-string**: string posta antes de qualquer instrução de módulo, explica o conteúdo do módulo ""

###### ***criar módulo** (módulo e main em pastas diferentes)*

- SO windows  
- main python ([main.py](http://main.py)): C:\\Users\\user\\py\\progs   
- módulo: C:\\Users\\user\\py\\modules  
- variável path, módulo sys – variável (lista) que guarda os endereços dos módulos requisitados nos imports  
  - 1o elemento: endereço de início da execução  
  - python trata .zip como um arquivo

  import sys


  for p in sys.path:

    print(p)


  \# \#saída

  \# C:\\Users\\nicol\\anaconda3

  \# C:\\Users\\nicol\\anaconda3\\Lib\\site-packages

  \# C:\\Users\\nicol\\anaconda3\\Lib\\site-packages\\win32

  \# C:\\Users\\nicol\\anaconda3\\Lib\\site-packages\\win32\\lib

  \# C:\\Users\\nicol\\anaconda3\\Lib\\site-packages\\Pythonwin


###### 

##### **Pacote**

- tipo um container de módulos  
- requer inicialização  
  - arquivo \_\_init\_\_.py dentro do arquivo do pacote – executado quando algum dos módulos é importado; pode ser vazio  
  - pode colocar nas subpastas também, se alguma delas precisar de uma inicialização personalizada  
- módulo: def funX (X \= 1a letra do módulo)

- para impedir que o usuário execute o código do módulo como um script comum  
  import sys  
    
  if \_\_name\_\_ \== "\_\_main\_\_":  
      print "Don't do that\!"  
      sys.exit()  
  


##### **PyPI \+ pip**

- repositório mais importante, só pegar e usar os códigos  
- Python Package Index, mantido pelo Packaging Working Group, parte do Python Software Foundation – suporte aos devs python em disseminação eficiente de código  
- [https://wiki.python.org/psf/PackagingWG](https://wiki.python.org/psf/PackagingWG)  
- [https://pypi.org/](https://pypi.org/)   
- acessa pela ferramenta pip (portão para o universo dev python)  
- 

Dependências

- dependency is a phenomenon that appears every time you're going to use a piece of software that relies on other software, inclui mais de 1 nivel de software  
- ex: redsuspenders (pacotes: nyse \- wallstreet \- bull, bear)  
- **pip** – identifica e resolve todas as dependências  
- pip help – todos os comandos e opções  
  - pip help \[operação\]  
  - \--user – apenas para usuário local  
- pip list – pacotes instalados (criador preenche as infos)  
  - pip show \[nome do pacote\]  
- pip search \[pacotes, strings\] – não funciona mais → [https://pypi.org/search](https://pypi.org/search) – pesquisar conteúdo PyPI  
- pip install \-U \[pacote\] – atualiza para versão mais nova  
  - pip install \-U \[pacote\]==\[versão\] – atualiza para versão específica  
- pip uninstall \[pacote\] – desinstala

###### *Pygame*

pip install \--user pygame  
pip show pygame

**RESUMO** – módulo \+ pacote

- módulo: juntar entidades relacionadas (funções, variáveis, constantes)   
  - em cada 1a importação de um módulo, Python traduz seu código-fonte em um formato semi compilado nos arquivos \`.pyc\` e implanta esses arquivos no diretório \`\_\_pycache\_\_\` (no diretório home do módulo) 

- pacote: container que permite juntar módulos relacionados sob um nome comum   
  - pode ser um lote de arquivos implantados (subárvore) ou um .zip   
- para dizer ao usuário (que usa o módulo) que uma entidade deve ser privada (não usada fora do módulo): marcar o nome com prefixo \`\_\` ou \`\_\_\` (recomendação)   
- os nomes shabang, shebang, hasbang, poundbang, hashpling descrevem os dígrafos no \`\#\!\` (instruem SOs Unix como carregar arquivos-fonte Python; não afeta Windows)   
- para o Python "ver" um diretório não padrão: o nome do pacote deve ser inserido na lista de diretórios de importação (variável de ambiente \`path\` \- módulo \`sys\`)   
- arquivo \`\_\_init\_\_.py\`: executado quando um pacote é importado, para inicializá-lo (pode ser vazio)

##### **módulo OS**

- interagir com o SO – informações, gerenciar processos, operar com streams  
- função **`uname()`** – retorna objeto com atributos (Unix, Windows importa módulo *platform*)  
  - *systemname* – nome do SO  
  - *nodename* – nome da máquina na rede  
  - *release* – versão do SO (ex: 1.0)  
  - *version* – versão do SO (ex: 1.0-alpha)  
  - *machine* – identificador do hardware x86\_64

*import* os, platform  
print(platform.uname()) *\#uname\_result(system='Windows', node='WIN-F0FOK76J0KO', release='11', version='10.0.26200', machine='AMD64')*

- **`os.name`** (atributo) – identifica o SO   
  - posix (Unix)  
  - nt (Windows)   
  - java (Jython)

###### ***criar (mkdir) / listar (listdir) diretórios \+ recursivos (makedirs)***

os.**mkdir**("files/my\_1st\_directory") *\#path (endereço)*  
print(os.**listdir**()) *\#lista arquivos e diretórios do path passado (ou, se nenhum argumento é passado, do path atual)*

*\# \['.git', 'activities', 'draft.py', 'examples', 'files', 'modules', 'packages', 'progs', 'README.md', '\_\_pycache\_\_'\]*

- rodar 2 vezes causa *FileExistsError*

*\# todos os diretórios do path serão criados*  
os.**makedirs**("files/my\_1st\_directory/my\_2nd\_directory")  
os.**chdir**("files/my\_1st\_directory")  
print(os.**listdir**()) *\# \['my\_2nd\_directory'\]*

*\# Unix: mkdir \-p my\_first\_directory/my\_second\_directory*  
*\# Windows: mkdir my\_first\_directory/my\_second\_directory*

###### ***diretório atual (getcwd) \+ caminho absoluto (abspath)***

- retorna path absoluto  
- Unix: *pwd*

print(os.getcwd()) *\#C:\\Users\\nicol\\nicolegrazzioli\\python-essentials-2*

def find(path, dir):  
    path \= os.path.abspath(path)

###### ***verificar se é diretório (isdir) \+ mudar diretório (chdir)***

*if* os.path.isdir(atual\_path):  
    os.chdir(atual\_path)

###### ***deletar diretório (rmdir) \+ recursivo (removedirs)***

- Unix: *rm \-r \[directory\]*

os.rmdir("files/my\_1st\_directory/my\_2nd\_directory")  
os.chdir("files/my\_1st\_directory")  
os.makedirs("my\_first\_directory/my\_second\_directory")  
os.removedirs("my\_first\_directory/my\_second\_directory")  
print(os.listdir()) *\# \[\]*

###### ***system()***

- Windows: retorna o valor do shell após rodar o comando passado  
- Unix: retorna status de saída (0 se der tudo certo ou erro)  
- executa função passada como string

print(os.system("mkdir my\_first\_directory")) *\#Já existe uma subpasta ou um arquivo my\_first\_directory. 1*

###### ***m datetime***

- classes de data e tempo – verificar erros (logs), mudanças na base de dados, validação de dados, transferências bancárias  
- classe date – ano, mês, dia  
  - método *`today()`* – retorna objeto `date`

*from* datetime *import* date

today \= date.today()

print("Today:", today) *\# 2025-12-25*  
print("Year:", today.year) *\# 1 (const MINYEAR) \<= year \<= 9999 (const MAXYEAR)*  
print("Month:", today.month) *\# 1 \<= month \<= 12*  
print("Day:", today.day) *\# 1 \<= day \<= \[último dia do mês do ano\]*

- criar objeto *date* no formato ISO (YYYY-MM-DD)

my\_date \= date(2019, 11, 24)

- método *`replace()`* – não pode mexer nos atributos (são apenas leitura), pode passar 1+ parâmetros, retorna um objeto *date* para uma variável

d \= d.replace(year\=1992, month\=1, day\=16)

- método *`weekday()`* – retorna dia da semana inteiro (0-6)

print(d.weekday())

- *`isoweekday()`* – retorna dia da semana inteiro (1-7)

print(d.isweekday())

- criar objeto *datetime* – date e time podem ser tanto objetos separados quanto um só (classe combina)

datetime(year, month, day, hour, minute, second, microsecond, tzinfo, fold)  
*\# 1 (const MINYEAR) \<= year \<= 9999 (const MAXYEAR)*  
*\# 1 \<= month \<= 12*  
*\# 1 \<= day \<= \[último dia do mês do ano\]*  
*\# 0 \<= hour \< 23*  
*\# 0 \<= minute \< 59*  
*\# 0 \<= second \< 59*  
*\# 1 \<= microsecond \< 1000000*  
*\# tzinfo \= objeto da subclasse tzinfo ou None (default)*  
*\# fold (zonas de tempo) \= 0 (default) ou 1*

*\# EX:*  
*\# Datetime: 2019-11-04 14:53:00*  
*\# Date: 2019-11-04*  
*\# Time: 14:53:00*

- método *timestamp* – envia um datetime, retorna um float com os segundos (UTC)

*from* datetime *import* datetime

dt \= datetime(2020, 10, 4, 14, 55)  
print("Timestamp:", dt.timestamp()) *\# 1601823300.0*

- métodos *`today(), now(), utcnow()`* – retorna data e hora atual  
  - *`today()`* – atributo *tzinfo \== 0*  
  - *`now()`* – retorna igual *today()*, a menos que passe o argumento opcional *tz* (objeto *tzinfo*)  
  - *`utcnow()`* – data e hora UTC, *tzinfo \== None*

*from* datetime *import* datetime

print("today:", datetime.today()) *\# today: 2025-12-25 23:53:22.138194*  
print("now:", datetime.now()) *\# now: 2025-12-25 23:53:22.140864*  
print("utcnow:", datetime.utcnow()) *\# utcnow: 2025-12-25 23:53:22.141134*

- método *`strftime()`* – formatar data e hora, recebe uma string com o formato ([***diretivas***](https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes))  
  - string com *%* \+ letra, ex: *%Y* \= ano com século em decimal; *%y* \= ano com 2 dígitos

*from* datetime *import* date, time, datetime

d \= date(2020, 1, 4)  
print(d.strftime('%d/%m/%Y')) *\# 04/01/2020*

t \= time(14, 53)  
print(t.strftime("%H:%M:%S")) *\# 14::53:00*

dt \= datetime(2020, 11, 4, 14, 53)  
print(dt.strftime("%y/%B/%d %H:%M:%S")) *\# 20/November/04 14:53:00*

- método *`strptime()`* – cria um objeto *datetime* a partir de uma string, deve especificar o formato

*from* datetime *import* datetime  
*\# 1o arg: data e hora como string*  
*\# 2o arg: formato, pode dar ValueError*  
print(datetime.strptime("2019/11/04 14:53:00", "%Y/%m/%d %H:%M:%S")) *\# 2019-11-04 14:53:00*

###### ***m time***

- criar date com ***timestamp*** (diferença de segundos entre a data e 01/01/1970 00h – Unix epoch, início da contagem de tempo em sistemas Unix) – métodos `time()` \+ `fromtimestamp()`

*import* time  
timestamp \= time.time()  
print("Timestamp: ", timestamp) *\#1766701...*

d \= date.fromtimestamp(timestamp)  
print("Date: ", d) *\#2025-12-25*

- criar objeto *time*

time(hour, minute, second, microsecond, tzinfo, fold)  
*\# 0 \<= hour \< 23*  
*\# 0 \<= minute \< 59*  
*\# 0 \<= second \< 59*  
*\# 0 \<= microsecond \< 1000000*  
*\# tzinfo \= objeto da subclasse tzinfo ou None (default)*  
*\# fold (zonas de tempo) \= 0 (default) ou 1*

- ex: nap/soneca

*import* time

class Student:  
    def *take\_nap*(self, seconds):  
        print("I'm very tired. I have to take a nap. See you later.")  
        time.sleep(seconds) *\#espera 5s*  
        print("I slept well\! I feel great\!")

student \= Student()  
student.take\_nap(5)

- função `ctime()` – converte o tempo em segundos (desde 01.01.1970) para uma string; ou sem argumentos (tempo atual)

timestamp \= 1572879180  
print(time.ctime(timestamp)) *\# Mon Nov 4 14:53:00 2019*  
*print(time.ctime()) \# Thu Dec 25 20:11:59 2025*

- classe **`struct_time`**`()` – valores acessíveis por index

time.struct\_time:  
    tm\_year   *\# year*  
    tm\_mon    *\# month (value from 1 to 12\)*  
    tm\_mday   *\# day of the month (value from 1 to 31\)*  
    tm\_hour   *\# hour (value from 0 to 23\)*  
    tm\_min    *\# minute (value from 0 to 59\)*  
    tm\_sec    *\# second (value from 0 to 61 )*  
    tm\_wday   *\# weekday (value from 0 to 6\)*  
    tm\_yday   *\# year day (value from 1 to 366\)*  
    tm\_isdst  *\# her daylight saving time applies (1 – yes, 0 – no, \-1 – it isn't known)*  
    tm\_zone   *\# timezone name (value in an abbreviated form)*  
    tm\_gmtoff *\# offset east of UTC (value in seconds)*

timestamp \= 1572879180  
*\# retorna objeto em UTC, atributo tm\_isdst \== 0*  
print(time.gmtime(timestamp)) *\# time.struct\_time(tm\_year=2019, tm\_mon=11, tm\_mday=4, tm\_hour=14, tm\_min=53, tm\_sec=0, tm\_wday=0, tm\_yday=308, tm\_isdst=0)*  
*\# retorna tempo local*  
print(time.localtime(timestamp)) *\# time.struct\_time(tm\_year=2019, tm\_mon=11, tm\_mday=4, tm\_hour=14, tm\_min=53, tm\_sec=0, tm\_wday=0, tm\_yday=308, tm\_isdst=0)* 

- função as`ctime() + mktime()` – recebe um objeto *struct\_time* ou uma tupla que guarda valores de acordo com os índices da classe *struct\_time*  
  - as`ctime()` – converte um objeto *struct\_time* / tupla para string, função *gmtime* pega o objeto *struct\_time*, se não passar argumento pega o retorno de *localtime*  
  - `mktime()` – converte um objeto *struct\_time* / tupla para o número de segundos Unix epoch

timestamp \= 1572879180  
st \= time.gmtime(timestamp)

print(time.asctime(st)) *\#Mon Nov 4 14:53:00 2019*  
print(time.mktime((2019, 11, 4, 14, 53, 0, 0, 308, 0))) *\#1572879180.0*  
     
*\# tupla*  
*\# 2019 \=\> tm\_year*  
*\# 11 \=\> tm\_mon*  
*\# 4 \=\> tm\_mday*  
*\# 14 \=\> tm\_hour*  
*\# 53 \=\> tm\_min*  
*\# 0 \=\> tm\_sec*  
*\# 0 \=\> tm\_wday*  
*\# 308 \=\> tm\_yday*  
*\# 0 \=\> tm\_isdst*

- função *`strftime()`* – pode receber também como argumento um objeto *struct\_time* ou tupla – [***diretivas***](https://docs.python.org/3/library/time.html#time.strftime)

*import* time

timestamp \= 1572879180  
st \= time.gmtime(timestamp)

*\# formata objeto struct\_time*  
print(time.strftime("%Y/%m/%d %H:%M:%S", st)) *\# 2019/11/04 14:53:00*  
*\# formata hora atual*  
print(time.strftime("%Y/%m/%d %H:%M:%S")) *\# 2025/12/25 21:09:57*

- função *`strptime()`* – passa uma string (tempo) para um objeto *struct\_time*, análogo ao método *strptime* da classe *datetime*

*import* time  
print(time.strptime("2019/11/04 14:53:00", "%Y/%m/%d %H:%M:%S")) *\# time.struct\_time(tm\_year=2019, tm\_mon=11, tm\_mday=4, tm\_hour=14, tm\_min=53, tm\_sec=0, tm\_wday=0, tm\_yday=308, tm\_isdst=-1)*

- classe **`timedelta`** – criar objeto: subtração entre objetos *date*/*datetime* (retorna um objeto *timedelta*) \+ operações

*from* datetime *import* date  
*from* datetime *import* datetime

d1 \= date(2020, 11, 4)  
d2 \= date(2019, 11, 4)

print(d1 \- d2) *\# 366 days, 0:00:00*

dt1 \= datetime(2020, 11, 4, 0, 0, 0)  
dt2 \= datetime(2019, 11, 4, 14, 53, 0) *\# especificou o tempo incluso*

print(dt1 \- dt2) *\# 365 days, 9:07:00*

*\# argumentos do construtor (opcionais, default \= 0): days, seconds, microseconds, milliseconds, minutes, hours, weeks*  
*delta \= timedelta(weeks\=2, days\=2, hours\=3)*  
*print(delta) \# 16 days, 3:00:00 \--\> converte argumento weeks para dias (14d) \+ argumento days (2d)*  
*print("Days:", delta.days) \# 16*  
*print("Seconds:", delta.seconds) \# 10800 (3h \-\> sec)*  
*print("Microseconds:", delta.microseconds) \# 0 (milisec \-\> microsec)*

*delta2 \= delta \* 2*  
*print(delta2) \# 32 days, 4:00:00*

*d \= date(2019, 10, 4) \+ delta2 \# objetos datetime \+ dias e horas \= objeto timedelta*  
*print(d) \# 2019-11-05*

*dt \= datetime(2019, 10, 4, 14, 53) \+ delta2*  
*print(dt) \# 2019-11-05 18:53:00*

###### 

###### ***m calendar***

![][image9]

- função **`calendar(year)` \+ prcal(year)** – calendário do ano  
- função **`calendar.month(year, month)` \+ prmonth(year, month)** – calendário do mês do ano

*import* calendar

*\# CALENDARIO DE ANO*  
print(calendar.calendar(2025))  
calendar.prcal(2025) *\#nao precisa print()*  
*\# w \= date column width (default 2\)*  
*\# l \= linhas por semana (default 1\)*  
*\# c \= espaços entre colunas de meses (default 6\)*  
*\# m \= qtd de colunas (default 3\)*

*\# CALENDARIO DE MES ESPECIFICO*  
print(calendar.month(2025, 12))  
calendar.prmonth(2025, 12) *\#nao precisa print()*  
*\# w \= date column width (default 2\)*  
*\# l \= linhas por semana (default 1\)*

- função **`setfirstweekday(calendar.DAY)`** – mudar 1o dia da semana

calendar.setfirstweekday(calendar.SUNDAY) *\#6*  
print(calendar.month(2025, 12))

- função **`weekday(year, month, day)`** – retorna int do dia da semana

print(calendar.weekday(2025, 12, 26)) *\#4 \= quarta feira*

- função **`weekheader(width)`** – retorna dias da semana com X caracteres (se for \>3 retorna de 3\)

print(calendar.weekheader(2)) *\# Mo Tu We Th Fr Sa Su*  
print(calendar.weekheader(4)) *\# Mon  Tue  Wed  Thu  Fri  Sat  Sun*

- função **`isleap(year)`** – retorna True se for ano bissexto  
- função **`leapdays(year, year)`** – retorna quantidade de anos bissextos no intervalo (último não incluso)

print(calendar.isleap(2020)) *\# True*  
print(calendar.leapdays(2010, 2021)) *\# 3* 

- classe **`Calendar`** – tem métodos para preparar dados de calendário, construtor recebe parâmetro opcional *firstweekday* (default 0, int 0-6 ou constantes) – [*documentação*](https://docs.python.org/3/library/calendar.html)  
  - método (iterador) **`iterweekdays()`**  
  - método (iterador) **`itermonthdates(year, month)`** – retorna todos os dias do mês \+ dias antes e depois para completar uma semana  
  - método (iterador) **`itermonthdays(year, month)`** – retorna dias da semana em números, pode colocar *0*s antes ou depois para completar uma semana  
  - método **`monthdays2calendar(year, month)`** – retorna lista de semanas do mes (cada semana é uma tupla de numero de dia e de dia da semana), números fora do mês são *0*

c \= calendar.Calendar(calendar.SUNDAY)

*for* weekday *in* c.iterweekdays():  
    print(weekday, end\=" ") *\# 6 0 1 2 3 4 5*

*for* date *in* c.itermonthdates(2019, 11):  
    print(date, end\=" ") *\# 2019-10-28 2019-10-29 2019-10-30 2019-10-31 ...*

*for* iter *in* c.itermonthdays(2019, 11):  
    print(iter, end\=" ") *\# 4 5 6 7 8 9 10 11 ...*

print("\\n\\ndays2\\n") *\# dia do mes, dia da semana*  
*for* i *in* c.itermonthdays2(2019, 11):  
    print(i, end\='') *\# (0, 6)(0, 0)(0, 1)(0, 2)(0, 3)(1, 4)(2, 5)(3, 6\) ...*

print("\\n\\ndays3\\n") *\# ano, mes, dia do mes*  
*for* i *in* c.itermonthdays3(2019, 11):  
    print(i, end\='') *\# (2019, 10, 27)(2019, 10, 28)(2019, 10, 29\) ...*

print("\\n\\ndays4\\n") *\# ano, mes, dia do mes, dia da semana*  
*for* i *in* c.itermonthdays4(2019, 11):  
    print(i, end\='') *\# (2019, 10, 27, 6)(2019, 10, 28, 0)(2019, 10, 29, 1\) ...*

*for* data *in* c.monthdays2calendar(2020, 12):  
    print(data) *\# \[(6, 6), (7, 0), (8, 1), (9, 2), (10, 3), (11, 4), (12, 5)\] ...*

- classe **`TextCalendar`** – criar calendário de texto regular  
- classe **`LocalHTMLCalendar`** – subclasse de **`HTMLCalendar`**, construtor pega o parâmetro de local e retorna meses e dias da semana

**SUMÁRIO**

- para criar um objeto *date*, passa year, month, day  
- o objeto *date* tem 3 atributos read-only: year, month, day  
- método *today* retorna um objeto *date* representando a data local atual  
- Unix epoch: segundos desde 01/01/1970 00:00:00 até uma data, para criar um objeto: passar um *timestamp Unix* para o método *fromtimestamp*, retorna segundos em float  
- o construtor da classe *time* aceita 6 argumentos opcionais (hour, minute, second, microsecond, tzinfo, and fold)  
- módulo *time* tem a função *sleep*, que suspende a execução do programa por X segundos  
- classe *datetime* combina os objetos date e time, argumentos read-only: year, month, day, hour, minute, second, microsecond, tzinfo, fold  
- método *strftime* recebe 1 argumento (string) com as diretivas

#### **instalar/importar pacotes/bibliotecas – pip (Linux)**

- import os – acesso ao file system, pode ler e escrever arquivos  
- pip install cowsay  
- pip install qrcode

  import os

  import qrcode


  img \= qrcode.make("https://m.media-amazon.com/images/I/412ptOjfobL.\_AC\_.jpg")


  img.save("moo.png", "PNG")

- Teorias  
- Métodos http (flask usa 2\) \- conjunto de regras usadas pelo navegador e sites para se comunicar  
  - **GET**: acessar uma página e passar as informações pela url (digita url do site, tudo visível na url), não seguro para informações sensíveis; ex: Moodle “https://ead06.proj.ufsm/course”  
  - **POST**: acessar um recurso e passar (recuperar do servidor) as informações (ocultas) por formulário oculto (envia para o servidor); ex: amazon (oculto na url, não fica link tripa)  
  - **XML** \- transmitir informações pelo protocolo http, site cria e manda para o servidor  
  - **AJAX** \- js+xml, suporta json (dicionário python)


[image1]: <data:image/png;base64,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>

[image2]: <data:image/png;base64,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>

[image3]: <data:image/png;base64,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>

[image4]: <data:image/png;base64,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>

[image5]: <data:image/png;base64,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>

[image6]: <data:image/png;base64,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>

[image7]: <data:image/png;base64,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>

[image8]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAO0AAACtCAYAAABcFfjjAAA/MUlEQVR4Xu2dBXcUSduw+RHf+7yywMLiwUOMCBDcfYFlcQnuuywL64sES3C3ENwlQJAQJEiA4BLcCRAlgobU13d1qqfrru7xmVjXOddJpqq6x/qaqi4t9X/flCMGBgZFh1I4wqBoc/PQH+QbjXiD4oMhbTHi0JbfSUpscxI3zF9IMyg+GNIWEwb82Jp8fHOSSntv8xSyupunkMegeGBIW0zIebKZ5DxcQqVNPt6KnBnqRyY0qSHkMyjMfKsCp5kwpC0GJN1YTd4/20lST7Wn0gIJf3Sm4rbzrCLkNygMfEv+9/+sRy2zIW0RZ/fan2gpm5v9VBEWSDoeSqUFalaoIBxnUBCIMv7v/5Wl/M//irA0GdMxhrRFmKE9asnVYomPr49x0r7c2UaRFihTRjzewF2IospilqH89/8wSiOkdIDmM4lsSFtEGfFjbZLzeAMVFqrGKSdacNK+2t6EvImP4sTF5zBwNdqiMin/89/fyPzn/8h/6fCf/+Tn+W+TyIa0RRDPmhVJRsJIpZTN+5LJCUtL2q1NyOtjv3DSnv2zk3AuA9egJyvIByKCkP/vv/6X/l2xYhW5dOmSJsGNm8n58vOCwIa0RYyyZcuT9AtDSM7TLbK00t+8r580pQWuTO+lSHtlahcSMay5cE4D58ILK8pau049QU5rAYENaYsYIOz7p1vJh1fRkrRbyKe0BPLu+kRO2KSdsrBA9vPrnLTAjJ4NhfMaOAcmLF+6yrJCdRlLaA+GtEWIK7t7kfRLo6mwDELypPvZloqwyTGmUhZIjvtXkBboFFBbOL+BY6iFpQ1LUunKqsFYPEcwpC0irJvdjpayamFhBFRe7gdJ1vxGqOO8sIxHu+cL0gI1K1cWnsfAPrCwrHSF0hZLh+nYYyAJbNVLIKBFT7J91x4hvyFtEaDCdxWosJm3Z3HS5n3JIR9eRtG0N/ubCrIyct+/o9Je/qcTJ+2lfzqT8mW/E57PwFZM97BqYdu17yQIx2jStqcgqSUMaYsIrOEp/cJQTtgPSccIhLeHBypgWRmvdnch12cPJJf/7shJe/a3juTwuLakynfG4Av74RudmLBYUkZA826CjLZiSFuI+aZ0OZIWD8JK1eKXBzlpv35IkarGHzlp3x4eIAjL+Jj+llyc0pqTNubn9lTa6LFtSJnS4vMbWMZULZYbnUDYqVOnC7ICWD57MaQtxNw/0k8uZS8O40tZ2gBFyLvry5C0EtHa4r5/eZ7ET2zGSQvCMkBc/PwGlhDvY/UanbB4jmBIW0iJWt4lv1o8hLx/vpMT9nPGDblqfDRElFanxIUq8oWJLXSlBSa1qy+8DgN91NVi1lKMZXW2sIAhbSFkaC9/RdiMy+PFUjYvV6NqjBHF/ZD8zKy0QGtvYzqfdahLWbkvVquUxcI5A0PaQkaVShUVYXEXDyXpKC1lsx/u0RAVw4sLfbpM2PN/dhKEZdSuXEl4XQY8WveyWNjvfwwRhHMGhrSFiHLlvlManoCsxHmCtHlfsqm0KTGDNCTVILqfIm1q/HzyeNccKm3sRLkRSouoQcGkdOnywuszMIG7eGwpZR0JhrSFjNTzIeZLWaga54e0M3r3sxpE95fF3dacfM39TKU9OqGdICtjZxdPCn59Bgy+agylbHj4fE5Yc/2wjgZD2kLCi8PNeGFfHhCEzX3/gn5pOY/W0TyCnBYAcT+/e06uz+0riKolLWCs7CjCVY11GqCwqFrS4nhLsGBIWwgY17eOMnYYZMy8OVUQVl3Kpl8cbpe0UFV+c+wn8jH9jSAqY3+/IE7a7Z2NEhejbjW2tWqslg/H37xzX/k/6XWykM6CIW0BE+xfRZhWh2UFPiafoV9Y3tfPSmmcfMzK+1oVbw7KX/6R8dr3tDu71uOkBda2qyO87pKMpfvZBi27C8JpyacX1/6H4WbzGNIWIOXLlTeVsPE9KdlS1RfmySqyvj1NgZZfCO9f7CEZCePIp9QL5HP6LZJ2IZQX8+gQknpmMiX5xHglnsWlxv1Kcj9kkMS9q0hc6FCF2D96k8Pj2wnCMsJbGrOCGFxXz3++EcYYY0kxLOg9Bn79J5zGPX7yQshnSFuAvI1ppkiblyu3CkPIebqNivsp9aISZykkx4ykcqad/VOJ+5AUr0jLQt6XDyTl5GTlMQ7pT+4JwjI8K1UU3kPJA/XPSvezERHrHZJ28cpN9HHSG1OVGOcxpC0E3IsZw1WJU0+0VL6UD5nvSOqN1crj3E+fyAyvyspjCF9zv5BPOSbRIbyK6s9Je+vwARLqVYWT9lN2tnCuzx8/SDbLJTmEhMhlgrAMY4yy2HJ88eJFh6QF/p29lIvD6erjDGkLgO2L+5HM63+RtDM9VA1Qg8jXD2+VL+b59SvK/+HB3mTHxFHK42dXLlHxgI1D+yjx0bP+tktadi4WctLTSFj9aoKwwN6BwXQiA35PJQexpN23b7/D0loDC4a0bmbP8gFUWEbqyTZUWrZIG7t3ZSF65j+CZPOb1yez/KoqLcgs5H39Stb376Q8tlbazSMHkkcx25XHjy+co3mwsLu6eSsNViV58IWz7mntDYa0bmTgDw04YWX+JBkJoxRp3z/frXw5ICHIM6t+DdVXRsi2MSEkerLcr/v28CAl/klCPFnasanyOCnxtiBt+ovngrQ4zPTz0JQ2ekwbRdqo0a1LbB+us1qP7Q2GtG7C27O6hrAyMJ6YSSuXtnJIf/mCygPV1ewHcmsiC8dmDCTvrk3m7kUXtgoShFzSvjHJuDxPeXx8wRwhT3ZqivL/sk7NaPqqpjV5abvWE7qH9o5sJbzPkoCj/bSOYkjrJtIvjhRkpcK+Oki7dMxJCwGq0B9fH1bScHgqlbKQN/IHX/Il+yVOVkKodxUyJ6AaFwfHff7wQXm8vHENsZQd3UqQFpj/Y7DwXos79o6Igu4bc0Gdd9YCU0MkDoa0biBqYQCVDgubdWuG0g/74fVxi9ICZxcPJl8+flTyQEl7PWq30pjEunheXowy5ZHCp/c5Sp6L8ztyaRAHa0ix8Ob+XU7Y3d19BFnVjGzhLbzn4o3YgmyNtM4KhrQuZmwf0xDF1NOdOWk/vj2lSAvA/SwTlwkG4B0E4kL9uHRgtn818ubQAG6gxfJ29YR8RyY3V9LV8SDtsX7eyuNQL9M9LaxqgUXFtPOuKbz34ot1K1ZgabfuOoT9sysY0roQrzqVONmAd1enUGFzHq7mhGUwafNyc5QvKStxDn8e1VKpr/b35UTV4020GCcjN2TdXDSK20IEOPSjN9nby18QVI+S1KLM39daX9o6A0NaF1G2bDlBWFranmiZX8qKwgK5Oc8I7vbJujvLdI6Y5iT3QzKXDuOR1SLCWsjyOUzkff1CMq4t4fKZ0tmJ8ig5SU8UcS/93VmQU4+DY9oKn0PxBffXfkPKflvBLeIa0rqA8uUqUDEzEvhRT4z3z3fxsr6RSDppkkcjnJ7Vmbw9Yure0QpJMb/mS6u659UIULrK0mqHlCePaBU54a/2wsqNljhUghaIU5e2eg1SrhDXkNbJQN9l+pU/TPeu1/7ghE2P70erv3A/++HVSfLhxQlKbvYrRZrUZ0+Ue8uzEavI8YX53TSq7p01vTrRuDlBdZQ4CJfmd+KkpefxrkK2jR2ixGUkvaRDHtUB3/sC6vWkqLg/WSdu1JiSIq5197bOFteQ1slc2RJM57vilmImbc6TTVTarMTNirAA7HyHBXoUf5a82NKYbPqxNlna0kOlmJxnXsOq5GlkMMl+aiqlIR5LmxjRg9yN5FsvoetHL5wO8ZWqxfxuBIy4KfIC55YI+6GR8NkUR7juH2Pd46JH5PT6ipwZCaMFcTNv/kuFzbwdSXn/7JhK2i+KNCDagzOnyNdP79DCbKYAeVh85r0tXPyXj++5x1AVTj09SYlj8XoB0mLH8wubq4HtRLCkWoxu6SN8RsUPWVpjh4EiyPdSSYjvXd8ljDcJe+Nfev+afW+7Im3m7Q2KtF8/pinSnN+whnx4947kPNxHXh/oQd4c7C1IG+pbTZEWGqJYAOE+vxelTY4ZocTBLCIsLSvdGeakBS7/24UcGS+KimnpVfy7gkylrWk5VdgEGgvraKkLwyPhWENaJ4GFVcS9/LPcWpxkKlVzHkUp4mY/2KvEmwsvtzeXSmr9UTIQjoaHUuFyP5uq2lohrKGnIC0OWFI9LDVQ7R/QgFQuV/w3+dIUV2MGEKaDzo55avAxhrRO4PbOxoKsnLhXfyUf35zi7mGhaszEtUZakOzZxsYk694OnETDtf27aJ5ZfvwQRRzW9etG863p7IWTuLCqbT1BUD3O5G/khdnfvwEdnLFDonzZ4t+Ha6om8+I6azNphiGtg7w8bFp9Qg86e+dZDCctI/vuNpJ5ZwPJzXmtCAOzenB1NdS7MnmxRa4OXwkLENKB8EY1pfvgDHqO6NC/hHSGelRUWAN5Ro8WWE5LqIXd1c1LGL+MP7viiLrEZY1TzpbXkNYB9swLFATFpF8cojQ+vX8eK0gLQHUZhyf7xpNTM7qTo793IjfWhpC0M1O4Ring8uwAEj3Wixyb6EOeRAYr8W8O9CSv4yPI9QWBCreWtyXZaanky7sn3ACLxHU9yO013RVe3rxCXt25SU7+1EaQ0hqOwjpTGovDAREd6gqfYXGEiav04VJx5QEYIG/tOvUEEa0FupQMae1kcNdagqBayN07rOEJxD0uSPvhBT+wIu/Le0nS3wTeHuojiKtH1p2NQhwLGVcWc+KqSb+6luZ5n/xUENIazgyrT/b3EEtZxqxmtYTPsjjCi6stLwgIf1esWCXIyQhu3EzOl58XSm1DWjsIkKqqWE4tshLDuS4e0z0sX+J+efdYEQpCzqP9grAMLKIeyUeH8I+Pm5argQCt2FhYBgtYSEuAsGz447H+PoKwjJH+HsJnWjxh4orysmozRZIRhNQCBJfzycfAIA5DWhspU8a07Kk5Uk+2pcJmP9okSIvFxQGLyhE3WRDUEm8P9cVPoYScxwcFab9+kefWPtwWKoipx/kxDYUJB3FD/ARhGcEeJWmTL215ZYFNEusj55WPK2tIaysvo5uR10e0eXPUROb9dSTr4Uby7k4kybi5nmTciFBIv7aO8i5xF8l8GE3nx8p8IJ8/vCd31/9glptLm5PzM/ytIuXKOqSpHHLSk8mJqa3JyX9bCRz5ZxCJXRxOYsKnk209Ay0S0c6TrG1ZS5cljapzLAzyIPMCq5fABeLU8soCmyTWh+VjxxnS2kgZiT89xZbWwkZ4E2/y/MYl8vTyRZLy5AFRz+Z5ceOykN+dTJcoX+KEVYPltQ44DjCktZPWlSsIF2OhRjXWWEhzM8bayRiTkNrw+Q1pHcS/SkXyb//AIsHMUW3Ipk1bhPjfv69D+bNHHfJT0xouo+63xX+AhTswpDUwKGIY0hoYFDEMaQ0MihiGtAYGRQxDWgODIoYhrYFBEcOQ1kFKS0C/Y1GgbJny5NtylYR4d1FSN+xyNoa0DnLj0EDy5uRgt/P2VIgQZxHpGAjquKSY/uTuumaUR1tbkLhfAsjpn13DiOYlY4aPqzGkdYB1czqKYjhA2oUR5N210RxYzrenQ4Q8QPKZocL5tMj9kMI9vhvRnJP25pLGgmzOpEGtysLnaGAbhrR20qm1F8m4PEqQQpsQknJumCTlcJJ+aSTJuDpKkQ3OAXFYQjWQJ+2iJPRVMQ0Du/OJz2/iXeIa5f9ne79XhGXSAlg0Z1O5fPFfM8qVGNLaQU2PKiQtYSStbr6KGahL0vFBJE0SEvLC31QbeSOVnq9t5EXsYIWnhweQJwf6kycH+5NnRwbmx4co6TdXNSE3VjYh15Y2Jlclri2TOTrKjxwZoU/0MF+b2T/YR2HfIB9StrT4uRpYhyGtjUBjCh4AX9SAhcpxnLuZ5mVUk+3FkNZGLq7uRmJntLWZ8IbVuYsWxMF5HEF97piprYV0NRdWDidR433Nsrm7p8tZ1a1krBnlbAxpbSBm44/CPaQthAfL4oKwGVdM97XOIOXCCHru+U1qCmkc0v30s/0/KPeveuD7UFcROaikbUjtOIa0VnJpX3960WfdXkiy7662CzgexHp2bJAokxO4tPJ7EvVrMyFeDZbzwUZT6zHwcIsc/3BLc0EwV7ExxFf4vA30MaS1As861egFn3J2mNLymnx2vCClJeAcIC0WyZlolbTQOp16fjh5tK0NuS9Jej9SEjXCJCrG3aUtsKyPl/C5G2hjSGsBaHiCC1+vHzTtEsi7UhEz58FGumsdJjfnOXl3ZwGV9u3pIeTr5yzy9UuWlJZNPqWe5STLy4+3Fngd7P+c9DTuXPR58sFyvjg6SXoNpn1/YBOwpLjZVGqQ9uL0hiTulyDyOTud8vpiFCfa+5TnStqzmAhBRFvxqGB0BVmDIa0FUhPkflQsKydu/AhOWnMh7+tXesy7xLVcPJPs/fMNqlh+R3i9AOdTh9n+cs0AfhzUQS3s188mWYWQl6dUnUFadbi96XdFsi/vM5X4l3HbBAntwRjqaBlDWjOc3dnXorBAslRttlZaCGlP7wqiHZk9lYqmDgtaBHCP9QKU3vjxmfCO5O0pXlqIn+1flXzKeMLF6wUQF0sLIWpMOyqYWtqLmyPo+bGEtnLqZ0NcSxjS6rByRnuSDgMoNCTFpF/UL2lZN8zdE8e4+FCvKuTt2bFc3NMrl5T/s5LfKMdu7C/v3aMOLI2hDjN9PcjZ+V2kqju/QDnkmyNJqw63j0Ur59g7ZQKXtqJba3IpNJiLY+HICH+XSAscGFVf+D4MTBjSatChRT06ZBDLqUfW7bmKtFmJYapLWxZlSRsvkv74uBAPx37OfMTFsxDqXZXmebCrN7m3oxe5GdmDS4e0Q782o/E4TS/AMVF/TxTigJ1DvMmN5Y2JukqesGMzWdO5jimzKuR+/kw+57hGWmBVP6MrSA9DWkTXdt60mgpDFLGcWkBpzITNvPE7ybw1WXVpa4e7J4/TC/ze9l7S/fBwnEyWdWlJ0zf2CyApZ4fSe1N4LnWA9HPzOxEY14zT9AIcEzNvuhC3pX89pcU4Ly9XSbt5+AAJ9TG/dSYLzpYW2DHM6ArSolBJW6eAB5JXr2bqjoHB/VhQTMr5YTRv1u2ZynGWpE19+lgp3ZLPD6ek35rD5WHpb6V75VeSlAyc59Ts9uTlicHk0b4+XFrk4J4K6gDHLGrlx8Utl34gon/2IwkLGpFrK9pyaXumjBekXdgykHvMApN230AfhR2969nElh6eAhMaVBO+p5JOoZE2YgAMJPcmFcuIae6gdOnyiiyOMK8ZL0XasyeU+M3rhbyMdX27csfgdIa5PHppWvE4XN2/m+z76xccTfNiaSFu3598FRsCk9YVtKlWQfi+SjKFQtp/pPsmViWa7VuNrgaB87iaqzv6kLPzO9rMnvGNuQtsw4Cm3MWML0Dg5Kx23Dmub/1ZOCYurIPwXDjPrtHBumkbe9clRyf7C/FAWKN6XLxWWNa5Oc07N9CDi6fvsUsd8ixuNxfPpN3+Yz2XEFizJG3YZZ4Cl7ZCufLcfczC4BqyuG6cunV8Yy9uQII2YyTGkXfXx0tMolXirMSlNA3GEgMpUpU689YU7mKGC3lFRy8p31iNc8pk3xerxzA1D+fDeeKXdNFNOzLJj96j4ngq1mD5HvbdmyQuHcKHrEwqNcv7aFsrLh3iDg31pd/Vh3TT7vWuuKfFVCrg26fCQoFKC7umnfzJn8SOqE+OD6tPv5jo4b5U2pm+7rmXqV6tEr3oM69PJNmJy7lhh9YAx85vUoNKBqOmMq78RePZRU+l7RQoHJd9d5XECuk5l9DW58ybf3PHpCZIPxLX4UdibD7jSOaNX7g8F1aMocfKPyjyEEkGk/bRlhbk3KwGXNri5tVpWmJEM/oY+oMXtWkoTNm7s7ap0kCljt/4fV1FpEWN+dlLWDRng7+/kkiBSku/iJ8CyMlx/lRc9sWAtMBU76rCMc6kTNlyJP3KKKl0nKEhlTWsVGThV7EIIXukquueMU3J3nEtScy0H0jWnWVSybySIgurRj5f1KQeCpm3TUMj1bD0/b90Jvd29VVK2hcHu5Dtg7wo2wbWI2dnBCmjny4vDKYtxFv7yyXo7PpVFBnpGONpgWRF+5pkfnA1sqJdTXJ6aiCXDsB513WoTZY0q0E29/CkE9nZ9wXxDCyZs1lhdAUVnLQ7h8lVLODsJP6LWdq8liLu316uEzclQRL2xiROirRLf0ul2k9SyfdnvmCmtCypJM66s0D6Xy6Rs27PpitBwEAJ1vViLbD2E0xAoMvPXB5Jp+qpsWZpGQDyQkv3vfXiwH8t5jf2oOJiKbVgx7DH8f8EkR19pB+G3jLHRpt+aN3J+FYle4G4ApE2doLpC7j4Z6BC3EQ57uQEf0VaYFTtKsI5HCXp/AhJzD8UIVPOTVCEwmJgZHFXU7kXtaxNLq/pJkjpLl7HDhTENMfmvp5y1XddU1p1vidVkR9ulicIaAkLwBhkiHu4uQWJlWpFTFoAlqbBUrmD0G6ewndaUnC7tJGqahUs16mWFmBpc/09OHF7VXde6+GD2CEE7gOZsLiUtFTKsePgfxAg5bzlPl1XgaW0xMl/Aulrjg9rSB5uQnNpJXkfoDgGkxm+G7W0wKmfRKncQe8G1YXvtiTgVmn/6mxqwACwsIxzk6ULo5cXJy3QsnJF4Zy2Mvf31rJ4iUslVhAsLEBXPtSQVWZsflV5EXl6ZCCZ6VuFJMfJI5bczb1IvkS0hpsrmlBpN0klLp4Abw4m7ZXwYLK7v7cgLhbKXZTEJVndJm0H36rch33hD31pmbhYWqCWAxsTB9U3TRDPvPm7IIEaUVaZrMTF+aXsGLK+lx9Z/b030RLf1Tzc3FYQy1pYS+/9DdZLq64iHx/LV5EBuNfFQrmLMmXE3dKLM26R1rtaReUDPj9FFFSPeUF8FZlRo5zt4latwq8YYU3pCGN+U+OH05ZhdpxcNc5vNfauTJ4fGyQc52qe7esuSGULTNp7kWKaHnDvy0pbuK3B0gJHRxVMwxQAI9rwd15ccYu0yoc70XzpqgbkPjhU7rPVovQ3tv26ZqjuU/Gq/dbCpH13fSJJlmSGC5+e77R957OH1zEDBKFsxSSt9SUtoFSR5waTnX1FaQFoRMRCuYNY6Xnxd15ccbm0O4abunbifxfl1OQPU4MUllVNGY3n0+LRSWh4ckxYRtadcHqe3eOCyZwAeYUIW6bxOYKtLcV6rGhfi0oLC5PjNHMorctbtKvIDCyUu9g/0k/47osjLpX2yFjtX11BUhV4A6jV7WoLsqopq/G8auaNb0LSpOotLBvz6vggh0k6EUJenhpKpksX/eV13em5Ga9iBwv5ncntNc2cwo6h3vT1bx7oJaTpcXd9c3Jfup9lnJC+m629vHQ5MSGAnPjJ/UztUvzXUnaZtOsHmrp2tIA+2fOTofSF+9wAcsbMbm1YVAx+bgOD4oxLpP27s2nWDhMUSlD4e2ZSADlnqTEKqsf5Ay2skfYvF46aMjAobDhd2s71q3HCnpusIaWVsKpyeFB1QVTML3UNcQ1KBk6V1kvVtQPE/yaKaCtwHth1DUuqRf+aJa+j3aDk4TRpy5ZRde1AlVhjiKI9WFtFZnSv5rzhjgYGhRGnSAsd22phAbh3PfuraRIALXmt7fLJBxqp2LGLm9QUBNWjQUVjeRKD4otTpD06TrtrRwsogc/+KgNDFc//BkMaA7lhjfC/WnYABqVjOc1R245RUwYGRQGHpYWVJxQh81uJsajOYrafKKc5YILB3V296QAIPFDBXlLODCOhPvIKDw/39+OGRtLhkWcsD4+0B3MbZtlC4pqmyoioZW1r0qGMMBcXgD18APpY9Xz3I1UDK/K5sagx2dVPnDjAgDT8/bmLSuWK97I0Dkn7Zye5a0fr/hVKUvxh0m4fB6Te2Uec+aPHLAm4MJNODSFPDvQlT6L6ksc6PNjd2yIP9/Sms3rYBQ/MC65BXhwPIU8PDyA3N//IcXXN9+TKqi5Wc2pWG11ipzUn0ZPqi/xanxzOZ88oH56R2szy45eUWdmxFtk71ofsHeNDtg7wtJ7+nmRV65pkcdMaCgsae3DAKhcrWtW0msVNqzvMgkYeZH5DD9rGgq/X4oLd0nb0lbt2YNUJLKytyNVjGG8s3wvDQAs4r5bgWE491BemQckDRnzha7a4YJe06q4dLKCzwfe2c9DkeC1C87+4FR3rkVVdvKxiRv6iZlD1xWkFxcrO9ciyNjUFwhvIS8YAMP557fe1CoQ1nWuRhcFyyWaOhcHVyfIWNe1mbYfadrGifR3h2i0O2Cxt2TKmlmIsmCuAklct7ZGRfoKkamZJ972wFjF/rzmWZN78h664iO9BgdQLI6is6WwKHqwRdWs6yboTJrGQLpXKAXF35pGs23PoonD03Dd+o7N/3l2fQOhSq8LzwIqJsPzqBHkZViFdRH0PSXdoz9+lHWDS4ntNdxMzpr5wP6sFTDDAtSZ3sLxv8dus2iZpYclT9dIiUKXFkjkbXNICWFTG4mZ1FEEyb4Uqy8KYloeRZTHFraCPN/b3J7Ez2tL/s+7MF45zDasESbWE1ZrzCvHL29ckMb/7CxK5CtYwhePjJgUKguqBv0d38ZtU6uJruShjk7Qx4y3/WkIDVPxvYikMgkMXD9yv0ntWM/kgTUtWBlSZsLCwphRc7Jm3pgqCZN0OpSJjMRhQYqUljKRrC+NjtVlFV7CAaXqw7jCUuPT/OwskFtFVG/ExWbfD6AqP725Mkp7nZ+E1qHmyszVdrwnLygCBTk8PInGhQYJEzkbrdahL/NvLm+jOrcUU5OoWrYvR+HSrpVV37RQ0O3vzrchz6jNhpyuSvI2T1yHGQmDSEkaRhc1r0f9hRQosGwCLhOPjXMWjbS2t6t6B1RTDG1UTJHMm5l6HOh/UvrCg5sDfp7sY3KSGcF0XRaySNlq6bzk82o8cHOFLjkr/x4yTOTa2PjkixR8eZR7IowbOwYBzsPMdVwHx0aPk5zwwXCL/ueHDx6VsKl2IbQIVLCV+Ete/iaXAbBoYQN6eg93vTKszstJUvj8Vj3EVj3e0EuTQA9Z3cuU9LX4+AdXyM+f+CBLENEdBlrjQJoOv76KGRWlX9/cmOwd5FRrCG1ejLb1M2OgpLegFn524UhiQYI20cOHDX/W9LPyP87maJ7tsW6jtRexvqh121CGPPN3bQ5CQsq0V+ZIj7t/DQsrVRbTBCz+XHrRxbKtchYYdB7Cc5igocaFWgK/xooZZaetVqyhIYwtQSh4a6SvEA8fH+dNSd+9QHyFNzd5h3uTQGKmkHeVDtvWrR/6VJANA2HXdfeWL/kaYIKs10j4+NIDMqi8vGcOVsBp5XUlyXH9uBJJZIpqTr7kfsW9C+Jj+QJDWmnA3wnppAXbuE+P1l5/RA+6FsVTuYF8RX5ZGV9ry35Ynx6UvAkukZk+IN9knSQdV4FPShxEr5d8vVWVPaCzuBdVdyAu/dNDIBI1QAGt0goW59gzxJlEjfciR8b6aTPOVhQVYw1PGlZ8FUdXAthtYEgasWXwtsge3l0/y2XH0uNT8DaNdTWp8iO4C4VrYEnI/ZSpSfUi+jpOFkJK/4fXaLrWE59WDnf/i9IaClNZQUMMdIwYW3T2BNKWFrh0QDyTCogLs3tJecIsxhi5B8zvfpRQlvZa1nUzrRcEFn3FlLHl7epggKgaLIh+bXzW+qi5lYbcB/ljYCc/SjgP2kp4wzKa1hzPuR2PPSE5aGlnVox3ZOKS3VDPOw8lkU0gHeiwOy7rIfb2h3lXJmp4dyfuMdLKghb/S/4ufW48HG+T1kOEvFtJa9gwoGHF/aVc0u4I0pXVlSzEMlsCSWgJmAkV0qUNZ3b4WeRkbQkVKvzxdkEyP5LihnDD7fm5KFreqQ9IuyDsG0FbiW4uE4zhOhZDUc8PoDgTpCSM5IA42woISGiYVwPPBusmMFOk4SGN53pwYLAhgCRzSXjxTJGPg8O51ElnUrDqOJnGrltBd6/HxwJ7hPsJz66FeDzkqxFcQ0lpg1wJ8rbiDFvWcv0+UqxGk3T7UT54u96dpAjoGxgWfmyKD02xFa7IBJqKrLCyUtPd39aHSvT01VJTKCpi0sNB4SvwIknV7qalqHDdSyO8q8MVvDTiEN/FRRLu6VF4ONensQpyNpn/OScfRSvj65T1JubmZXFkYTGb6VBGe1xJMWr1FzK2loBY7r1PF8e1m3Akn7XGpSgz3pXuH+ZCbc4PIo6UNLYI/AGdySirx17avTWfszPSpSi6t7kaFwwLYQrpUIibu6E1m+VWVxB+iCPvu5gIhrytIiukvXPTWggMTdnuIF5UG8jyLHo+z0TwLm4qlrVa4t8G2VmyASZu4uim3FaY97B1YMCWunxM3eHM1irRrB/hI96p+3L3r7sHe5O68BoKoWFroT4X8h0aYFia3lv3SD8Tx8fwvLPTLwvk29/ZUGp52T2gil7AOruafcnYovYjjl3aRqruytGwghjvAF7wt4LCkfWP6XkJ9KiuNWam3tuFsityQvrJ7W5KdmoKzKCHvay5JhHWONZ5fC7gnZ9ICh0f4CSLayv7B5pffdRWVyheNebhU2knSDTl0v+AGJypuiDcn6a05QXTBNvj/+owg+mbV+aHxCn8YesSMM7VOq+NZHBN2fqvaVFjYQBlLYCuw2DhcwI6W2LbijN0BcPj65YsiJN22MqIlzkKeXU1Q8tzb0IbclkrD0PwZTUDs4jB8iCK4OWCivNa+tmd/s22ghR5RIQUjLhakMFKqvW9VEj1SW1hg7xCTtIlSqQtvDMYOs1J2T4h2P+sh6Ab6KYB2BeEPhqHOHzPWVNrC42m+VRRp2X2oNZtmWWL3mGB6UUIVGae5ErrrnGrMrhawI525Hd3fXlqB/ZJKxq/kzvGj5FPGY5xEw5zA2vT9hjWoQR/n5X4k6Xe3kPub25It/TzJiWXz0RGytDDlD78+a7gj/ShgAe2lIMTdKJXyWJLCRikYPoiFU3Pxb7lUVd+/XpkaSB4ukR/j/PYC1WR2/pVtainCwpS5uUEeZFb9qib87IeVMFDazJR+sDik57IFdi538jE7CzumGy5t26gc9/ruHZysGXZPHi88Z0kEi1KYKAXVXywQY9dgL3JvQQNyf5F+g5Ocz5tEqTba0gP6fqFKrB58wZ5r3xBZ2v2DfJS+2IIQY37TuuTKhokk5fJikpW4Su4KurOSPDj0r1RqVRfyFwQZr15g14RwUipBWX7oi7UmvJHExs9VUvmlTuFtmCrFZIIBEyAekxj+YulcAVSfoZSFvzAUjgm7on098iCqn1t4eHAsSUlYyA2y0OPhIXlQxtZhDYTzYC4vaUISFjVyCYvaBJAnly5g70jCzs1S7cRUowDi5zakx6TdjCRfPn7Ah9DSe9dE+X0xEhaKz2ktF+c1JBu71SUbvnceW3vWI4eG+boVz6qFcyleKq0eeNUIV6IWdnm7elzDk9w1szJ/vmo+MIeVzmOdLwGl4goC44axZHTu6+0wbsZO5o0pJDtxmUZey7yMm00vajpK6vp4ojedzxYyrocL94bWcGWxfH+uR1iQLO+NlU1o/sQI09605sDPYw/HRlu3ooWt4OvG1QTVKHwlbim4N8XdOIz7C03VYuiG0csL8Q8XNySJ4Q3IjVlB0j1vELn0VyDFtGib/Bfirk0PInfCGtBjYAFzOD8TNkyqgjK51A05WarxwQXJwuae9MKG14fT7OWdndIybqxoTHYN8yKRPeuQbYPqkVP/Bipp8Fo39vYUjjkzI4jsGeFNNvxYh2zsVYfsH+tL7moslaqHXoMZLMEK6ZdnNRKEcwZ7Bri/capahcLVFVQKC6jm9ly5tRhm5OD7Xag+w+ybYz/5kTO/+ZOEfyRZpwWSmzMbkDuSvHfnmwCZIQ7Ox4DJAuxDAVln+VQj072r0NIVCwswkc2ReWMSXR0i89Y/0t+/6GOcR5PrE6X8f9PVJ7JpiQ2lp1hqw9pQIMGqrl7y80nPkXV7pvQ3VPpRmUn/T4odTl4eGUBeHOxFnkf1IE92d1CAx2mXZwrnzbg6W5DCWcDrnRNQVYh3BEvjpSEPdEFh4ZxFQUwygF00sDwFBa0ewywbvMQLSAvLw8D/WFh7gEYtaLAyIcev7GBqKYY1ikEGLKy10rqOsfQvTOUDCa6s666kwWANpVtncyvNC5wtBK7u18y4OleRNiX+L+E4ZwHrHId6O6fKqwaLqgbeL+Q5PtY1VWTA3WOVj0kFF5anoNC8pwVZQVr2GAvoLNQjnuKXdqUSYFkZ6RdGkIzL8uD8lLMws4cfGQWD8uk0PI0ZOVB6wwB+fE7l2FMh9Jxw7ozLoyShTKjPs3GAPAuG1Qbgudg57kW2FC5ePe5vlC/qV0cHU2lfRPcTpHCE+xtMz7WkVQ3uPhWeW9lRAHZ33wg/Ji0s9iFjLE0nhDyX57imisxw93zcaOlHCAtUEGhK+0C617w7T5YWJrJj2ZzBtv6mCe0bBgaYFbagodPzrsmTDNj9LMCGVD7Z1Vm4aC3BJHm8zVQ64zwAzKKh23JYIZXWyo3bpM8aXvOtNU3lUVMaz6GG3ZNawtIKFyyPua1DnIG7xe3kV02QyN2UgqoqdPecVPWdQinLtvWwtLKEvTBhp3rLEjg6ptjVwJrIcPGv6ebNlbJPdncRLlhr0BoCiPNoIkkMo6vgeAD+N7fqBTRKweuO/StASDMHnJMtJ6MFyI2PUQMlMeQ7ZuW6yI6iXtrX1dSqXLBdQaWwTCd/9udajY+MNj9iyh5AVOU+9vTQ/OquKEphYuvQBvTiTzot33e/jRtCHu+QJ5jbA5YW5MN5nMGtlU3kH5uu1q9GgZHvyWURoTptbpVGBiuxr4QFC4K5CiyXKylTWpTJXQjSAvgFwnQ9nMdemKxAav49KBakMAKNOeqq8b0IxyTD0uJ0Z8L6X3G8q2HvDVamwIK5ilgbtl11lAoFtJ1qqeixvmSPqgoMrbr4xTHYFDx7UZewNzb1pBd/8mnHJwG4A7jo2frID7dav9SpHrTxp4RIe/JnxybH20r0cD/h2nUVBVHiloqdWJ/ETYb1mPgVJOhK/zojomDYIww9xFJiYJoerFcM/bxz65vWKZ7fsCbZPaohOfRLY3JwfENycEIjm9k5JJBs7htglk19/clGHXBec0T29COzfKqSFe3qkQ096pLIbnXI+u+1Gdu6Junc2MMiXZtVJ12bm8DpziSg4nfEv0J5Id7VqN9bs9qV3EorzyqkrfSduZrW3u7fuaAUXtpFD5AYRi9pbT8JjQCwrtRJmIqn0SAwL6i6IixjXefayrpP9oLPqQWseKEFSIjzOotq3xZMtcmgZGC1tFrQ4Ym/BUjIKyiy/XrUwu7oJW/hAaOdaGuxBCwfgwW0h/kN+G0vYaA8lhHLyonr6zpxKxWDlewNCicOSasHiAzCRg2Wp9mpG58YWEBrWNmmJlnXyVRCLwyuQc8PoqrPDfIyedj6UnpAOhbOWZQugPsdg+KPS6QFDg31VUpXLZZLAmIp9VDfDwM4Hp8bUMuIRcVg2ZzJNxofuoGBIyhjj7F0jnBgmI8gEWaal7y1B2NtR/EeFwuAgao2Pq8alg9LqoUrS1z8oRsYOAI3jBHvF3vhd+ke9Vd5TSgQG4A5tuen6G8ofXikL1nQ3EMQSAt8cc9vUJ0saFSdzPETL3wGzAaaZqYEVwMrNsAxWFA98HM5E/zBGxjYCx1csWeIvMcObvW1lV19+METesCibTMDPci8hjXJvAY1BOZKabMlZgVWo8wMqEZC7YSdMyyoulXg1wKEB8n3zmEB1aX/PWQCbWOKnwep+N13CpUq8KjTnE25MuUoON7VqN/bd9+Wdzsw+MEdYKlcjTAiCsYiw0ZZsPQM3RdWAvpkIQ76XWEeLQMeQzwQ0a2OIKcW03yqcDNx8CCGwsjecfIKEXci5cH9eBCBPagHVlgafO8oy9vXLNDBFfD+dvZ136goBiwZgwsWV/BnpzqCWK5EkNYeIrpbJyyQegk2gDZNmcOCWANMs2PT4zISRpLU88Pp8qp00sEpMb+jwO566ult+OK0B7W0MIMHpzuT01MD5B+d1U2FNFcBM4rU7xF2TcRSuQN3be7VwY23QA5La4uwD6P6K8IqJe0p62f3pF0wCW8VMCdWkptukBU/nG6ClXzGtmGTcAxc8LDEqrOkVW9a5axz6gHPxdaGOj09SJ65ozd7Jz8N8lBgJtEmeSYRTOanE/ojYVJ/PhHy+dljSMeyMq4vbCwI5S52uGn6Xs1K7pn945C02weY5sRCS6651lzYvZ2NgTUwKK6ULyNK5mxslhbuZQ+O9KMbTuMWUgwb2BAWLK+eYGBQ3PnD0/ULnQsLu13N35/HHAdCfAVB9QhXra5oN1dHkwO/NiNai5e/iHX++lEZl4cL1TtnA6/dFWs3uQqoLqs/9/U/1BHyWOLC9AZC1bUg2NnHtdXlQ2NcuyyNIC0A/bLsBcCSpzdmBpGbs2Qu/RVA1nWoRYnsXIvs7u9JDg73kkpeH/p3Y1fTbu1A+uWRghSOsK6nr3Lh3NvdV0h3lLQLQ4SLzRUUNWmBK0vkVnTYUgWn6aFe4QIm0WOBCpKYMa7bD3d1Py9BNmehKS17YhxvDbCWMRP2+TG5FIRd0tULscHiaVgWa7m+8Qd64dza8iN9DIuvwblhcbbU+OG08QkfYy3Jp527wJo51NIqDUewxItOQ05hAV734lY1hHgtoHFK3SgGcftDfAR5CpJ9g1y3jvKU9q7pCip1+d9AunA4k+7cZNMO8FDiRg33IUfG+JG9A7zJvCAPEhbgQeb6e9BRS0C49HhfSD3l+PuLGlBh45d0piKolxhVg4Wxlpl+VcmilvLWlwC0DONzs1ZffKw5XkZ/L1x0zoItz8LWTQLU0motNcOWIdXj4ZbmFHpu2oKrWjtKr3XYCazpJu/Ch+O1wO8JWqYvhTYUxCloYCNsZwwu0sIV8201V2NkwGR3aHxa3bm23ELsrd1CDC3DIHDiPKkKPSeQbB0UREWAZU2xTI5I+/qMvCH06zh5dUT6HGa6jNgqimpwyL4fRp7tba9caF+/vOfSP2e/FC5G4Omerlw+CDgPu3C/5n7CWWnI/fKZfMp8SlKvrRYucEAvfP2cRd6/vUxenQ4Vjkk6MwdnF1bJ+Jh2m0vPSTovvG4cWDzbiuRx1HCcRTiH5ffxiaQ/f0CubQon2/vwgy92DQzE2XUDPtZeXLXihbdHRUE8R+Baj/GTQdzSNjUFSbVgVeL5jWrmy6QvrM39rfms6iIvB6qOw+fG4HPgkHRyAnehYWk/Zb1ULj5amuWXliQvj8sH4c25fzUvWj1pcXgVx0tobfiY8cjscY/3DlBev5aQENhrBsFfn5mKUvNM6VLpDt+B1vt/fpC/vWBLtlobYqeHKAIVhLTA7v6iB86grBO7gjhpYQE39iSwpOqGnnUFOfVgk89BDCjhsDwMW6utauBiORXWQXkM58Lnx+Bz4BDRvxtX3cPSpr14RtNvr1SNJopozuVRB8iLhyVaKy2EJ/uH6spnLuS8OkdfPwxwyPv6mUt7/y6Dvi445/1NHbk0Fmb71yQ3VzSheXI/ZnBp+//6hR6/sKkHreLOCazFpasDblyz9X3sGSqv3miLtGxneyygIzh7gTjYFfIbJ82v5qSNHmkaqxne2LqZOmppLa2syMYcw04AUHVOvTBckEqPHaMa0i8mBRqbIM7CczFw6zUO9kj7KVN/f9hDM/8iUWN8zEp77/QJsqJ7WxIZ0ovu5I7DgiYemhf71rFDKMcXheEkGg5Om0zfQ9LpSThJkfZD6j2cRMPD+LNkedsams8LxwKXFwTLUn/KxlmUsGl4P3J+dgPl84TSHYez61fT97951CDNEnteUDVNaec2qKMJe31YPGeA5XMEKq6GhLbCSQsbPsPJFzeuIUhpifSEUebvL2FssEa6WigYcpgmiQyNS1ha2BEevhgmPj6POcxJe2Dq75K43cnLmFGUvNyPXLooLV/KYum+5uYqguhJe/3gPuVCA3CAuCO/1MfR3DHAm/t3cRYSJl3wIAsOm4b1Jcd/98fRXIBzJp2by8V9ys5Wnk8uqTtw6Z/Rfref37+neZUq8hbxtRwJn2Hx/W/q6YejhfePwcI5i6gQ5008gHXUsIS2wu0EDycN8/egI5mwlOZI3NlHEMVatPblAdJUEwueHRtEv5QLy+T9fmCCAM5vCViq9dG2lvg6sBiwtO+Tb3HpF7duIM+vJnBxi9s2Iqf+CbQoLatK4mDuYoZj2HkvhjXEWWiei+FSfF4uF5+R9IrMa+LNxeEAx+Z+4msakUP7KK8HnvNLTgqXfmDqbyQnPY2Lg+V+ri4NVsTFgUkLm0Vv7y2+JkgzVwVXh7jw8YJkrkK9C4cjTO5QWxDRFui6xyDskdF+yuRzW6Q9Oq2NIIgzgOozk3ZJa7kKxB7jvJZ4fVxuiNGq+lkKWFocqEjSRaoO0CoMu9XpSZvy9DFJ2L6RXNu7Q6od8nJBsFZavdcDpFxeiJNIZvIb7nHsYr6aPcu/BvcYAjvfqo61dZ9vlnQ/rA6ws3x4Q7nE1yppn19LoO//4Yl9mtVjOOdsK6U9FTaObP2xniCYqzgwxDmlbgcH9gQqFfuTvI8PHn4I6zuxSQAzfKuQJS2qC8vBrPu+jiCIs4CSkUkKX+KStnXp/+Z2v9MiKaa/2YvcUlBL+/r8fC4t98sXsrhNQwoOodJneCtfdCytubDjpxFOkVYrDYe5DT25xznp6dzj3M+fuPOl343i0qGBS/f9S9cP65+2JSztJM9Islba7ePlWVibf/AUBHMlzmioqlvFvq6gUkdG+AnCMla0Mr/42lszrcSOAve2tCp8aST9Ug790dzmUlZrcywcdvw8kixuF6zw+QN/j6aW1pbw5OJ5MsdfLm2tlfb8hjWKJNZIm/X8DM5itbT3407Iz6FR0rFwaPofVp8Ph4Qdm8niZtVtOu7o3OnK880Nqo2Tuc8G425pAWdsbm1Pw1QpLKqaJU1rCKIy3thY4tkKa3Ba1s6TfimbBgVa3WL85sQgcm+9OCJH6wJirceMT+9zuHQmbWJkJy7emgCDTu6uFaXN+5pLvnziG7wgqF/H7VXij8Syzs3J8i4tyNOoEdK9ZxZOJuciVyvHw3tNvhaBsyhhSXt5Y66kOzdxkhLYudZ2rSV9nq1wssXAXgcOX3O/SO9f/CFTv3+t1uOwRvU0gduTgpCWcWCo/VVmGIlVxsY1ss1KCyxuIop7aUknURQnwu5nI3r5cV+kNStdJB3tK4hqjbRs60i9Lp/cz3wJbE2IXTKPbOpdV5CWNUTl5fEtzy9vXafxCfMaab5WcwFasdWfld77ZYHlOz9X/HFggeWB15P9Mh4nWwzbpap+1FhfHK00ROFw83AUjQcBtaTVCwcndhJEKgiOjbZvAsKRsbbtMl/K3MqHWsQv7qw73tcZQLfQhr7yjuuYnaMaCfnpMadDSOq5YeTxtpZcxz7eQxVWWcDB2n5aHPBrAw7P+hdno/F5X7WlpedF4h5fOIckrjUvHA5ZyW+51wGlNBwPO8LjLiwITy6dV/Jqte5CWNOrM02nLdwajUn4vQNX9mzH2eT3iAKTNmqsD04iW0YPpgLYIm1ErzZkXgMPQSJb2NbLecDsIShBbQEGNlm7uH0pPJaYNjxJ1TpYqhQLO9O7Ku0vtRf8JRcEOFhTPY5buYiLe/c6STiv3vlPLp0nVAXV0i5oEcClQZjpV13zXDhc2r6JzG/G10Ywx+bNxIdJ30U1Ls+Ds6dwFi498fhhLo3VCLTAYccEcYyyup92eVex2g2NWNY2REFY1rml8DqKItMlrLnHLYW7cLSYJv3awrKmyzt4FjqWtKxuF/gDs8Ri6Zg5AVWFeHxeYF4jXgqWD8ctaOyh+3qgy0gvTQ/8OtTgvFrH4DScDq/JXDpjbqD254TjFjaT3//CJh5CGix4MFf6vOf4i+fSA/IXRmCE1/yGHlYRLoElxVglLczuYasfFhZSbZmsThcpg3G58qB56IrAX7gaLTnvbWguxO0a6iU+Vz44r1bc6emBSv6IHqbheAy2wBqOV7OiXQ1yeZFpIIMeG3vLDXqY22ua6r5mwNx7iv3TX3gevbwJCxsJcVcWN6J5YRIGDLTA6VBt3dRd+3Vrgau8hQlbWprrVTW/QJxV0qbE2zcrx1nARHcYQ0x/OCSe7m4nXCRaaM1T1ePcrIbKl+/K+aiFhW2D5RlTa7vbvmyMK8AXeXFlT3/r5P3u2+8EWa2WNnFnb0EiTiiQCZYovTCCDi9MOT+MriABkwLsXqHiCoxjFqf2wRxWtWh6cj3YIEppDUxa+B+Ex+ctVqhKcCGtADg7rXCsH+UuLI1nhjHKeve3ZqUNayLPjVW4an7anbVACzFMIIBzUXQmEzBeHu4jCIaBlmEcZytqaRkw1Q1fYFrQquwmqQoOawTD2sCq1wPLruCJ6AWNutp9a6U8JU/9etWrbFgLvEe6RrJqnWT1msnw/4PN+ufFF3ZJwNywyKM6XUGl8N6ujDnBNThhsUjuIOloP0EsV6IlrbPRqx24A/xatudXkdd0kccV6wE/QnK7gPyDxIYnOoLWcjr4gi5pHB8r9vPGThDF5QZXQLcMbEE53beqIqs1AxqczasjfelEc/xFuxLYMsMd0gLuFhdKTfwagGtLGtP3S8cJa6S7mnuRvLjRBbR1SGEDrxJ5cDS/JKvmiKiC2iDr9fGBwhfrKpQtLfK5tUIe1gctxzivK7BGXMgDFzY+9v56/SomRut4NTB4At43G5Dhbh6q2g5urWoiXMAlmSMjTWtWrejrrS/tg339FGHfxomNQa7g2d5u1le58veOgWoau0+CtYioBFaIoMf5MLn1eHGL6lw8nNeWVmhbYNVO9fPQLimNvOa4L4kJVVflNUM1doN1r3lxC3n3h90jvIU0Btuvh37myl4+Yj57UX9v+MI18CL7B8vLvE5sK8/D5aSN+beNIqw8Od0kFqzHBF0vXMOUDpCP7maX36KcKp0LptQB8D+QcnYIebqnozLm11HpHCV6ojyyaFM/TyFNDbxOuhHVerl6Bw0ruNSE90NLOGt/iCyhWiaVkt/fbLc4qvNdXSxXkWd4VRHeq83k3/dCdVxpkILGJ3iMUP/IqNk7xFe4aIsyW3vV49jcy8vEj/XIhp4mIiXW/2Bidfe6Cqu61SXLutYlfh6V5NZjmCUxx8+D7B3bhLJ/bGOyd0RDsnt4Q7J3jBzH2C2l7R7TmP5Vx1tL1ATpnFKxby97JHaP8CW7JPaMENPtZVkbeQ/X1Z3q0PMWPeDzkBiuAj6n4X5kgnTxmIPdy+P4gmC8dDG39axCWtcxEVi9okJA9UrEr2pFhXqVKxLPyhUUqn33nULV8t+RcmXLc3yrokzpchylS5dXwI0/hQmuy4eNO4aGCZgEj1uUtYDGK1zFdibwg4KfUwtYbQPyw99ZvlXpe8Djqs2Bnxc2Diuq4Pfyp5fzF8w2KDjM9tNayzQY4K0hnCPAxYefx9Xg5y/qqN/PsFpVhC/foGjy/wGKSfieUSowhQAAAABJRU5ErkJggg==>

[image9]: <data:image/png;base64,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>
