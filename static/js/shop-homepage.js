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
        cache: true
    });

        $('.list-group-item').bind('click', function(e) {
            e.preventDefault();
            var kind = $(this).text();
            console.log('where is ' + kind + '?');
            var cID = document.getElementById('cID').getAttribute('value');
            var firstName = document.getElementById('firstName').innerText;
            console.log(cID+firstName)

            if (cID === undefined || cID === null){
                alert("please logging")
            }
            var $productDisplay = document.getElementById('productDisplay');
            while($productDisplay.hasChildNodes()) //当elem下还存在子节点时 循环继续
            {
                $productDisplay.removeChild($productDisplay.firstChild);
            }
            $.getJSON('http://127.0.0.1:5000/'+firstName+'_'+cID, {'kind': kind}, function(data) {
                console.log(typeof(data))
                console.log((data.length))
                if (data != null || data != undefined){
                    for (var i=0;i<data.length;i++){

                        var childNode = '<div class="col-lg-4 col-md-6 mb-4">\n' +
                            '                    <div class="card h-100">\n' +
                            '                        <p class="notShow">'+data[i].amount+'</p>\n' +
                            '                        <p class="notShow">'+data[i].kind+'</p>\n' +
                            '                        <p class="notShow">'+data[i].pID+'</p>\n' +
                            '                        <a href="#"><img class="card-img-top" src="'+data[i].picture+'" alt=""></a>\n' +
                            '                        <div class="card-body">\n' +
                            '                            <h4 class="card-title">\n' +
                            '                                <a href="#">'+data[i].p_name+'</a>\n' +
                            '                            </h4>\n' +
                            '                            <h5>'+data[i].price+'</h5>\n' +
                            '                            <p class="card-text">{{ productDescription }}</p>\n' +
                            '                        </div>\n' +
                            '                        <div class="card-footer">\n' +
                            '                            <svg class="add" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" version="1.1" id="Capa_1" x="0px" y="0px" width="22px" height="22px" viewBox="0 0 510 510" style="enable-background:new 0 0 510 510;" xml:space="preserve">\n' +
                            '                        \t\t<path d="M255,0C114.75,0,0,114.75,0,255s114.75,255,255,255s255-114.75,255-255S395.25,0,255,0z M382.5,280.5h-102v102h-51v-102    h-102v-51h102v-102h51v102h102V280.5z" fill="#e3a034"/>\n' +
                            '                            </svg>\n' +
                            '                        </div>\n' +
                            '                    </div>\n' +
                            '                </div>'
                        console.log(data.productName, data.productPrice, data.productDescription);
                        $('#productDisplay').append(childNode);
                    }
                }
            });
        })
})

function appendNode(){

}



