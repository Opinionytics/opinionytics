$("#analyzeForm").submit(function(event) {
    event.preventDefault();
    var form = $(event.target);
    var formData = form.serialize();

    $.ajax({
        type: 'POST',
        url: '/get_result_text',
        data: formData,
        timeout: 100000
    }).done(function(response) {
        console.log(response);
    }).fail(function(response) {
        console.log(response);
        alert("Erreur réseau. Veuillez vérifier votre connexion.");
    });
});