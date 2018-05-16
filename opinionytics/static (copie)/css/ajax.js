var form=$("#analyzeForm");
form.submit(function(event) {
    event.preventDefault();
    var formData = form.serialize();
    alert(formData);

    $.ajax({
        dataType: "json",
        type: 'POST',
        url: 'http://localhost:3100/getText/',
        data: formData
    }).done(function(response) {
        console.log(response.resultat)
        if(response.resultat) {
            $(location).attr('href', 'tableau_de_bord.html')
        }
    }).fail(function(response) {
        alert("Erreur réseau. Veuillez vérifier votre connexion.")
    })
});

var emailInput = $('#inscriptionForm input[name=email]')
emailInput.focusout(function(event) {
    $.ajax({
        dataType: "json",
        type: 'POST',
        url: 'ActionServlet',
        data: { 
            email: emailInput.get(0).value,
            action: 'verifExiste'
        }
    }).done(function(response) {
        if(response.resultat)
            emailInput.get(0).setCustomValidity("Adresse e-mail déjà utilisée, veuillez en essayer une autre")
        else
            emailInput.get(0).setCustomValidity("")
    })
})

function verifierEgal(champ1, champ2, message) {
    champ2.focusout(function(event) {
        if(champ1.get(0).value != champ2.get(0).value)
            champ2.get(0).setCustomValidity(message)
        else
            champ2.get(0).setCustomValidity("")
    })
}

verifierEgal($('#inscriptionForm input[name=email]'), $('#inscriptionForm input[name=emailconf]'), "Deux adresses e-mail différentes ont été entrées")
verifierEgal($('#inscriptionForm input[name=mdp]'), $('#inscriptionForm input[name=mdpconf]'), "Deux mots de passe différents ont été entrées")

