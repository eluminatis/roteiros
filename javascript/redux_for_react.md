# Configuração e uso do redux no react

instale redux e react-redux no projeto

```bash
yarn add redux react-redux
```

vamos usar para esse exemplo uma lista de cursos

## crie o store/index.js

```javascript
import { createStore } from "redux";

const INITIAL_STATE = {
  data: ["React Native", "ReactJS", "NodeJS"]
};

function courses(state = INITIAL_STATE, action) {
  switch (action.type) {
    case "ADD_COURSE":
      return { ...state, data: [...state.data, action.payload] };
    default:
      return state;
  }
}

const store = createStore(courses);

export default store;
```

imagine o `courses` como uma função que recebe um objeto com o attr `action` que tem um attr `type:string` e com base nesse type vc vai executar uma ação, essa ação sempre deve receber o state anterior e devolve-lo com as alterações desejadas, seja inclusive, update ou exclusão de algum item especifico do state, dentro desse action vc pode colocar um attr contendo o conteudo necessário para essa alteração, normalmente se usa o attr com nome de `payload` para se manter um padrão.

## crie seu App.js

```javascript
import React from "react";
import { Provider } from "react-redux";

import store from "./store";

import CourseList from "./components/CourseList";

function App() {
  return (
    <Provider store={store}>
      <CourseList />
    </Provider>
  );
}

export default App;
```

o Provider vai receber o store e garantir que todos os filhos dele tenham acesso a esse store, por isso é importante que ele fique no topo da arvore de componentes da aplicação

## criando a lista de cursos

```javascript
import React, { useState } from "react";
import { useSelector, useDispatch } from "react-redux";

// actions sempre retornam um objeto com o type usado para identificar a ação no reducer e os dados necessários para realizar a ação
function addCourseAction(title) {
  return { type: "ADD_COURSE", payload: title };
}

export default function CourseList() {
  const [input, setInput] = useState("");
  const courses = useSelector(state => state.data);
  const dispatch = useDispatch();

  function addCourse() {
    dispatch(addCourseAction(input));
    setInput("");
  }

  return (
    <>
      <ul>
        {courses.map(course => (
          <li key={course}>{course}</li>
        ))}
      </ul>
      <input
        type="text"
        value={input}
        onChange={e => setInput(e.target.value)}
      />
      <button type="button" onClick={addCourse}>
        Adicionar curso
      </button>
    </>
  );
}
```

os dois hooks principais para se usar o redux são `useSelector` e `useDispatch`

#### useSelector

recebe uma função que recebe o state inteiro da aplicação e devolve o que vc precisa para esse componente

#### useDispatch

Devolve uma função que recebe um objeto `{ type: "nome da ação", payload: dados necessários para essa ação }`, normalmente esse objeto é montado por uma action, no nosso exemplo a action é `addCourseAction` mas basicamente esssa action faz alguma coisa e devolve um objeto que carrega o nome da ação e os dados necessários para executa-la.

concluimos que para adicionar ou remover algo do redux precisamos criar o reducer que recebe o state inteiro da aplicação e action e de acordo com o type da action manipula esse state e devolve ele com o novo valor, cria-se uma action para montar o objeto com o type e dados e passa esse objeto para o nosso reducer por meio do useDispatch e quando é preciso ler algo desse reducer usa-se o useSelector.

repo desse exemplo https://github.com/PetersonJFP/react-hooks-redux-example
