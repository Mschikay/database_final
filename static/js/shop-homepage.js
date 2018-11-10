// $('#pagination').empty();
// $('#pagination').removeData("twbs-pagination");
// $('#pagination').unbind("page");
// $('#paginationholder').html('');
// $('#paginationholder').html('<ul id="pagination" class="pagination-sm"></ul>');
// $('#pagination').twbsPagination({
//     totalPages: 10,
//     visiblePages: 1,
//     next: 'Next',
//     prev: 'Prev',
//     onPageClick: function (event, page) {
//         //fetch content and render here
//
//     }
// });


$(document).ready(function () {
    $.ajaxSetup ({
        cache: false
    });

    console.log($('form#formLogin').serialize());

    // login
        $("#formLogin").on('click','#buttonLogin', function () {
            console.log('clicked');
            $.ajax({
                url: "http://127.0.0.1:5000",
                type: "POST",
                data: $('form#formLogin').serialize(),
                contentType: 'text/plain; charset=UTF-8',
                success: function (response) {
                    console.log(response.d);
                    console.log("login info sent");
                },
                fail: function (response) {
                    console.log(response.d);
                    console.log("failed");
                }
            })
        });


    // search
        $('#formSearch').on('click', '#buttonSearch', function () {
            console.log('begin sending select');
            $.ajax({
                url: "http://127.0.0.1:5000",
                type: "POST",
                data: $('form#formSelect').serialize(),
                contentType: 'text/plain; charset=UTF-8',
                success: function (response) {
                    console.log(response.d);
                    console.log("search info sent");
                },
                fail: function (response) {
                    console.log(response.d);
                    console.log("failed");
                }
            })
            // }

        });
})



