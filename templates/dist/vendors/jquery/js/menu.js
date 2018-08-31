$(document).ready(function () {
    $("#menu_add").click(function () {
        $("#menuAddModal").modal({'show': true, 'backdrop': 'static', 'keyboard': false});

    })

    $("div #menulist").on("click", "div button[id='add_submenu']", function () {
        $("#submenuAddModal").modal({'show': true, 'backdrop': 'static', 'keyboard': false});
        var parent_id = $(this).siblings("input[type='hidden']").val();
        var parent_name = $(this).siblings("p").text();
        // console.log("parent_id:aaaaaaaaaa" + parent_id);
        $("form[id='submenu'] input[name='parentname']").val(parent_name);
        $("form[id='submenu'] input[name='parentid']").val(parent_id);

    })


    $("div #menulist").on("click", "div button[id='del_submenu']", function () {
         $("#delmenuModal").modal({'show': true, 'backdrop': 'static', 'keyboard': false});
         $("#delmenuModal button[type='submit']").click(function(){
             alert("aaaa");
         })
    })

    $("div #menulist").on("click", "div button[id='edit_submenu']", function () {
        // $("#submenuAddModal").modal({'show': true, 'backdrop': 'static', 'keyboard': false});
        // var parent_id = $(this).siblings("input[type='hidden']").val();
        // var parent_name = $(this).siblings("p").text();
        // // console.log("parent_id:aaaaaaaaaa" + parent_id);
        // $("form[id='submenu'] input[name='parentname']").val(parent_name);
        // $("form[id='submenu'] input[name='parentid']").val(parent_id);
        alert("xxxxxxxxx");

    })

})
