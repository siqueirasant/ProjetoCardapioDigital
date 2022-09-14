function cadastre(){
    let aPergunta = document.getElementById("linkCadastre")
    aPergunta.style.display="none"
    let aCadastrese = document.getElementById("linkCadastreHover")
    aCadastrese.style.display="block"
}
function cadastreReset(){
    let aCadastrese = document.getElementById("linkCadastreHover")
    aCadastrese.style.display="none"
    let aPergunta = document.getElementById("linkCadastre")
    aPergunta.style.display="block"
}