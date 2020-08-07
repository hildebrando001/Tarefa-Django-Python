$(document).ready(function () {
    var deleteBtn  = $('.delete-btn');
    var searchBtn  = $('#searchBtn');
    var searchForm = $('#searchForm');

    $(deleteBtn).on('click', function (e) {
        e.preventDefault();

        var delLink = $(this).attr('href');
        var result  = confirm('Deletar chamado?');

        if (result) {
            window.location.href = delLink;
        }
    });
});

$('#searchBtn').on('click', function() {
    searchForm.submit();
});






setTimeout(function (){
    if ($('#message').length > 0) {
        $('#message').remove();
    }
}, 2000)

let confirmation = confirm("Deseja realmente excluir este item?");


