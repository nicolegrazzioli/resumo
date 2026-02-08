## **JS – backend**

- linguagem interpretada (lida e executada junto)  
- JS só executa uma coisa de cada vez – função em execução é enviada para o call stack  
- typescript – linguagem a partir do js, com tipagem  
- [node.js](http://node.js) – js back end, front, mobile e desktop

###### ***Variáveis***

- **var** nome \= valor – não recomendado (pode acessar fora do lugar)   
- **let** – consegue alterar o valor  
- **const** – não consegue alterar o valor  
- **boolean** (true / false)  
- **null** – vazio (padrão)  
- **undefined** – não sei ainda

###### ***Comandos***

- **console.log(mensagem)** – imprime no inspecionar (console) do navegador  
- **variável.toUpperCase()** – tudo em letras maiúsculas  
- **variável.toLowerCase()** – tudo em letras minúsculas  
- split – cortar string em lista – default: corta em cada caractere  
  - **nome.split(“**caractere como referência para cortar**”)** – ex: (“,”)  
- **variável.toString()** – converte variável para string  
- **typeof variável** – checar tipo da variável  
  - **Array.isArray(variável)** – verifica se é uma lista (retorna true/false)

###### ***Lista*** 

- guarda valores de qualquer tipo  
  - const list \= \[1, 2, 3, 4, “ana”, false\]  
- adicionar valores no fim da lista  
  - lista.**push**(“valor”)  
- adicionar valores no início da lista  
  - lista.**unshift**(“valor”)  
- remover 1o valor da lista  
  - lista.**shift**()  
- remover último valor da lista  
  - lista.**pop**()  
- remover valores da lista (posições)  
  - lista.**splice**(posição, posição, …)  
- inverter ordem dos valores  
  - lista.**reverse**()  
- alterar valor (mesmo sendo const)  
  - **lista\[pos\]** \= ‘valor’  
- verificar posição de elemento ou se existe na lista  
  - lista.**indexOf**(‘valor’)  
  - lista.**includes**(‘valor’)  
- colocar elementos em ordem alfabética  
  - lista.**sort**()  
- verificar quantos elementos tem  
  - lista.**length** 

###### *map*

- executa função para cada elemento do array (ex: multiplicar toda lista por 2\) e joga em novo array  
```
   const numbers \= \[1, 2, 3, 4, 5\]  
   //multiplicar cada um por 2 e joga em uma nova lista  
   // a função vai ser executada para cada elemento (recebe item atual)  
   const doubled \= numbers.map(function*(n)* {  
       return n \* 2;  
   })  
   // ou map(num \=\> num \* 2\)  
   console.log(doubled) //saída: \[2, 4, 6, 8, 10\]
```


- com *array de objetos*  
```
  *const users \= \[*  
      *{ name: 'Alice', age: 25 },*  
      *{ name: 'Bob', age: 30 },*  
      *{ name: 'Charlie', age: 35 }*  
  *\];*  
  *const ageBy2 \= users.map((user) \=\> {*  
      *return { ...user, age: user.age \* 2 }; //spread operator \- copia as propriedades do objeto e altera a idade*  
  *});*  
  *console.log(ageBy2); //saída: \[{ name: 'Alice', age: 50 }, { name: 'Bob', age: 60 }, { name: 'Charlie', age: 70 }\]*  
```
  


###### *filter* 

- seleciona alguns elementos da lista e joga em nova (ex: numeros pares)   
  const ages \= \[15, 22, 18, 30, 25\]  
  //colocar idades pares em nova lista  
  /\* const evenAges \= ages.filter(function(n) {  
       return n % 2 \=== 0; //retorna se for true  
   }) \*/  
  const even \= ages.filter(*(number)* \=\> number % 2 \=== 0);  
  console.log(evenAges) //saída: 22, 18, 30  
    
- com array de objetos  
  const users \= \[  
      { name: 'Alice', age: 25 },  
      { name: 'Bob', age: 30 },  
      { name: 'Charlie', age: 35 }  
  \];  
  const ageAbove30 \= users.filter(*(user)* \=\> user.age \>= 30);  
  console.log(ageAbove30) //saída: \[{ name: 'Bob', age: 30 }, { name: 'Charlie', age: 35 }\]  
  //id 3 ao 5  
  const new\_pessoas \= pessoas.filter((pessoa) \=\> pessoa.id \> 2 && pessoa.id \<= 5);      
  //saída: \[  
    { id: 3, nome: 'Carla' },  
    { id: 4, nome: 'Daniel' },  
    { id: 5, nome: 'Eva' }  
  \]


###### 

###### ***reduce*** 

- reduz toda lista a um elemento (ex: somar valores)  
- recebe 2 parâmetros: item atual e accumulator (total)  
- const sum \= ages.reduce(function(n, accumulator) {  
    return accumulator \+ n;  
  }, 0\) //inicializa accumulator em 0

###### ***Object*** 

- guarda propriedades e valores  
- pode ter objeto dentro de objeto, lista pode guardar objetos

  const person \= { 

  fiName: "Ana", 

  laName: "Silva", 

  age: "10", 

  hobbies: \['filme', 'livro', 'jogo'\], 

  dog: { 

  name: "luna", 

  age: 2, 

  },

  };

- acessar: person.propriedade

###### ***lista com objetos***

- ex: teste de backend de uma API  
    
  const todo \= \[  
      {  
          id: 1,  
          title: 'Estudar JavaScript',  
          completed: false  
      },  
      {  
          id: 2,  
          title: 'Fazer exercícios',  
          completed: true  
      },  
      {  
          id: 3,  
          title: 'Ler um livro',  
          completed: false  
      }  
  \]

    
- imprimir cada objeto da lista

  todo.forEach(function(item) {

      console.log(\`id: ${item.id} \- título: ${item.title} \- concluído: ${item.completed}\`)

  })




###### ***JSON***

const pessoas \= \[  
    { id: 1, nome: "Ana" },  
    { id: 2, nome: "Bruno" },  
    { id: 3, nome: "Carla" },  
    { id: 4, nome: "Daniel" },  
    { id: 5, nome: "Eva" }  
\];

const pessoasJson \= JSON.stringify(pessoas);  
console.log(pessoasJson);

const listaNova \= JSON.parse(pessoasJson)

- transitar dados entre frond e back, para enviar a lista com objetos  
- tudo tem aspas, não consegue mais acessar elemento específico (json é tipo uma string\\0)  
- transformar **objeto js em JSON**  
  - const listaJson \= JSON.stringify(lista)  
  - const novoJson \= JSON.stringify({id: 1, nome: "Ana"})  
  - console.log(novoJson)

  ![][image41]

- **JSON em objeto js**  
  const listaNova \= JSON.parse(listaJson)  
  //acesso  
  console.log(listaNova.nome)


###### ***Loop** – let pq vai alterando*

 const cars \= \['Audi', 'BMW', 'Lamborghini', 'Aston Martin'\]

*for*  
for (let i \= 0; i \< cars.length; i\++) {  
    console.log(\`nome: ${cars\[i\]}\`)  
}  
//OU  
for (const car of cars) {  
    console.log(car) //saída: Audi, BMW, Lamborghini, Aston Martin  
}

*forEach*

- bom para quando quer acessar o index (i) de cada iteração  
- executa bloco de código para cada elemento do array  
- cars.forEach(function*(car, index)* {  
-     console.log(\`índice: ${index} \- nome: ${car}\`)   
-     console.log(car)  
- })

*for in*

- bom para interação com objetos únicos  
- com objetos (propriedades)  
  for (property in person) {  
      console.log(property)  
      console.log(person\[property\])  
  }  
  saída 1: fiName, laName, age, hobbies, dog, email  
  saída 2: Ana, Silva, (3) \['filme', 'livro', 'jogo'\], {name: 'luna', age: 2}, ana@email.com

*for of*

- melhor para arrays (fácil de entender)  
- executa um bloco de código para cada elemento em um array   
  const iterable \= \[10, 20, 23\];  
  for (let value of iterable) {  
      console.log(value); //saída: 10, 20, 23  
  }

- com array de objetos  
  const iterable \= \[10, 20, 23\];  
  for (let value of iterable) {  
      console.log(value); //saída: 10, 20, 23  
  }  
  //objetos  
  const people \= \[  
      { name: "Ana", age: 12 },  
      { name: "Bia", age: 72 },  
  \];  
    
  for (let person of people) {  
      console.log(person);  
  } //saída: { name: "Ana", age: 12 }, { name: "Bia", age: 72 }


  
*while*

- executa enquanto condição for verdadeira  
- break – interrompe o loop  
- continue – interrompe 1 execução do loop  
  const i \= 0;  
  const n \= 0;  
  while (i \< 5) {  
      i\++;  
      if (i \=== 3) {  
          continue; //pula para a próxima iteração  
      }  
      n \+= i;  
  }  
  console.log(n); //saída: 10 (1 \+ 2 \+ 4 \+ 5\)  
    
  let i \= 0;  
  while (i \< cars.length) {  
      console.log(\`índice: ${i} \- nome: ${cars\[i\]}\`) //saída: índice: 0 \- nome: Audi, índice: 1 \- nome: BMW, ...  
      i\++;  
    
      if (i \=== 3) {  
          console.log('Chegou no índice 3, saindo do loop.');  
          break; //quebra loop  
      }  
  }

###### ***Condicionais***

- \== verifica só o valor  
- \=== verifica valor e tipo  
  - const sum \= 1 \+ 1  
  - if (sum \== 2\) → true  
  - if (sum \== “2”) → true  
  - if (sum \=== “2”) → false  
- && e ||  
    
- definir variáveis baseado em uma condição  
  - let var;  
    if (xxx) var \= x  
    else var \= y

    
- **operador ternário** (simplifica)  
  - **(***condição***)** **?** *valor se for true* **:** *valor se for false*  
    const b \= (sum \=== 2) ? 10 : 20;  
    console.log(b) //saída: 10

    
- **switch case**

  const day \= 3;

  switch (day) {

      case 2:

          console.log('Segunda-feira');

          break;

      case 3:

          console.log('Terça-feira'); //saída: Terça-feira

          break;

      case 4:

          console.log('Quarta-feira');

          break;

      case 5:

          console.log('Quinta-feira');

          break;

      case 6:

          console.log('Sexta-feira');

          break;

      default:

          console.log('Dia inválido');

  }


- **truthy e falsy**  
  - checar se é true ou false  
    - console.log(**\!var**)  
    - \! inverte o valor booleano atual  
      - \!false \= true  
      - if (\!var) é igual a if (var \== false)  
  - **falsy** – false, 0, "", null, undefined, NaN  
  - **truthy** – "0", "false", \[\], {}, function() {}, etc  
  - checar se lista é vazia  
    - if (lista.lenght) → se tiver vazia \= false  
    - if (lista) → sempre true

###### ***Funções e arrow functions***

- pode passar ou definir parãmteros

```
function sumFunction*(a, b \= 10)* {  
    console.log(a \+ b);  
}  
sumFunction(5); //saída: 15
```

**Arrow functions**

- declara como variável
```

*// Traditional function*  
   function add(a, b) {  
     return a \+ b;  
   }

   *// Arrow function – função de 1 linha*  
   const add \= (a, b) \=\> a \+ b;
```

###### 

###### ***POO***

- método estático – classe não precisa ser instanciada para executar o método (não usa nenhum dado de objeto), chama direto pela classe  
- herança – herda atributos em uma nova classe 
``` 
  class Pessoa {  
      constructor*(name1, name2, age)* {  
          //atributos  
          this.name1 \= name1;  
          this.name2 \= name2;  
          this.age \= age;  
      }  
    
      //metodo para juntar name1 e name2  
      getFullName*()* {  
          console.log(\`${this.name1} ${this.name2}\`);  
      }  
    
      static hello*()* {  
          console.log('Hello\!');  
      }  
    
      speak*()* {  
          console.log(\`Olá, meu nome é ${this.name1} ${this.name2} e tenho ${this.age} anos.\`);  
      }  
  }  
    
  const p1 \= new Pessoa('João', 'Silva', 30);  
  console.log(p1)  
  //p1.getFullName(); //saída: João Silva  
  Pessoa.hello(); //saída: Hello\!  
  p1.speak(); //saída: Olá, meu nome é João Silva e tenho 30 anos.  
    
  //herança  
  class Aluno extends Pessoa {  
      constructor*(name1, name2, age, course)* {  
          super(name1, name2, age); //chama o construtor da classe pai  
          this.course \= course;  
      }  
       
      speak*()* {  
          console.log(\`Olá, eu sou um aluno de ${this.course}\!\`);  
      }  
    
  }  
  const a1 \= new Aluno('Maria', 'Oliveira', 22, 'Engenharia');  
  Aluno.hello(); //saída: Hello\!  
  a1.speak(); //saída: Olá, eu sou um aluno de Engenharia\!
```

###### ***Desestruturação***

- extrair valores de arrays ou propriedades de objetos e passá-los para variáveis

**Array / lista**

- errado  
```
  const numbers \= \[1, 2, 3\];  
  const first \= numbers\[0\];  
  const second \= numbers\[1\];  
  const third \= numbers\[2\];  
  console.log(first, second, third); //saída: 1 2 3
```

- desestruturar array  
```
   const \[first, second, third\] \= numbers; //desestruturação do array
```

- atribuição de variáveis por desestruturação  
```
   const \[a, b, ...rest\] \= \[1, 2, 3, 4, 5, 6\]  
   console.log(a, b, rest); //saída: 1 2 \[3, 4, 5, 6\]
```

- novo array a partir (incluindo) array existente  
```
   const numbers \= \[1, 2, 3\];  
   const morenumbers \= \[...numbers, 4, 5, 6\]  
    
   console.log(numbers) //saída: \[1, 2, 3\]  
   console.log(morenumbers) //saída: \[1, 2, 3, 4, 5, 6\]
```

- inverter valores de variáveis (não precisa de aux)  
```
   let a \= 1;  
   let b \= 2;  
   \[a, b\] \= \[b, a\];  
   console.log(a) //saída: 2  
   console.log(b) //saída: 1
```

**Objetos**

- acessar propriedades  
```
  const user \= {  
      name: 'John',  
      age: 20,  
      email: 'john@email.com',  
  };  
```
    
- errado  
```
  console.log(user.name);  
  console.log(user.age);  
  console.log(user.email);
```

- desestruturado  
```
  const { name, age, email } \= user; //desestruturação do objeto  
  console.log(name);  
  console.log(age);  
  console.log(email);
```

- alterar: mudar nome da variável que guarda o nome do user, sem alterar o nome da propriedade  
```
  const { name: fullName, age, email } \= user; //desestruturação do objeto  
  console.log(fullName);
```

- interagir com o resto do objeto  
```
  const { a, b, ...rest} \= { a: 1, b: 2, c: 3, d: 4 }; //rest operator \- pega resto das propriedades  
  console.log(a); // 1  
  console.log(b); // 2  
  console.log(rest); // { c: 3, d: 4 }  
```
- outro exemplo  
  - atribui valor padrão se a propriedade não existir, previne de acessar propriedade inexistente no objeto   
  - b não existe no objeto que é desestruturado mas ainda consegue atribuir um valor para b  
  - valor original não é alterado (a: 3\)

```
  const { a \= 10, b \= 5} \= { a: 3};

  console.log(a); // 3

  console.log(b); // 5
```

- desestruturação em propriedades nestadas (aninhadas – acessar propriedades dentro de objetos que estão dentro de outros objetos)  
```
  const user \= {  
      name: {  
          fName \= 'John',  
          lName \= 'Doe',  
      };  
  };  
  const { name: fName, lName } \= user;  
  console.log(fName); //John  
  console.log(lName); //Doe 
``` 
  


###### ***Promises***

- JS só executa uma coisa de cada vez – função em execução é enviada para o call stack  
  - ex: função de requisição para API leva 10s para retornar  
  - call stack fica congelado até a função terminar  
  - ex: função com setTimeout()


- promise: envia função que não congela o call stack  
  - .then e .catch

  const returnName \= *(name)* \=\> {

      //retornar nova promise, recebe 2 parâmetros

      //resolve: quando a promise é cumprida OU reject: deu erro

      return new Promise(*(resolve, reject)* \=\> {

          try {

              setTimeout(*()* \=\> {

                  resolve(name);

              }, 5000); //resolve após 5s

          } catch (error) {

              reject(error); //pode passar função para o .catch – vai ser executada quando Promise for rejeitada, recebe de parâmetro o valor de reject

          }

      });

  };

  const printAge \= *(age)* \=\> {

      console.log(age);

  };


  **//returnName é deixada de lado e as próximas funções são executadas (printAge)**

  **//ela promete que vai retornar algo \- call stack pega a próxima função**

  **//.then \-- passa uma função que vai ser executada quando a promise for cumprida (resolve)**

  **//recebe como parâmetro o valor que foi passado no resolve**

```
  returnName("Ana B").then(*(name)* \=\> console.log(name)); //saída: "Ana B" após 5s

  printAge("21");

  /\*saída:

    21

    //espera 5s

      Ana B

  \*/
```

- pegar dados de uma API (URL)
```

  function fetchUsers*()* { //fetch \- função nativa do JS para buscar dados em uma API / URL

      fetch('https://jsonplaceholder.typicode.com/users')

          .then(*(response)* \=\> response.json()) //response: converte para JSON

          .then(*(jsonResponse)* \=\> console.log(jsonResponse));

  }

  fetchUsers(); //chama função
```

- saída

  ![][image42]

###### ***async / await***

- (melhor) – mesma API  
  - async (função assíncrona) – armazena valor do resolve em uma variável (response), sem usar .then  
  - coloca todas chamadas de Promises (await) em um bloco try catch – se alguma Promise falhar, executa catch
```

  async function fetchUsers*()* {

      try {

          const response \= await fetch('https://jsonplaceholder.typicode.com/users'); //await espera a promise ser resolvida

          const jsonResponse \= await response.json(); //await espera a conversão para JSON ser concluída

          console.log(jsonResponse);

      } catch (error) {

          console.log('Erro\!');

      }

     

  }

  fetchUsers(); //chama função
```


  


###### ***Selecionar elementos do DOM***

- DOM \= estrutura do site

**selecionar 1 elemento**

- getElementById – selecionar o elemento pelo id – retorna referência ao elemento  
- (melhor) **querySelector** – seleciona \#id ou .classe – retorna elemento em si  
  - retorna 1o elemento da classe/id

**//selecionar UM ELEMENTO**  
const addUserText \= document.getElementById("add-user");   
const addUserText \= document.querySelector("\#add-user") OU (".container") OU (".container \#id"); 

console.log(addUserText); //saída: \<button id="add-user"\>Adicionar usuário\</button\>

- alterar conteúdo com getElementById 

addUserText.innerText \= "alterado"; 

- alterar conteúdo com querySelector 

addUserText.textContent \= "alterado"; 

**selecionar vários elementos**

- (melhor) **querySelectorAll** – retorna lista, pode ser classe dentro de classe  
- (não é bom) getElementsByTagName – retorna itens de uma tag HTML  
- (não é bom) getElementsByClassName – seleciona elementos de uma classe  
  - *HTMLCollection* – não consegue usar elementos de lista

```
**const allItems \= document.querySelectorAll(".item"); //OU .items .item**  
**console.log(allItems); //saída: NodeList(3) \[div.item, div.item, div.item\]**  
**console.log(allItems\[0\]); //saída: \<div class="item"\>Item 1\</div\>**

**//transforma em array**  
**

const allItemsArray \= Array.from(allItems);**  
**console.log(allItemsArray); //saída: \[div.item, div.item, div.item**

**const allItemsbyClass \= document.getElementsByClassName("item");**  
**console.log(allItemsbyClass); //saída: HTMLCollection(3) \[div.item, div.item, div.item\]
```**

###### ***Eventos – mdn events***

- formas de executar uma ação quando algo acontece (ex: clicar no botão)  
```
  const submitButton \= document.querySelector('\#submit-button');  
  const myForm \= document.querySelector("\#my-form");  
  const body \= document.querySelector("body");  
    
  const items \= document.querySelector(".items"); //seleciona lista de itens  
  //ver valor dos inputs  
  const nameInput \= document.querySelector('\#name');  
  const emailInput \= document.querySelector('\#email');  
    
    
                          //evento de clicar, chama função event  
  submitButton.addEventListener('click', function*(event)* {  
  //previne o comportamento padrão do botão submit (tentar enviar ao ser clicado e recarregar a página)  
      event.preventDefault();  
      console.log('Botão clicado\!'); //ao clicar no botão: Botão clicado\!  
      const nameValue \= nameInput.value; //pega o valor do input name  
      console.log(\`Nome: ${nameValue}\`); //saída: Nome: valor do input name  
      //console.log(\`Nome: ${nameInput.value}\`); //saída: Nome: valor do input name  
  });
```

- acessar valor do input quando alterado  
```
  nameInput.addEventListener('change', function*(event)* {  
      console.log(event.target.value); //acessar valor do input quando escuta mudança  
  })
```

- mostrar mensagem se os 2 valores não estiverem preenchidos (exemplo) 
``` 
  if (nameValue \=== '' || emailValue \=== '') {  
          alert('Por favor, preencha todos os campos.'); //alerta se algum campo estiver vazio  
          return; //sai da função se algum campo estiver vazio  
      }
```

- mudar background/cor ao enviar  
```
   myForm.style.background \= "blue"; //do form  
   body.style.background \= "lightblue"; //do body  
   body.style.color \= "lightblue"; //cor do texto
```

- alterar textos dos *items* ao enviar form  
```
   items.firstElementChild.textContent \= nameValue; //altera o primeiro item para o nome  
   items.children\[1\].textContent \= emailValue;
```


###### ***Validar form***

- mensagem de erro no form – por 3s  
```
  const msg \= document.querySelector('.msg'); //div vazia no início do form  
    
  submitButton.addEventListener('click', function*(event)* {  
      ...  
      if (nameValue \=== '' || emailValue \=== '') {  
          //preenche classe msg acima do form  
          msg.textContent \= 'preencha tudo';  
          msg.classList \= "error"; //adiciona classe a msg  
           
          //após o tempo); a função abaixo vai ser executada  
          setTimeout(*()* \=\> {  
              msg.textContent \= ''; //limpa a msg  
              msg.classList \= ""; //remove a classe error  
          }, 3000); //3s  
          return;  
      }  
  })
```

- criar elemento (li) – createElement(‘tipo’)  
  - adicionar valores como novos *li* na *ul* (vazia) e imprimir 
```

      const li \= document.createElement('li');

      li.classList \= "item"; //adiciona classe item

      li.innerHTML \= \`Nome: ${nameValue} \<br /\> Email: ${emailValue}\`; //adiciona texto

      //adicionar li na ul

      items.appendChild(li); //adiciona li na lista de itens


- limpar campos após submit  
```
  submitButton.addEventListener('click', function*(event)* {  
      ...  
      nameInput.value \= '';  
      emailInput.value \= '';  
  })
```
  


## **JS** – front

- conjunto de ferramentas e bibliotecas (padrões e componentes reutilizáveis)  
- single page application (conteúdo atualiza sem recarregar a página)  
- (cliente) AJAX →← JSON (server)

#### **React**

- sempre usar componentes funcionais (funções)  
- concorrentes: vue e angular  
- terminal vs code: ctrl j  
  - npm create vite@5.5.2 . → react → javascript  
  - npm install  
  - **npm run dev** – para rodar no localhost  
  - npm install lucide-react@0.435.0 – ícones  
  - npm install uuid@10.0.0 – gerar ids  
  - npm install react-router-dom@7.7.1 – gerenciador de páginas  
- react (js) que insere conteúdo no html (**single page application**)  
  - SPA: html vazio, conteúdo inserido por js (se desabilitar o js, a pagina fica em branco)  
  - mais rápido  
- **react router** – gerencia rotas entre as páginas  
- renderizar componente – 1a letra maiúscula – \<Componente /\>  
  - **componente** – função que retorna jsx  
  - **componente** – classe \+ state – pouco usado, não consegue usar hooks (ex: useState)  
    import React from "react";  
      
    class Test extends React.Component {  
        constructor*(props)* {  
            super(props); //passar props para React.Component  
            this.state \= {  
                message: "hello world",  
            };  
        }  
        render*()* {  
            return \<h1\>{this.state.message}\</h1\>  
        }  
    }  
      
    export default Test;  
      
- quando cria uma função, transforma em componente se retornar um JSX (ex: h1)  
- todo componente por padrão recebe props  
  - quando chama uma prop que é uma função (ex: clicar num botão) e vai passar um parâmetro  
  - onClick \+ arrow function  
  - JS dentro do return – {}  
- verificar além de **espaços**: variável**.trim()**  
- vai para outra página (estrutura) e passa os dados – não tem uma página para cada tarefa, ao abrir uma tarefa vai para /tasks com os dados desta  
- **hooks** – permitem que você utilize estado e outros recursos do React sem a necessidade de escrever classes. Hooks são funções que 'se conectam' ao estado e aos recursos do ciclo de vida do React em componentes funcionais. Hooks incluem funções como State, Context, Ref, Effect, Performance e outros, que possibilitam o uso de diferentes recursos do React dentro dos seus componentes. Eles oferecem uma forma mais direta e simples de gerenciar o estado e as funcionalidades dos seus componentes funcionais.  
    
- **chamar função em interação** (ex: onClick) – arrow function, se não tiver *()* \=\> vai ser executada ao carregar a página  
  - passa a função que chama a função navigate (ao clicar)  
  - **botão que volta para a página anterior**  
     \<button onClick\={*()* \=\> navigate(\-1)}

    
- **persistir alteração**  
  - local storage (armazenamento do navegador)  
    function App*()* {  
      const \[tasks, setTasks\] \= useState(JSON.parse(localStorage.getItem("tasks")) || \[\]);  
    //salvar tarefas no local storage e manter num state  
    //parâmetros: função e lista  
    useEffect(*()* \=\> {  
      //executa a função sempre que algum valor da lista (tasks) for alterado \= state atualizado \- console.log("tasks foi alterado")  
       
      //atualizar localstorage com o state  
      //parâmetros: nome de identificação do dado, o que vai armazenar (json)  
      localStorage.setItem("tasks", JSON.stringify(tasks)) //converte tasks (objeto js) para string  
      //pegar dados do local storage e jogar no state  
    }, \[tasks\])  
      
    

**JSX**

- cria vários componentes (funções js, componentes) que são juntados – componentes em JSX (html \+ js)  
- JSX só pode retornar 1 elemento  
```
    return (  
      \<div className\="w-screen h-screen bg-slate-500 flex justify-center p-6"\>  
        \<div className\="width\[500px\]"\>  
          \<h1 className\="text-3xl text-slate-100 font-bold text-center"\>Gerenciador de tarefas\</h1\>  
          {/\* renderizar \*/}  
          \<AddTask /\>  
          \<Tasks tasks \= {tasks}/\> {/\* passar os valores \- prop tasks \= state tasks\*/}  
        \</div\>  
      \</div\>  
    );  
  }

- em Tasks.jsx (imprime lista com os titles de cada tarefa) – map  
  function Tasks*(props)* {  
    return (  
      \<h2\>  
        {props.tasks.map(*(task)* \=\> (  
          \<p\>{task.title}\</p\>  
        ))}  
      \</h2\>  
    );  
  }
```

- com listas (renderiza cada elemento, map): passar **key** – valor único, react saber qual item é qual  
- adicionar classe (configuração) se condição for verdadeira – componente filho (Tasks.jsx)  
  className\={ ${task.isCompleted && 'line-through'}\`} {/\* se task.isCompleted \== true, adiciona a classe line-through \*/}  
    
- **query params**  
  - passa parâmetro a mais na URL (id da task)  
  - ex URL: [http://localhost:5173/task?title=Titulo\&description=123](http://localhost:5173/task?title=Titulo&description=123)   
  - useNavigate() – retorna uma função que permite a navegação programática: redirecionar o usuário em resposta a interações  
      function onSeeDetailsClick*(*task*)* { //quando clica no botão para ver detalhes  
        const query \= new URLSearchParams() //faz tratamentos na string para não ter conflitos (ex: espaço)  
        query.set("title", task.title);  
        query.set("description", task.description);  
        navigate(\`/task?${query.toString()}\`);  
        // navigate(\`/task?title=${task.title}\&description=${task.description}\`)  
      }  
      
- **componente de estilo** (css) – ex: input – Input.jsx  
```
  function Input*(props)* {  
      return (  
          \<input  
          className\="p-2 rounded-md w-full mb-2 border border-slate-300 outline-slate-400 px-4 py-2"  
          {...props}  
          /\>  
      );  
  }  
    
  export default Input;  
```
- chamar

```
          \<Input

            type\="text"

            placeholder\="Task title"

            value\={title}

            onChange\={*(event)* \=\> setTitle(event.target.value)} 

          /\>
```




- **State** (estado)  
  - pode ter quantos quiser  
  - funções no componente pai (App), passa para componente filho  
  - quando altera variável, altera (atualiza) interface (função é executada novamente)  
  - ação de resposta a uma interação do usuário  
  - importa useState do react  
    import { useState } from 'react'  
```
      
    function App*()* {  
      const \[msg, setMsg\] \= useState("Mensagem inicial")  
      
      return (  
        \<div\>  
          \<h1\>{msg}\</h1\>  
          \<button onClick \= {*()* \=\> {  
            setMsg("Fui clicado");  
          }}  
          \>Mudar mensagem\</button\>  
        \</div\>  
      );  
    }  
```
    

**API**

- url que chama e dá algum recurso de um banco de dados  
  - axios npm ou fetch (js)  
- ex: [https://jsonplaceholder.typicode.com/](https://jsonplaceholder.typicode.com/) ([https://jsonplaceholder.typicode.com/todos?\_limit=10](https://jsonplaceholder.typicode.com/todos/1))  
- usuário acessa componente (página inicial) – ação → componente chama API → dados da API persistidos no estado do componente  
  ![][image45]  
- função executada só na 1a vez que o usuário acessa a aplicação (useEffect, 2o par: lista vazia \[\])  
- pegar dados de API e persistir  
```
  useEffect(*()* \=\> {  
    const fetchTasks \= async *()* \=\> {  
      //chama API  
    const response \= await fetch(  
      'https://jsonplaceholder.typicode.com/todos?\_limit=10',  
      {method: 'GET'}  
    );  
    
    //pega dados que ela retorna  
    const data \= await response.json(); //converte response para json  
    
    //armazenar/persistir dados no state  
    setTasks(data)  
    };  
    fetchTasks();  
  }, \[\])
```




**Estrutura**

- package.json – arquivo com scripts padrão e dependências node  
  - padrão: "vite": "^7.0.6"  
  - mudar para 5.4.1  
- src/main.jsx  
  - importa bibliotecas/arquivos  
  - renderiza a aplicação  
  - app é um componente  
  - createRoot – faz a inserção no html (spa) pelo js  
- App.jsx  
  -  

**Deploy (subir online)**

- vercel – [https://vercel.com/](https://vercel.com/)   
  - npm run build

**Tailwind**

- [https://tailwindcss.com/](https://tailwindcss.com/)   
- estilizar elementos com classes utilitárias (tipo bootstrap)  
- npm install \-D tailwindcss@3.4.10 postcss@8.4.41 autoprefixer@10.4.20  
- npx tailwindcss init \-p  
- em [tailwind.config.js](http://tailwind.config.js)

  content: \[".index.html", "./src/\*\*/\*.{js,jsx,ts,tsx}"\],

- em index.css

  @tailwind base; 

  @tailwind components; 

  @tailwind utilities;


  
![][image46]![][image47]![][image48]

#### **Angular**

- linguagem typescript  
- [Node.js](http://Node.js) – plataforma para execução de código JS no servidor  
- npm – instalação e gerenciamento de pacotes e dependências  
- Angular CLI (command line interface) – simplifica tarefas (criar projetos, gerar componentes) e processo de construção  
- `ng new nome-projeto` – cria novo projeto  
- `ng serve` – carregar no navegador (localhost:4200)

**Módulos**

- estruturas que agrupam componentes, serviços, etc  
- classe com `@NgModule`   
- `ng g m nome --routing` – cria módulo

**Componentes e Templates**

- partes independentes e reutilizáveis em uma interface web  
- cada recurso da interface é encapsulado em um componente (dividir aplicação em partes)  
- contém lógica de aplicação, manipulam eventos, interagem e fornecem dados para o Template (visual do componente)  
- encapsulamento de lógica e de interface do usuário

**Rotas**

- navegação entre diferentes componentes sem recarregar a página (SPAs)

**Data Binding**

- mantém os dados do componente sincronizados com o visual no template  
- Interpolation `{{ }}` – exibir valores do componente direto no template  
  - ex: `{{ nome }}`  
- Property Binding `[ ]` – vincula uma propriedade do DOM a uma expressão no componente  
  - ex: `[valor]=”preco”` (vincula valor da variável preco do componente a uma prop DOM  
- Event Binding `( )` – eventos DOM são vinculados a métodos no componente  
  - `ex: (click)-”enviarDados()”` (vincula o evento de clique a um método no componente

**Diretivas**

- recursos para manipular o DOM e controlar a aparência do template (interface dinâmica)  
- Diretivas de atributo – modifica aparência ou comportamento de um elemento do DOM  
  - ex: ‘`ngStyle`’, ‘`ngClass`’  
- Diretivas estruturais – manipula estrutura de elementos do DOM  
  - ex: `*ngFor` (iterar sobre uma lista de elementos no componente e renderizar no template)  
  - ex: `*ngIf` (exibe/oculta elementos no template com base em uma condição no componente)

**estrutura**  
package.json – dependências  
angular.json – configurações para o angular cli, css  
tsconfig.json – TS para JS (navegador)  
pasta src

- [main.ts](http://main.ts) – ponto de entrada  
- index.html – única HTML  
- styles.css  
- pasta app  
  - [module.ts](http://module.ts) – quais peças existem, tipo o pom



[image45]: <data:image/png;base64,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>

[image46]: <data:image/png;base64,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>

[image47]: <data:image/png;base64,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>

[image48]: <data:image/png;base64,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>

