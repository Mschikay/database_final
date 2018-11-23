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
        cache: true,
        async: false
    });


    // search by kind
    $('.list-group-item').on('click', function(e) {
        e.preventDefault();
        var kind = $(this).text();
        console.log('where is ' + kind + '?');
        var cID = document.getElementById('cID').getAttribute('value');
        var firstName = document.getElementById('firstName').innerText;
        console.log(cID+firstName);

        if (cID === undefined || cID === null){
            alert("please logging");
        }
        var $productDisplay = document.getElementById('productDisplay');
        while($productDisplay.hasChildNodes()) //当elem下还存在子节点时 循环继续
        {
            $productDisplay.removeChild($productDisplay.firstChild);
        }
        $.getJSON('http://127.0.0.1:5000/'+firstName+'_'+cID, {'kind': kind}, function(data) {
            console.log(typeof(data));
            console.log((data.length));
            if (data != null || data !== undefined){
                appendNodeProduct(data);
            }
        });
    });

    // search by input
    $('#buttonSearch').on('click', function(e){
        e.preventDefault();

        var firstName = document.getElementById('firstName').innerText;
        var cID = document.getElementById('cID').getAttribute('value');
        var selectRecord = document.getElementById('selectRecord').value;
        var $productDisplay = document.getElementById('productDisplay');


        while($productDisplay.hasChildNodes()) //当elem下还存在子节点时 循环继续
        {
            $productDisplay.removeChild($productDisplay.firstChild);
        }

        console.log(selectRecord);

        $.getJSON('http://127.0.0.1:5000/'+firstName+'_'+cID, {'search': selectRecord}, function(data) {
            console.log(typeof(data));
            console.log((data.length));
            if (data != null || data !== undefined){
                appendNodeProduct(data);
            }
        });

        //
        // $.ajax({
        //     type: 'POST',
        //     url: 'http://127.0.0.1:5000/'+firstName+'_'+cID,
        //     // dataType: 'text/html',
        //     success: function(data, status){
        //         console.log(status);
        //         console.log(typeof(data));
        //         console.log(data)
        //         if (data != null || data !== undefined) {
        //             // appendNodeProduct(data);
        //             // var str = $(data).find("body").text();
        //             // var json = $.parseJSON(str);
        //             // console.log(json)
        //         }
        //     },
        //     error: function(){
        //         console.log('???');
        //     }
        // })
    })
});

function appendNodeProduct(data){
    for (var i=0;i<data.length;i++){

        var childNode = '<div class="col-lg-4 col-md-6 mb-4">\n' +
            '                    <div class="card h-100">\n' +
            '                        <p class="notShow amount">'+data[i].amount+'</p>\n' +
            '                        <p class="notShow kind">'+data[i].kind+'</p>\n' +
            '                        <p class="notShow pID">'+data[i].pID+'</p>\n' +
            '                        <a class="picture" href="#"><img class="card-img-top" src="'+data[i].picture+'" alt=""></a>\n' +
            '                        <div class="card-body">' +
            '                            <h4 class="card-title pName">' +
                                            data[i].p_name +
            '                            </h4>' +
            '                            <h5>'+data[i].price+'</h5>' +
            '                            <p class="card-text">remain: '+data[i].amount+'</p>' +
            '                        </div>\n' +
            '                        <div class="card-footer">\n' +
            '                            <svg class="add" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" version="1.1" id="Capa_1" x="0px" y="0px" width="22px" height="22px" viewBox="0 0 510 510" style="enable-background:new 0 0 510 510;" xml:space="preserve">\n' +
            '                        \t\t<path d="M255,0C114.75,0,0,114.75,0,255s114.75,255,255,255s255-114.75,255-255S395.25,0,255,0z M382.5,280.5h-102v102h-51v-102    h-102v-51h102v-102h51v102h102V280.5z" fill="#e3a034"/>\n' +
            '                            </svg>\n' +
            '                        </div>\n' +
            '                    </div>\n' +
            '                </div>'
        $("svg.add").off("click").on("click", add);

        $('#productDisplay').append(childNode);
    }
}


    // update quantity of total item
    function calItem(){
        var num1 = $("#addedItem").children(".shop").length;
        if (num1 > 0){
            $("#total").html(num1+" items");
            $(".check").show();
        }
        else{
            $(".check").hide();
        }
    }
    // check empty or all is space
    function isNull(str){
        if ( str == "" || str == null || str == undefined ) return true;
        var regu = "^[ ]+$";
        var re = new RegExp(regu);
        return re.test(str);
    }
    // drop the item
    function dropItem(){
        $(this).parent(".shop").remove();
        calItem();
    }
    // add to my shopping list
    function addToList(content){
        // display the good
        $("#addedItem").prepend("<div class='shop'><div class='del'>DEL</div><div class='good'>"+content+"</div><input class='checkCount' type='number' min='0' value='0'/><div class='drop'>DROP</div></div>");
        // bind when every time we add a dom node.
        // if we don't bind again, the event cannot be added to the dynamically created node
        $(".del").off("click").on("click", deleteFromList);
        $(".drop").on("click", dropItem);
        calItem();
    }
    // put the item back to the shoppinglist from which I will buy later
    function undoItem() {
        var content = $(this).next().text();
        addToList(content);
        $(this).parent(".shop").remove();
        calItem();
    }
    // put items to the place where things are those I will buy later
    function deleteFromList(){
        // remove the good for later consideration
        var content1 = $(this).next().text();
        $(this).parent(".shop").remove();
        calItem();
        $("#buyLater").prepend("<div class='shop'><div class='undo'>UNDO</div><div class='good'>"+content1+"</div><div class='drop'>DROP</div></div>");
        $(".undo").off("click").on("click", undoItem);
        $(".drop").on("click", dropItem);
    }
    // check if the goods are legal and put in shopping list
    function add(){
        var amountElem = $(this).parent().siblings('.notShow.amount')[0];
        var amount = parseInt(amountElem.innerText);
        console.log(amount);
        if (amount <= 0){
            return -1;
        }
        else{
            var item = $(this).parent().parent().children('div.card-body')[0].childNodes[1].innerText;
            console.log(item);
            addToList(item);
        }
        // // var content = $("#addItem").val();
        // // $("#addItem").val("");
        // if (isNull(content)){
        //     alert("INPUT IS ILLEGAL");
        //     return;
        // }
        // else{
        //     addToList(content);
        // }
    }
    $("#addItem").on("enterKey", add);
    $("#addItem").keyup(function(e) {
        if (e.keyCode === 13) {
            $("#addItem").trigger("enterKey");
        }
    });
