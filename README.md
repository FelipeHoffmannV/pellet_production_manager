
# Pellet Production Manager 🚀

O **Pellet Production Manager** é um sistema de gestão de produção desenvolvido em Django, focado na digitalização de registros de produtividade e tempos de parada. 

Este projeto nasceu de uma necessidade real: substituir o controle manual (papel e caneta) por uma interface digital intuitiva para tablets, eliminando erros humanos e garantindo dados precisos para a gestão.

---

## 📝 O Problema
No ambiente industrial onde o projeto foi concebido, os apontamentos de produção e tempo produtivo eram feitos manualmente. Isso gerava três grandes gargalos:
1. **Erros de Preenchimento:** Dados ilegíveis ou matematicamente inconsistentes.
2. **Cobranças Injustas:** Erros nas anotações levavam a interpretações erradas sobre o desempenho dos colaboradores.
3. **Delay na Informação:** O tempo entre a anotação e a análise gerencial era muito longo.

## ✨ A Solução
O sistema permite que o operador realize os apontamentos em tempo real através de um tablet. 
- **Validação em tempo real:** O sistema impede a entrada de dados inconsistentes (ex: tempo de parada maior que o turno).
- **Transparência:** Redução de erros de comunicação entre a operação e a gestão.
- **Eficiência:** Dados prontos para análise assim que são inseridos.

---

## 🛠️ Tecnologias Utilizadas
- **Python** (Linguagem base)
- **Django** (Framework Web)
- **Bootstrap/CSS** (Interface responsiva para tablets)
- **SQLite/PostgreSQL** (Banco de dados)

---

## 🚀 Principais Funcionalidades (Em desenvolvimento)
- [x] Cadastro de ordens de produção.
- [ ] Registro de tempos produtivos e paradas.
- [ ] Validações automáticas de jornada.
- [ ] Dashboard de produtividade diária.
- [ ] Exportação de relatórios (CSV/PDF).

---

## 🧠 Aprendizados (A "Virada de Chave")
Este projeto marcou minha evolução como desenvolvedor. Mais do que aplicar sintaxe de Django, o desafio foi:
- Mapear processos industriais reais para lógica de programação.
- Priorizar a **arquitetura e a experiência do usuário (UX)** no chão de fábrica.
- Entender que ferramentas (Google, IA, Documentação) são aliadas para resolver problemas complexos, e que a lógica de negócio é o ativo mais importante de um programador.

---

## ⚙️ Como rodar o projeto localmente

1. Clone o repositório:
    ```bash
  git clone [https://github.com/FelipeHoffmannV/pellet_production_manager.git](https://github.com/FelipeHoffmannV/pellet_production_manager.git)

    ```
2. Crie um ambiente virtual:
    ```bash
  python -m venv venv

    ```


   3. Instale as dependências:
    ```bash
    pip install -r requirements.txt

    ```


4. Execute as migrações:
```bash
    
 python manage.py migrate

```


5. Inicie o servidor:
```bash
python manage.py runserver
```


## 🤝 Contribuições

Feedbacks e sugestões de melhorias na lógica ou arquitetura são muito bem-vindos! Sinta-se à vontade para abrir uma *Issue* ou enviar um *Pull Request*.
