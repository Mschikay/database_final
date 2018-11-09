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

        $("button#buttonLogin").click(function () {
            console.log('clicked');
            $.ajax({
                url: "http://127.0.0.1:5000",
                type: "POST",
                data: $('form.formLogin').serialize(),
                contentType: 'json; charset=UTF-8',
                success: function (response) {
                    console.log(response.d);
                    console.log("login info sent");
                },
                fail: function (response) {
                    console.log(response.d);
                    console.log("failed");
                }
            })

        })
})




