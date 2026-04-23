async function mostrarCarrinho()
{
    const resposta = await fetch("http://10.110.134.2:8080/api/get/carrinho")

    if (!resposta.ok) {
        alert("ERRO AO CARREGAR CARRINHO!")
    }
    else{
        const dados = await resposta.json()

        const carrinho = document.getElementById("carrinho")

        carrinho.innerHTML = "";

        for (let dado of dados){
            total = total + dado.preco
            let linha = `
                teste
                <img src="${dado.imagem}" alt="Hambúrguer" class="cart-item__image">

                <div class="cart-item__info">

                    <div class="cart-item__top">
                        <h3 class="cart-item__name">${dado.nome}</h3>
                        <button class="remove-item-btn" title="Remover item">🗑️</button>
                    </div>

                    <div class="cart-item__bottom">
                        <span class="cart-item__price">R$ ${dado.preco}</span>
                    </div>
                </div>
            `

            carrinho.innerHTML += linha

        }
    }
}

mostrarCarrinho();