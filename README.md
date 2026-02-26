# Sistema de Criptografia de Chaves Assimétricas 🔐

Este é um projeto educacional em Python que demonstra o funcionamento básico de um sistema de criptografia de chaves assimétricas, fortemente inspirado nos conceitos matemáticos do algoritmo **RSA**.

O objetivo deste script é ilustrar como a matemática (números primos, módulo e inversos multiplicativos) permite criar um par de chaves relacionadas, onde uma tranca a informação e apenas a outra pode destrancá-la.

## 🚀 Funcionalidades

O sistema opera com um menu interativo via terminal e oferece os dois pilares da criptografia assimétrica:

1. **Confidencialidade (Encriptar / Decriptar)**
   * **Encriptar:** Usa a **Chave Pública** para embaralhar uma mensagem. Qualquer pessoa pode encriptar, mas ninguém consegue ler.
   * **Decriptar:** Usa a **Chave Privada** para restaurar a mensagem. Apenas o dono da chave privada consegue ler.

2. **Autenticidade (Assinatura Digital / Verificação)**
   * **Assinar:** Usa a **Chave Privada** para "assinar" um documento. Garante que foi você quem escreveu.
   * **Verificar:** Usa a **Chave Pública** para validar a assinatura. Qualquer um pode confirmar que o arquivo veio realmente de você.

## 🛠️ Como a Matemática Funciona (Por Baixo dos Panos)

Sempre que o script é iniciado, ele gera um par de chaves novo exclusivo para a sessão:
1. Sorteia dois números primos aleatórios grandes ($p_1$ e $p_2$).
2. Calcula $n = p_1 \times p_2$ e a Função Totiente de Euler $\phi(n)$.
3. Escolhe a Chave Pública ($pu$) de forma que seja co-prima de $\phi(n)$.
4. Calcula a Chave Privada ($pr$) como o inverso modular multiplicativo de $pu$.