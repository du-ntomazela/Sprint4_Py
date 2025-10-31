# Como cada estrutura/algoritmo foi usado no contexto do problema

## Definição clara do problema

Em unidades de diagnóstico, precisamos planejar compras de insumos ao longo de T dias com demandas diárias conhecidas e sem permitir falta, minimizando o custo total. O custo total é a soma de: custo fixo por pedido (K), custo unitário de compra (C) das quantidades compradas e custo de estocagem (H) para itens armazenados entre o dia em que foram comprados e o dia em que serão consumidos. A decisão é escolher em quais dias comprar e até qual dia cada pedido irá cobrir. Modelamos isso por Programação Dinâmica determinística (sem previsão): no estado t (primeiro dia ainda não atendido), escolhemos um j ≥ t para fazer um único pedido em t que cobre as demandas de t até j, pagando K + soma dos custos de compra e estocagem desse intervalo, e então avançamos para t = j+1. A função de valor é V(t) = min_{j∈[t..T-1]} { Custo(t→j) + V(j+1) }, com V(T)=0. O plano ótimo é a sequência de intervalos (t→j) que particiona os T dias com menor custo total.]

---

## Notação rápida

- **T** — número de dias do horizonte.  
- **D** — vetor de demandas diárias conhecidas \([D_0, \dots, D_{T-1}]\).  
- **K** — custo fixo por pedido.  
- **C** — custo unitário de compra.  
- **H** — custo de estocagem por item por dia.  
- **t** — primeiro dia ainda não atendido no estado atual.  
- **j** — último dia coberto por um pedido feito em \(t\) (intervalo \(t \to j\)).

---

## 1) Recursiva com memorização (top-down)
- **Ideia:** definimos uma função `dp(t)` que retorna o custo mínimo para atender dos dias `t..T-1`.
- **Fluxo:** para um `t` dado, testamos todos os `j ≥ t`, computando `Custo(t→j) + dp(j+1)`, e escolhemos o menor.
- **Memorização:** guardamos `dp(t)` em um cache/dicionário para **não recalcular** os mesmos estados (evita recomputações exponenciais).
- **Por que aqui:** o espaço de estados é simples (apenas `t`), então a recursão fica clara e curta. A memorização garante eficiência.

**Efeitos práticos no problema:**
- Calcula **só os estados necessários** para o `t` inicial.
- Útil para validar a formulação rapidamente e manter o código direto.
- Se parâmetros mudarem, basta limpar o cache (reexecutar a função) para refletir o novo cenário.

---

## 2) Iterativa (bottom-up)
- **Ideia:** construímos uma tabela `V[t]` de tamanho `T+1`, preenchendo do final para o início.
- **Ordem:** começamos com `V[T]=0`. Para `t = T-1` até `0`, testamos todos os `j ≥ t` e salvamos o mínimo em `V[t]`.
- **Reconstrução:** armazenamos também o `j` que minimiza em cada `t` (ex.: vetor `nxt[t]`) para recuperar o **plano de compras**.
- **Por que aqui:** elimina recursão (sem risco de estouro de pilha) e tem **complexidade previsível**. É mais adequada a entradas grandes.

**Efeitos práticos no problema:**
- Gera a **mesma solução ótima** da versão recursiva.
- Facilita extrair, de forma estruturada, a **sequência de pedidos (t → j)**.

---

## 3) Função de custo do intervalo
- **Propósito:** `Custo(t→j)` agrega, de forma simples, todos os componentes do problema (pedido \(K\), compra \(C\), estocagem \(H\)).
- **Como é usada:** chamada tanto na `dp(t)` quanto no preenchimento iterativo de `V[t]`, garantindo **consistência** entre as duas abordagens.

---

## 4) Reconstrução do plano ótimo
- **Top-down:** após computar `dp`, reavaliamos os `j` viáveis em cada `t` selecionando aquele que atinge o custo mínimo armazenado, formando a lista de intervalos \((t \to j)\).
- **Bottom-up:** usamos o vetor `nxt[t]` salvo durante a tabela para caminhar `t → nxt[t] + 1`, montando os intervalos de modo direto.

---

## 5) Verificação de equivalência
- **O que comparamos:** custo total do plano da recursiva vs. custo total do plano da iterativa.
- **Critério:** devem ser **iguais** (diferenças apenas numéricas de arredondamento). Isso garante que ambas implementam a mesma DP corretamente.

---

## 6) Parâmetros e extensões
- **Parâmetros usados:** \(D\) (demandas), \(T\), \(K\), \(C\), \(H\).
- **Possíveis extensões:** custos que variam no tempo, capacidade de compra, lead time, e custo residual no fim do horizonte. A estrutura da DP se mantém, alterando apenas a função de custo e/ou os estados.

---
