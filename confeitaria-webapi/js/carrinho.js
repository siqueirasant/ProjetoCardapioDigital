let clickCarrinho = () => {
    const divCarrinho = document.getElementById('carrinhoDivIcon')
    divCarrinho.style.width = "900px"
    divCarrinho.style.height = "600px"
    divCarrinho.style.top = "15%"
    divCarrinho.style.borderRadius = "40px"

}

let outCarrinho = () => {
    const divCarrinho = document.getElementById('carrinhoDivIcon')
    divCarrinho.style.width = "80px"
    divCarrinho.style.height = "80px"
    divCarrinho.style.top = "710px"
    divCarrinho.style.right = "15%"
    divCarrinho.style.borderRadius = "100px"
    divCarrinho.style.display = "flex"
    divCarrinho.style.justifyContent = "center"
    divCarrinho.style.alignItems = "center"
}

// #carrinhoDivIcon{
//     width: 80px;
//     height: 80px;
//     right: 15%;
//     top: 710px;
//     border-radius: 100px;
//     display: flex;
//     justify-content: center;
//     align-items: center;
// }