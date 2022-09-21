const form = document.getElementById('registerForm')

// alert(form)

form.addEventListener('submit', function (ev){
    const password = document.getElementById("inputSenha")
    const confirmPassword = document.getElementById("inputConfirmSenha")
    
    if(password.value == confirmPassword.value) {
        return true
        
    }else{
        ev.preventDefault()
        alert(`As senhas não estão iguais. Verifique Por favor!!`)
        return false
    }
})

function logar(){
    let aPergunta = document.getElementById("linkLogin")
    aPergunta.style.display="none"
    let aCadastrese = document.getElementById("linkLoginHover")
    aCadastrese.style.display="block"
}

function logarReset(){
    let aCadastrese = document.getElementById("linkLoginHover")
    aCadastrese.style.display="none"
    let aPergunta = document.getElementById("linkLogin")
    aPergunta.style.display="block"
}

function limpa_formulário_cep() {
    //Limpa valores do formulário de cep.
    document.getElementById('inputRua').value=("");
    document.getElementById('inputBairro').value=("");
    document.getElementById('inputCidade').value=("");
}

function meu_callback(conteudo) {
if (!("erro" in conteudo)) {
    //Atualiza os campos com os valores.
    document.getElementById('inputRua').value=(conteudo.logradouro);
    document.getElementById('inputBairro').value=(conteudo.bairro);
    document.getElementById('inputCidade').value=(conteudo.localidade);
} //end if.
else {
    //CEP não Encontrado.
    limpa_formulário_cep();
    alert("CEP não encontrado.");
}
}

function pesquisacep(valor) {

//Nova variável "cep" somente com dígitos.
var cep = valor.replace(/\D/g, '');

//Verifica se campo cep possui valor informado.
if (cep != "") {

    //Expressão regular para validar o CEP.
    var validacep = /^[0-9]{8}$/;

    //Valida o formato do CEP.
    if(validacep.test(cep)) {

        //Preenche os campos com "..." enquanto consulta webservice.
        document.getElementById('inputRua').value="...";
        document.getElementById('inputBairro').value="...";
        document.getElementById('inputCidade').value="...";

        //Cria um elemento javascript.
        var script = document.createElement('script');

        //Sincroniza com o callback.
        script.src = 'https://viacep.com.br/ws/'+ cep + '/json/?callback=meu_callback';

        //Insere script no documento e carrega o conteúdo.
        document.body.appendChild(script);

    } //end if.
    else {
        //cep é inválido.
        limpa_formulário_cep();
        alert("Formato de CEP inválido.");
    }
} //end if.
else {
    //cep sem valor, limpa formulário.
    limpa_formulário_cep();
}
};


