$("#analyzeForm").submit(function(event) {
    event.preventDefault();
    var form = $(event.target);
    var formData = form.serialize();

    $.ajax({
        type: 'POST',
        url: form.attr('action'),
        data: formData,
        timeout: 100000
    }).done(function(response) {
        console.log(response);
    }).fail(function(response) {
        console.log(response);
        alert("Network error. Please check your connection.");
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
        alert("Network error. Please check your connection.");
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
        alert("Network error. Please check your connection.");
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
        alert("Network error. Please check your connection.");
    });
});