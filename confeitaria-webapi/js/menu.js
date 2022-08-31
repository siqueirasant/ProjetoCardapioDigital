/* Alterna entre adicionar e remover a classe "responsiva" ao menu quando o usuário clica no ícone */
function myFunction() {
    var x = document.getElementById("menuGeralId");
    if (x.className === "menuGeral") {
      x.className += " responsive";
    } else {
      x.className = "menuGeral";
    }
  }