$("#analyzeForm").submit(function(event) {
    event.preventDefault();
    var form = $(event.target);
    var formData = form.serialize();

    $.ajax({
        type: 'POST',
        url: '/get_result_text/',
        data: formData,
        timeout: 100000
    }).done(function(response) {
        console.log(response);
    }).fail(function(response) {
        console.log(response);
        alert("Erreur réseau. Veuillez vérifier votre connexion.");
    });
});


$("#signInForm").submit(function(event) {
    event.preventDefault();
    var form = $(event.target);
    var formData = form.serialize();

    $.ajax({
        type: 'POST',
        url: '/signin/',
        data: formData,
        timeout: 100000
    }).done(function(response) {
        console.log(response);
    }).fail(function(response) {
        console.log(response);
        alert("Erreur réseau. Veuillez vérifier votre connexion.");
    });
});


$("#signUpForm").submit(function(event) {
    event.preventDefault();
    var form = $(event.target);
    var formData = form.serialize();

    $.ajax({
        type: 'POST',
        url: '/signup/',
        data: formData,
        timeout: 100000
    }).done(function(response) {
        console.log(response);
    }).fail(function(response) {
        console.log(response);
        alert("Erreur réseau. Veuillez vérifier votre connexion.");
    });
});


$("#contactForm").submit(function(event) {
    event.preventDefault();
    var form = $(event.target);
    var formData = form.serialize();

    $.ajax({
        type: 'POST',
        url: '/contact/',
        data: formData,
        timeout: 100000
    }).done(function(response) {
        console.log(response);
    }).fail(function(response) {
        console.log(response);
        alert("Erreur réseau. Veuillez vérifier votre connexion.");
    });
});