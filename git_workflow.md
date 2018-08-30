# Workflow básico de desenvolvimento

## Divisão de Branches

**Branches ativos**
- `master` -> Código estável e testado, publicado tanto em homologação quanto em produção
- `homologacao` -> Código que foi testado na máquina de desenvolvimento e está sendo testado no servidor de testes
- `peterson` -> Branch _*work in progress*_ do trabalho do Peterson
- `girol`- > Branch _*work in progress*_ do trabalho do Girol

As divisões de trabalho serão feitas nos cards.

**Branches tópicos (temporários)**

Branches que serão usados para resolver um problema pontual. Na maioria dos casos será para resolução de *bugs* :bug: .

### Passo a passo para resolução de problemas com branches tópicos:

1. Abrir uma _issue_
    
    Exemplo: Sistema não redireciona para painel após login.

2. Criar um `branch` com o nome da issue + seu número. Exemplo:

```bash
# Supondo que a issue tenha o número 42
git checkout -b issue_42
```

3. Commitar mudanças
4. Incluir no seu commit a mensagem: `Fix #42` (número da issue que foi aberta)
5. Dar merge em todos os branches ativos para integrar a resolução do bug em todos os cenários

## Integrando funcionalidades

As funcionalidades só podem ser integradas através de _*Pull Requests*_.

_*Pull Requests*_. são como um documento ativo que registra integrações de código no sistema _estável_.

Passo a Passo:

1. Depois de testado em ambiente de desenvolvimento, abrir um `pull request` no GitHub
2. Verificar quais _issues_ esse `pull request` resolve e marcar na caixa de comentários
3. Verificar conflitos e integrar as mudanças
4. Sincronizar seu clone na máquina de desenvolvimento
5. Dar merge no branch `homologacao`
6. Publicar em `homologação` e enviar para o cliente testar
