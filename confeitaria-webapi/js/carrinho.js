
window.onresize = () => {
    let actualWindowSize = window.outerWidth
    const divCarrinho = document.getElementById('carrinhoDivIcon')
    console.log(actualWindowSize);
    if (divCarrinho.classList.contains("active") && actualWindowSize <= 750){
        console.log("entrou no loop");
        divCarrinho.style.width = "80%"
        divCarrinho.style.borderRadius = "27.5px"
    }else if (divCarrinho.classList.contains("active") && actualWindowSize >= 750){
        console.log("entrou no loop maior ativado");
        divCarrinho.style.width = "580px"
        divCarrinho.style.borderRadius = "35px"
    }
    
    if (!divCarrinho.classList.contains("active") && actualWindowSize <= 1560){
        console.log("entrou no loop pequeno menor");
        divCarrinho.style.width = "70px"
        divCarrinho.style.height = "70px"
        divCarrinho.style.right = "10%"
    }else if (!divCarrinho.classList.contains("active") && actualWindowSize >= 1560){
        console.log("entrou no loop pequeno maior");
        divCarrinho.style.width = "80px"
        divCarrinho.style.height = "80px"
        divCarrinho.style.right = "15%"
    }

}


let clickCarrinho = () => {
    let actualWindowSize = window.outerWidth
    const divCarrinho = document.getElementById('carrinhoDivIcon')
    const imgCarrinho = document.getElementById('imgCarrinho')
    const contentCarrinho = document.getElementById('iframeCarrinho')
    const buttonVoltar = document.getElementById("voltarCarrinho")
    const buttonFinalizar = document.getElementById("finalizarCarrinho")
    
    
    divCarrinho.style.bottom = "10%"
    divCarrinho.style.zIndex = "2"
    divCarrinho.style.width = "580px"
    divCarrinho.style.height = "600px"
    imgCarrinho.style.display= "none"
    divCarrinho.style.top = "25%"
    divCarrinho.style.borderRadius = "35px"
    divCarrinho.removeAttribute("onmouseout")
    divCarrinho.removeAttribute("onmouseover")
    divCarrinho.removeAttribute("onclick")
    divCarrinho.classList.add("active")
    contentCarrinho.style.display= "block"
    setTimeout(() => {
        buttonVoltar.style.display="block"
        buttonFinalizar.style.display="block"
    }, 150);  

    if (actualWindowSize <= 750){
        divCarrinho.style.width = "80%"
        divCarrinho.style.borderRadius = "27.5px"
    }
}

let hoverOnCarrinho = () => {
    const divCarrinho = document.getElementById('carrinhoDivIcon')
    let actualWindowSize = window.outerWidth

    divCarrinho.style.transform = "scale(1.1)" 

    if (actualWindowSize <= 1560){
        divCarrinho.style.transform = "scale(1.2)" 
    }
}
let hoverOutCarrinho = () => {
    const divCarrinho = document.getElementById('carrinhoDivIcon')
    divCarrinho.style.transform = "scale(1)" 
}
let returnCarrinho = () => {
    const windowSize1560 = window.matchMedia("(max-width: 1560px)")
    const divCarrinho = document.getElementById('carrinhoDivIcon')
    const imgCarrinho = document.getElementById('imgCarrinho')
    const contentCarrinho = document.getElementById('iframeCarrinho')
    const buttonVoltar = document.getElementById("voltarCarrinho")
    const buttonFinalizar = document.getElementById("finalizarCarrinho")

    divCarrinho.setAttribute("onmouseover", "hoverOnCarrinho()")
    divCarrinho.setAttribute("onmouseout", "hoverOutCarrinho()")
    setTimeout(() => {divCarrinho.setAttribute("onclick", "clickCarrinho()")}, 1);
    divCarrinho.classList.remove("active")
    console.log("clicou");

    if(windowSize1560.matches){
        divCarrinho.style.top = "85%"
        divCarrinho.style.borderRadius = "100px"
        divCarrinho.style.display = "flex"
        divCarrinho.style.justifyContent = "center"
        divCarrinho.style.width = "70px"
        divCarrinho.style.height = "70px"
        divCarrinho.style.right = "10%"
        imgCarrinho.style.display= "block"
        contentCarrinho.style.display= "none"
        buttonVoltar.style.display="none"
        buttonFinalizar.style.display="none"    
        
    }else{
        divCarrinho.style.top = "85%"
        divCarrinho.style.borderRadius = "100px"
        divCarrinho.style.display = "flex"
        divCarrinho.style.justifyContent = "center"
        divCarrinho.style.width = "80px"
        divCarrinho.style.height = "80px"
        divCarrinho.style.right = "15%"
        imgCarrinho.style.display= "block"
        contentCarrinho.style.display= "none"
        buttonVoltar.style.display="none"
        buttonFinalizar.style.display="none"    
    }
    
}